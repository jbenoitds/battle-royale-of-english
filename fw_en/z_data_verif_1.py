from files.data.data12 import data_all_texts1
from modulesu.library import items, zones, locations

(

# Text (characters)
enemy_text1,
enemy_text2,
enemy_text3,
enemy_text4,
enemy_text5,

) = (

# Text (characters)
data_all_texts1["enemy_text1"],
data_all_texts1["enemy_text2"],
data_all_texts1["enemy_text3"],
data_all_texts1["enemy_text4"],
data_all_texts1["enemy_text5"],

)

#3 enemytext
enemytext_verif = [enemy_text1, enemy_text2, enemy_text3, enemy_text4,
                   enemy_text5]

dataNOs = 0
textNOs = 0


#3a enemytext_verif
print('\n \n #3a Enemy Text Verif \n')
for enemytext in enemytext_verif:
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