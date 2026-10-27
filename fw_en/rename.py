import os

def rename_files(directory):
    for root, _, files in os.walk(directory):
        for filename in files:
            # Split the filename and extension
            name, ext = os.path.splitext(filename)
            if len(name) < 3:
                # Skip files with names shorter than 3 characters
                continue
            
            # Construct new filename with first, second, and last character
            new_name = f"{name[0]}{name[1]}{name[-1]}{ext}"
            old_path = os.path.join(root, filename)
            new_path = os.path.join(root, new_name)
            
            # Rename the file
            try:
                os.rename(old_path, new_path)
                print(f"Renamed: {old_path} -> {new_path}")
            except PermissionError as e:
                print(f"Permission error with {old_path}: {e}")
            except Exception as e:
                print(f"Unexpected error with {old_path}: {e}")

# Specify the top-level directory to start renaming
directory = 'files/new_enemies'
rename_files(directory)
