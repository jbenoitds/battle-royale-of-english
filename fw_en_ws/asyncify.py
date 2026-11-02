"""Web version (pygbag), step 3 of build_web.sh: make the game's blocking pygame loops browser-friendly (pygbag).

In a browser, a loop that never gives control back freezes the tab. This script:
  1. finds every function with a `while` loop that reads events / draws / waits for sound,
     makes it `async def` and adds `await asyncio.sleep(0)` at the top of that loop
     (= wait for the next frame);
  2. makes every function that calls one of those functions async too (repeat until stable),
     and puts `await` in front of the calls.
Usage: python asyncify.py GAME_FOLDER [--dry]
Files skipped: voice.py (rewritten by hand), main.py (async by hand).
"""
import ast, sys, os, glob

YIELD = ('event.get', 'display.flip', 'display.update', 'get_busy', '.tick', 'event.wait', 'event.poll')
SKIP = {'voice.py', 'main.py'}


def game_files(root):
    fs = glob.glob(os.path.join(root, 'z_lvl*.py')) + glob.glob(os.path.join(root, 'modules*', '*.py'))
    return sorted(f for f in fs if os.path.basename(f) not in SKIP)


def own_nodes(node):
    """Child nodes of node, not entering nested function/class/lambda definitions."""
    for ch in ast.iter_child_nodes(node):
        if isinstance(ch, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Lambda)):
            continue
        yield ch
        yield from own_nodes(ch)


def all_funcs(tree):
    return [n for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]


def yield_loops(func):
    loops = []
    for n in own_nodes(func):
        if isinstance(n, ast.While):
            calls = [ast.unparse(c.func) for c in own_nodes(n) if isinstance(c, ast.Call)]
            if any(any(k in c for k in YIELD) for c in calls):
                loops.append(n)
    return loops


def call_name(call):
    f = call.func
    if isinstance(f, ast.Name):
        return f.id
    if isinstance(f, ast.Attribute):
        return f.attr
    return None


def main():
    root = sys.argv[1]
    dry = '--dry' in sys.argv
    trees = {}
    for f in game_files(root):
        trees[f] = ast.parse(open(f, encoding='utf-8').read())

    async_names = set()
    seeds = {}
    for f, t in trees.items():
        for fn in all_funcs(t):
            if yield_loops(fn):
                async_names.add(fn.name)
    changed = True
    while changed:
        changed = False
        for f, t in trees.items():
            for fn in all_funcs(t):
                if fn.name in async_names:
                    continue
                if any(isinstance(c, ast.Call) and call_name(c) in async_names for c in own_nodes(fn)):
                    async_names.add(fn.name)
                    changed = True
    # names also defined as sync somewhere else would be ambiguous: report
    print('async functions:', sorted(async_names))

    warnings = []
    for f, t in trees.items():
        parents = {}
        for n in ast.walk(t):
            for ch in ast.iter_child_nodes(n):
                parents[ch] = n
        src = open(f, encoding='utf-8').read()
        lines = src.encode('utf-8').split(b'\n')
        point = []    # (line, col, text) in-line insertions
        newlines = []  # (line, indent, text) new line before `line`
        for fn in all_funcs(t):
            if fn.name not in async_names:
                continue
            if isinstance(fn, ast.FunctionDef):
                point.append((fn.lineno, fn.col_offset, b'async '))
            for loop in yield_loops(fn):
                first = loop.body[0]
                if first.lineno == loop.lineno:
                    warnings.append(f'{f}:{loop.lineno} one-line while: not handled')
                    continue
                line = first.lineno
                # put the await above any decorator/comment-free first statement
                newlines.append((line, first.col_offset, b'await asyncio.sleep(0)  # web: let the browser draw (one frame)'))
            for c in own_nodes(fn):
                if isinstance(c, ast.Call) and call_name(c) in async_names:
                    p = parents.get(c)
                    if isinstance(p, ast.Await):
                        continue
                    anc = p
                    while anc is not None and anc is not fn:
                        if isinstance(anc, (ast.GeneratorExp,)):
                            warnings.append(f'{f}:{c.lineno} async call inside a generator expression')
                        anc = parents.get(anc)
                    bare = (isinstance(p, ast.Expr) or
                            (isinstance(p, (ast.Assign, ast.AugAssign, ast.AnnAssign, ast.Return)) and p.value is c))
                    if bare:
                        point.append((c.lineno, c.col_offset, b'await '))
                    else:
                        point.append((c.lineno, c.col_offset, b'(await '))
                        point.append((c.end_lineno, c.end_col_offset, b')'))
        # async functions referenced without being called (callbacks)
        for n in ast.walk(t):
            if isinstance(n, ast.Name) and n.id in async_names and isinstance(n.ctx, ast.Load):
                p = parents.get(n)
                if not (isinstance(p, ast.Call) and p.func is n):
                    warnings.append(f'{f}:{n.lineno} {n.id} used without a call (callback?)')
        # module-level calls to async functions
        for c in own_nodes(t):
            if isinstance(c, ast.Call) and call_name(c) in async_names:
                warnings.append(f'{f}:{c.lineno} module-level call to {call_name(c)}')
        if not point and not newlines:
            continue
        for line, col, text in sorted(point, key=lambda x: (x[0], x[1]), reverse=True):
            b = lines[line - 1]
            lines[line - 1] = b[:col] + text + b[col:]
        for line, indent, text in sorted(newlines, reverse=True):
            lines.insert(line - 1, b' ' * indent + text)
        out = b'\n'.join(lines).decode('utf-8')
        out = 'import asyncio  # web version (pygbag): see asyncify.py\n' + out
        compile(out, f, 'exec')  # must still be valid Python
        print(f'{os.path.relpath(f, root)}: {len(point)} edits, {len(newlines)} frame waits')
        if not dry:
            open(f, 'w', encoding='utf-8', newline='').write(out)
    for w in warnings:
        print('WARNING', os.path.relpath(w.split(':')[0], root), w.split(':', 1)[1])


main()
