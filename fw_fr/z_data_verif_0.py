from files.data.data13 import data_all_else
from modulesu.library import items, zones, locations

(
# Data ID
data_id,
quest_title,

# Number of Enemies
enemy_spots,

# ID of Boss
boss,

# ID of Enemies
enemy1,
enemy2,
enemy3,
enemy4,
enemy5,

# Number of Events
search_spots,

# Text (decoy, edoc)
decoy,
edoc,

# Zones
d_trap_pool, 
d_shield_pool, 
d_search_pool, 
d_enemy_pool,
d_boss_pool,

# Specific locations
d_spec_location1,
d_spec_location2,
d_spec_location3,
d_spec_location4,
d_spec_location5,

# Specific real items
item1,
item2,
item3,
item4,
item5,

# Specific fake1 items
fake1item1,
fake1item2,
fake1item3,
fake1item4,
fake1item5,

# Specific fake2 items
fake2item1,
fake2item2,
fake2item3,
fake2item4,
fake2item5,

# Specific item position
position_item1,
position_item2,
position_item3,
position_item4,
position_item5,

# Specific fake1 item position
position_fake1item1,
position_fake1item2,
position_fake1item3,
position_fake1item4,
position_fake1item5,

# Specific fake2 item position
position_fake2item1,
position_fake2item2,
position_fake2item3,
position_fake2item4,
position_fake2item5,

# Sound (av, co, db, etc.)
tag1,
tag2,
tag3,
tag4,
tag5,
tagboss

) = (

# Data ID
data_all_else["data_id"],
data_all_else["quest_title"],

# Number of Enemies
data_all_else["enemy_spots"],

# ID of Boss
data_all_else["boss"],

# ID of Enemies
data_all_else["enemy1"],
data_all_else["enemy2"],
data_all_else["enemy3"],
data_all_else["enemy4"],
data_all_else["enemy5"],

# Number of Events
data_all_else["search_spots"],

# Text (decoy, edoc)
data_all_else["decoy"],
data_all_else["edoc"],

# Zones
data_all_else["d_trap_pool"],
data_all_else["d_shield_pool"],
data_all_else["d_search_pool"],
data_all_else["d_enemy_pool"],
data_all_else["d_boss_pool"],

# Specific locations; 'none' if none
data_all_else["d_spec_location1"],
data_all_else["d_spec_location2"],
data_all_else["d_spec_location3"],
data_all_else["d_spec_location4"],
data_all_else["d_spec_location5"],

# Specific real items
data_all_else["item1"],
data_all_else["item2"],
data_all_else["item3"],
data_all_else["item4"],
data_all_else["item5"],

# Specific fake1 items
data_all_else["fake1item1"],
data_all_else["fake1item2"],
data_all_else["fake1item3"],
data_all_else["fake1item4"],
data_all_else["fake1item5"],

# Specific fake2 items
data_all_else["fake2item1"],
data_all_else["fake2item2"],
data_all_else["fake2item3"],
data_all_else["fake2item4"],
data_all_else["fake2item5"],

# Specific item position
data_all_else["position_item1"],
data_all_else["position_item2"],
data_all_else["position_item3"],
data_all_else["position_item4"],
data_all_else["position_item5"],

# Specific fake1 item position
data_all_else["position_fake1item1"],
data_all_else["position_fake1item2"],
data_all_else["position_fake1item3"],
data_all_else["position_fake1item4"],
data_all_else["position_fake1item5"],

# Specific fake2 item position
data_all_else["position_fake2item1"],
data_all_else["position_fake2item2"],
data_all_else["position_fake2item3"],
data_all_else["position_fake2item4"],
data_all_else["position_fake2item5"],

# Sound (av, co, db, etc.)
data_all_else["tag1"],
data_all_else["tag2"],
data_all_else["tag3"],
data_all_else["tag4"],
data_all_else["tag5"],
data_all_else["tagboss"]
)

#1 Spots
spot_verif = [enemy_spots, search_spots]

#2 enemyid
enemyid_verif = [enemy1, enemy2, enemy3, enemy4, enemy5]

#6
decoyedoc_verif = [decoy, edoc]

#7
zones_verif = [d_trap_pool, d_shield_pool, d_search_pool, d_enemy_pool,
               d_boss_pool]

#8
specloc_verif = [d_spec_location1, d_spec_location2, d_spec_location3,
                 d_spec_location4, d_spec_location5]

#9
item_verif = [item1, item2, item3, item4, item5]

