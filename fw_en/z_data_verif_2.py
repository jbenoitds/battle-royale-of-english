from files.data.data12 import data_all_texts2
from modulesu.library import items, zones, locations

(

# Text (characters)
boss_text,
boss_netext,
enemy_position,
boss_position,

) = (

# Text (characters)
data_all_texts2["boss_text"],
data_all_texts2["boss_netext"],
data_all_texts2["enemy_position"],
data_all_texts2["boss_position"],

)

#3b bosspositionstext
bosspositionstext_verif = [boss_text, boss_netext, enemy_position, boss_position]

dataNOs = 0
textNOs = 0

#3b enemytext_verif
print('\n \n #3b Boss and Position Text Verif \n')
for enemytext in bosspositionstext_verif:
    if isinstance(enemytext, str):
        print('YES, enemytext is a string')
        if 300 <= len(enemytext) <= 400:
            print('YES, enemytext is between 300 and 400 charac')
        else:
            print(f'NO, enemytext is not between 300 and 400 charac ({len(enemytext)})')
            textNOs += 1
    else:
        print('NO, enemytext is not a string')
        textNOs += 1

#16 dataNOs Count
print('\n \n #16 NOs Count \n')
print(f'dataNOs = {dataNOs}')
print(f'textNOs = {textNOs}')
print('\n \n')