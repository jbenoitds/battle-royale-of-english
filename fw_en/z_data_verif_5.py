from files.data.data12 import data_all_texts5
from modulesu.library import items, zones, locations

(

# Specific initialize searches texts
init_search_text1,
init_search_text2,
init_search_text3,
init_search_text4,
init_search_text5,

) = (


# Specific initialize searches texts
data_all_texts5["init_search_text1"],
data_all_texts5["init_search_text2"],
data_all_texts5["init_search_text3"],
data_all_texts5["init_search_text4"],
data_all_texts5["init_search_text5"],

)


#11
initsearchtext_verif = [init_search_text1, init_search_text2, init_search_text3,
                        init_search_text4, init_search_text5]

#14
dataNOs = 0
textNOs = 0


#11 initsearchtext_verif
print('\n \n #11 Initsearchtext Verif \n')
for initsearchtext in initsearchtext_verif:
    if isinstance(initsearchtext, str):
        print('YES, initsearchtext is a string')
        if 300 <= len(initsearchtext) <= 400:
            print('YES, initsearchtext is between 300 and 400 charac')
        else:
            print(f'NO, initsearchtext is not between 300 and 400 charac {len(initsearchtext)}')
            textNOs += 1
    else:
        print('NO, initsearchtext is not a string')
        dataNOs += 1


#16 dataNOs Count
print('\n \n #16 NOs Count \n')
print(f'dataNOs = {dataNOs}')
print(f'textNOs = {textNOs}')
print('\n \n')