#9b
itemfake1_verif = [fake1item1, fake1item2, fake1item3, fake1item4, fake1item5]

#9c
itemfake2_verif = [fake2item1, fake2item2, fake2item3, fake2item4, fake2item5]

#10
positionitem_verif = [position_item1, position_item2, position_item3,
                      position_item4, position_item5]

#10b
positionitemfake1_verif = [position_fake1item1, position_fake1item2, position_fake1item3, 
                      position_fake1item4, position_fake1item5]

#10c
positionitemfake2_verif = [position_fake2item1, position_fake2item2, position_fake2item3, 
                      position_fake2item4,position_fake2item5]

#13
tag_verif = [tag1, tag2, tag3, tag4, tag5]

#14
dataNOs = 0
textNOs = 0

#0 Data
pass #print('\n #0 Data \n')
if isinstance(data_id, int):
    pass #print('YES,data_id is an int')
    if 10 <= data_id <= 100:
        pass #print('YES, data_id is between 10 and 100')
    else:
        print('NO, data_id is not between 10 and 100')
        dataNOs += 1
else:
    print('NO, data_id is not an int')
    dataNOs += 1

#0b Quest title
pass #print('\n \n #0b Quest title \n')
if isinstance(quest_title, str):
    pass #print('YES, quest_title is a string')
else:
    print('NO, quest_title is not a string')
    dataNOs += 1

#1 spot_verif
pass #print('\n \n #1 Spot Verif \n')
for spot in spot_verif:
    if isinstance(spot, int):
        pass #print('YES,spot is an int')
        if 1 <= spot <= 5:
            pass #print('YES, spot is between 1 and 5')
        else:
            print('NO, spot is not between 1 and 5')
            dataNOs += 1
    else:
        print('NO, spot is not an int')
        dataNOs += 1
        
if enemy_spots + search_spots == 6:
    pass #print('YES, enemy + search = 6')
else:
    print('NO, enemy + search != 6')
    dataNOs += 1

#2a enemyid_verif valid
pass #print('\n \n #2a Enemy ID \n')
accept_enemytag = ['av','co','dr','he','ju','na','on','pi','po','ro']
accept_enemynumb = [1, 2, 3, 4, 5]
for index, enemyid in enumerate(enemyid_verif):
    if isinstance(enemyid, str):
        pass #print(f'YES, enemyid {index} is a str')
        if len(enemyid) ==  3:
            pass #print(f'YES, enemyid {index} is 3 charac')
            if isinstance(enemyid[:2], str):
                pass #print(f'YES, enemyid {index} tag is a str')
                if enemyid[:2] in accept_enemytag:
                    pass #print(f'YES, enemyid {index} tag is in accept_enemytag')
                    try:
                        result = int(enemyid[2:])
                        pass #print(f'YES, enemyid[2:] {index} is an int')
                        if result in accept_enemynumb:
                            pass #print(f'YES, enemyid[2:] {index} is in accept_enemynumb')
                        else:
                            print(f'NO, enemyid[2:] {index} is not in accept_enemynumb')
                            dataNOs += 1
                    except ValueError:
                        print(f'NO, enemyid[2:] {index} is not an int')
                        dataNOs += 1
                else:
                    print(f'NO, enemyid tag {index} is not in accept_enemytag')
                    dataNOs += 1
            else:
                print(f'NO, enemyid {index} tag is not a str')
                dataNOs += 1
        else:
            print(f'NO, enemyid {index} is not 3 charac')
            dataNOs += 1
    else:
        print(f'NO, enemyid {index} is not a str')
        dataNOs += 1

#2b enemyid_verif match sound
pass #print('\n \n #2b Enemy ID Sound \n')
for index, enemyid in enumerate(enemyid_verif[:enemy_spots]):
    if enemyid[:2] == tag_verif[index]:
        pass #print(f'YES, enemyid[:2] {index} == tag')
    else:
        print(f'NO, enemyid[:2] {index} != tag')
        dataNOs += 1

#2c verif boss
pass #print('\n \n #2d Boss Verif \n')
if isinstance(boss, str):
    pass #print(f'YES, boss is a str')
    if len(boss) ==  3:
        pass #print(f'YES, boss is 3 charac')
        if isinstance(boss[:2], str):
            pass #print(f'YES, boss tag is a str')
            if boss[:2] == tagboss:
                pass #print(f'YES, boss[:2] = tagboss')
                try:
                    result = int(boss[2:])
                    pass #print(f'YES, boss[2:] is an int')
                    if result == 1:
                        pass #print(f'YES, boss[2:] = 1')
                    else:
                        print(f'NO, boss[2:] != 1')
                        dataNOs += 1
                except ValueError:
                    print(f'NO, boss[2:] is not an int')
                    dataNOs += 1
            else:
                print(f'NO, boss tag != tagboss')
                dataNOs += 1
        else:
            print(f'NO, boss tag is not a str')
            dataNOs += 1
    else:
        print(f'NO, boss is not 3 charac')
        dataNOs += 1
