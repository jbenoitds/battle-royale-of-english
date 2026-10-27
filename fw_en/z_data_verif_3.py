from files.data.data12 import data_all_texts3
from modulesu.library import items, zones, locations

(
# Text (objectives)
text_all, 
text_1,
text_2,
text_3,
text_12,
text_13,
text_23,
text_finish, 

) = (


# Text (objectives)
data_all_texts3["text_all"],
data_all_texts3["text_1"],
data_all_texts3["text_2"],
data_all_texts3["text_3"],
data_all_texts3["text_12"],
data_all_texts3["text_13"],
data_all_texts3["text_23"],
data_all_texts3["text_finish"],

)

#5
objectivestext_verif = [text_all, text_1, text_2, text_3, text_12,
                        text_13, text_23, text_finish] 

#14
dataNOs = 0
textNOs = 0


#5 objectivestext_verif
print('\n \n #5 Objective Text Verif \n')
for objectivestext in objectivestext_verif:
    if isinstance(objectivestext, str):
        print('YES, objectivestext is a string')
        if 300 <= len(objectivestext) <= 400:
            print('YES, objectivestext is between 300 and 400 charac')
        else:
            print(f'NO, objectivestext is not between 300 and 400 charac ({len(objectivestext)})')
            textNOs += 1
    else:
        print('NO, objectivestext is not a string')
        dataNOs += 1

#16 dataNOs Count
print('\n \n #16 NOs Count \n')
print(f'dataNOs = {dataNOs}')
print(f'textNOs = {textNOs}')
print('\n \n')