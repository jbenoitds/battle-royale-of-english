from files.data.data12 import data_all_texts4
from modulesu.library import items, zones, locations

(

# Specific riddles texts
search_riddle1,
search_riddle2,
search_riddle3,
search_riddle4,
search_riddle5,

) = (


# Specific riddles texts
data_all_texts4["search_riddle1"],
data_all_texts4["search_riddle2"],
data_all_texts4["search_riddle3"],
data_all_texts4["search_riddle4"],
data_all_texts4["search_riddle5"],

)


#4
search_riddle_verif = [search_riddle1, search_riddle2, search_riddle3, search_riddle4, search_riddle5]


#14
dataNOs = 0
textNOs = 0


#4 search_riddle_verif
print('\n \n #4 Search Riddle Verif \n')
for search_riddle in search_riddle_verif:
    if isinstance(search_riddle, str):
        print('YES, search_riddle is a string')
        if 300 <= len(search_riddle) <= 400:
            print('YES, search_riddle is between 300 and 400 charac')
        else:
            print(f'NO, search_riddle is not between 300 and 400 charac ({len(search_riddle)})')
            textNOs += 1
    else:
        print('NO, search_riddle is not a string')
        dataNOs += 1


#16 dataNOs Count
print('\n \n #16 NOs Count \n')
print(f'dataNOs = {dataNOs}')
print(f'textNOs = {textNOs}')
print('\n \n')