else:
    print(f'NO, boss is not a str')
    dataNOs += 1

#6 decoyedoc_verif
pass #print('\n \n #6 Decoyedoc Verif \n')
for decoyedoc in decoyedoc_verif:
    if isinstance(decoyedoc, str):
        pass #print('YES, decoyedoc is a string')
        if len(decoyedoc) == 6:
            pass #print('YES, decoyedoc = 6 charac')
        else:
            print('NO, decoyedoc != 6 charac')
            dataNOs += 1
    else:
        print('NO, decoyedoc is not a string')
        dataNOs += 1

#7 zones_verif
pass #print('\n \n #7 Zones Verif \n')
for zone in zones_verif:
    if isinstance(zone, str):
        pass #print('YES, zone is a string')
        if zone in zones:
            pass #print('YES, zone is in zones')
        else:
            print('NO, zone is not in zones')
            dataNOs += 1
    else:
        print('NO, zone is not a string')
        dataNOs += 1

#8 specloc_verif
pass #print('\n \n #8 Specloc Verif \n')
for specloc in specloc_verif:
    if isinstance(specloc, str):
        pass #print('YES, specloc is a string')
        if specloc in locations:
            pass #print('YES, specloc is in locations')
        else:
            print('NO, specloc is not in locations')
            dataNOs += 1
    else:
        print('NO, specloc is not a string')
        dataNOs += 1

#9 item_verif
pass #print('\n \n #9 Item Verif \n')
for item in item_verif:
    if isinstance(item, str):
        pass #print('YES, item is a string')
        if item in items:
            pass #print('YES, item is in items')
        else:
            print('NO, item is not in items')
            dataNOs += 1
    else:
        print('NO, item is not a string')
        dataNOs += 1

#9b item_verif
pass #print('\n \n #9b Item1fake Verif \n')
for item in itemfake1_verif:
    if isinstance(item, str):
        pass #print('YES, item1fake is a string')
        if item in items:
            pass #print('YES, item1fake is in items')
        else:
            print('NO, item1fake is not in items')
            dataNOs += 1
    else:
        print('NO, item1fake is not a string')
        dataNOs += 1

#9c item_verif
pass #print('\n \n #9c Item2fake Verif \n')
for item in itemfake2_verif:
    if isinstance(item, str):
        pass #print('YES, item2fake is a string')
        if item in items:
            pass #print('YES, item2fake is in items')
        else:
            print('NO, item2fake is not in items')
            dataNOs += 1
    else:
        print('NO, item2fake is not a string')
        dataNOs += 1

#10 positionitem_verif
pass #print('\n \n #10 Positionitem Verif \n')
for index, positionitem in enumerate(positionitem_verif):
    if isinstance(positionitem,tuple):
        pass #print(f'YES, positionitem {index} is a tuple')
        if len(positionitem) ==  2:
            pass #print(f'YES, positionitem {index} length = 2')    
            if isinstance(positionitem[0],int):
                pass #print(f'YES, positionitem[0] {index} is an integer')
                if 100 <= positionitem[0] <= 900:
                    pass #print(f'YES, positionitem[0] {index} is between 100 and 900')
                    if isinstance(positionitem[1],int):
                        pass #print(f'YES, positionitem[1] {index} is an integer')     
                        if 50 <= positionitem[1] <= 450:
                            pass #print(f'YES, positionitem[1] {index} is between 50 and 450')
                        else:
                            print(f'NO, positionitem[1] {index} is not between 50 and 450')
                            dataNOs += 1
                    else:
                        print(f'NO, positionitem[1] {index} is not an integer')
                        dataNOs += 1
                else:
                    print(f'NO, positionitem[0] {index} is not between 100 and 900')
                    dataNOs += 1
            else:
                print(f'NO, positionitem[0] {index} is not an integer')
                dataNOs += 1
        else:
            print(f'NO, positionitem {index} length is != 2')
            dataNOs += 1
    else:
        print(f'NO, positionitem {index} is not a tuple')
        dataNOs += 1

#10b positionitemfake1_verif
pass #print('\n \n #10b Positionitemfake1 Verif \n')
for index, positionitem in enumerate(positionitemfake1_verif):
    if isinstance(positionitem,tuple):
        pass #print(f'YES, positionitem {index} is a tuple')
        if len(positionitem) ==  2:
            pass #print(f'YES, positionitem {index} length = 2')    
            if isinstance(positionitem[0],int):
                pass #print(f'YES, positionitem[0] {index} is an integer')
                if 100 <= positionitem[0] <= 900:
                    pass #print(f'YES, positionitem[0] {index} is between 100 and 900')
                    if isinstance(positionitem[1],int):
                        pass #print(f'YES, positionitem[1] {index} is an integer')     
                        if 50 <= positionitem[1] <= 450:
                            pass #print(f'YES, positionitem[1] {index} is between 50 and 450')
                        else:
                            print(f'NO, positionitem[1] {index} is not between 50 and 450')
                            dataNOs += 1
                    else:
                        print(f'NO, positionitem[1] {index} is not an integer')
                        dataNOs += 1
                else:
                    print(f'NO, positionitem[0] {index} is not between 100 and 900')
                    dataNOs += 1
            else:
                print(f'NO, positionitem[0] {index} is not an integer')
                dataNOs += 1
        else:
            print(f'NO, positionitem {index} length is != 2')
            dataNOs += 1
    else:
        print(f'NO, positionitem {index} is not a tuple')
        dataNOs += 1
    

#10c positionitemfake2_verif
pass #print('\n \n #10c Positionitemfake2 Verif \n')
for index, positionitem in enumerate(positionitemfake2_verif):
    if isinstance(positionitem,tuple):
        pass #print(f'YES, positionitem {index} is a tuple')
        if len(positionitem) ==  2:
            pass #print(f'YES, positionitem {index} length = 2')    
            if isinstance(positionitem[0],int):
                pass #print(f'YES, positionitem[0] {index} is an integer')
                if 100 <= positionitem[0] <= 900:
                    pass #print(f'YES, positionitem[0] {index} is between 100 and 900')
                    if isinstance(positionitem[1],int):
                        pass #print(f'YES, positionitem[1] {index} is an integer')     
                        if 50 <= positionitem[1] <= 450:
                            pass #print(f'YES, positionitem[1] {index} is between 50 and 450')
                        else:
                            print(f'NO, positionitem[1] {index} is not between 50 and 450')
                            dataNOs += 1
                    else:
                        print(f'NO, positionitem[1] {index} is not an integer')
                        dataNOs += 1
                else:
                    print(f'NO, positionitem[0] {index} is not between 100 and 900')
                    dataNOs += 1
            else:
                print(f'NO, positionitem[0] {index} is not an integer')
                dataNOs += 1
        else:
            print(f'NO, positionitem {index} length is != 2')
            dataNOs += 1
    else:
        print(f'NO, positionitem {index} is not a tuple')
        dataNOs += 1

#13 tag_verif
pass #print('\n \n #13 Tag Verif \n')
acceptag = ['av','co','dr','he','ju','na','on','pi','po','ro']
for tag in tag_verif:
    if isinstance(tag, str):
        pass #print('YES, tag is a string')
        if tag in acceptag:
            pass #print('YES, tag is in acceptag')
        else:
            print('NO, tag is not in acceptag')
            dataNOs += 1
    else:
        print('NO, tag is not a string')
        dataNOs += 1

#14 bosstag_verif
pass #print('\n \n #14 Boss tag Verif \n')
acceptag = ['av','co','dr','he','ju','na','on','pi','po','ro']
if isinstance(tagboss, str):
    pass #print('YES, tagboss is a string')
    if tagboss in acceptag:
        pass #print('YES, tagboss is in acceptag')
    else:
        print('NO, tagboss is not in acceptag')
        dataNOs += 1
else:
    print('NO, tagboss is not a string')
    dataNOs += 1

#15 verif 2-3 diff zones
pass #print('\n \n #15 Verif 2-3 diff zones \n')
unique_elements = set(zones_verif)
if len(unique_elements) in [2, 3]:
    pass #print('YES, zones are 2 or 3')
else:
    print('NO, zones are not 2 or 3')
    dataNOs += 1

#16 dataNOs Count
pass #print('\n \n #16 NOs Count \n')
print(f'dataNOs = {dataNOs}')
print(f'textNOs = {textNOs}')
pass #print('\n \n')