### Checklist Level u ###

## Analog Implementation

# ! Manual scoring (test and adjust, can also be made positive)
- start with 1000 pts
- search wrong location: -100
- choose wrong object: -100
- lose battle: -100
- lose against boss - 200
- reach 0: lose



## To do (!mandatory, *optional)

# ! Boss ~~
- ~~ Could be Kakachi ~~
- ~~ What does he trigger? ~~
- ~~ Capacities: more lives? Hurt more? ~~
- ~~ If phrases + conj, might need special_boss ~~
- ~~ Debug ~~ 

# ! Everest Counter visible

# ! Everest counter save

# * Trap / shield save

# * Map Creation
- In-game map of the level, callable with 'm' and enter
- Could show map and position / ... + orientation / ... + directions to zone

# * Change character
- Just download and vary blit

# * Update
- Technique karaté: Face au Judo; 2-shot
- Os, bullet: Caché; Donne +1 Ulti 
- Increase map range (with map feature above)


## Completed

# ~~ ! Initial instru ~~
- ~~ J'ai enlevé, c'était rouge (idem pour Pre-Outro) ~~

# ~~ ! Character ~~
- ~~ blitter le gars (png full height) ~~
- ~~ Debug ~~

# ~~ ! Everest (mechanism) ~~
- ~~ méchanisme de charge avec special_animal ~~
- ~~ integration dans special_enemy ~~
- ~~ adapt special_animal for evy prep (celle de mission h) ~~
- ~~ blitter Evy normal a cote du gars (png full length) ~~
- ~~ adapter blit display_nal pour switcher avec tiger ~~
- ~~ make sure the number for evy is 7 everywhere (and not 8,9 like before) ~~
- ~~ Debug ~~

# ~~ ! General Debug ~~
- ~~ RGB error ~~
- ~~ missing 91 ~~
- ~~ double school ~~  

# ~~ ! Generate Data ~~
- ~~ Instructions ~~

# ~~ ! Verif ~~
- ~~ Debug ~~

# ~~ ! Searches ~~
- ~~ Debug ~~

# ~~ ! Data ~~
- ~~ Lui donner les specs de ## Info ~~
- ~~ Lui dire que items groupés ~~
- ~~ Lui demander des blagues dans textes ~~
- ~~ Qu'il donne toutes les instructions après les text ~~
- ~~ Qu'il donne nouvelle instruction 'e. attaque' ~~
- ~~ Qu'il donne les objectifs formats courts dans text_objectifs# ~~
- ~~ Cheat and Code both 6 letters ~~
- ~~ Limite text a 400 charac? ~~
- ~~ Objets position: width entre 100 et 900; height entre 50 et 450 ~~
- ~~ Qu'il donne un boss ~~

# ~~  ! Blup 3-5 max ~~

# ~~ ! Verification length ~~
- ~~ if longer than len(phrase), crashes, use email fix for every verification ~~

# ~~ ! Saved Objective ~~
- ~~ Maybe add halves (rounded up) for searches and enemies, so that if 5, saved at 3 too (would be 5 objectives now): complicated because would need to also get items and complete/false things. ~~
- ~~ Found a way more complicated but way better with conditions ~~
- ~~ Implemented in first screen ~~

# ~~ ! Verification script ~~
- ~~ check errors on its side and mine ~~
- ~~ lists ~~
- ~~ verif type, length and accept ~~
- ~~ cross-check matching elements ~~
- ~~ verif types, parts and coords ~~
- ~~ and a huge bunch of other stuff ~~

# ~~ ! Resize items ~~

# ~~ ! New import items ~~

# ~~ ! Generalization 2 ~~
- ~~ Pt pb avec endroit ou data insérée (si trop tôt, assigne pas valeurs des variables basses comme locations coordinate ; si trop tard, donne pas valeurs au variables hautes): réorganiser les 3 (data_all, 'var_basses', 'var_hautes') ~~
- ~~ Blitting of specific object ('carkeys') for specific searches (maybe could fix the non-random searches issue here: see think) ~~
- ~~ Creation of objects database (20aine avec des objets assez généraux pour interprétation dans différents scénarios: clé, boussole, horloge, chaussure, guitare, balle, briquet, smartphone, stylo, tournevis, etc.) ~~

# ~~ * Probably problem with searches ~~
- ~~ They were random, now if specific, how triggered in-game? ~~

# ~~ * Télé ~~
- ~~ Juste pas oublier que c'est là, pas obligé de faire qqchose avec, mais si besoin ~~

# ~~ ! Simplify data as dict ~~

# ~~ ! Location Coordinates Script ~~
- ~~ Takes seeks and return ~~

# ~~ Objectives ~~
- ~~ Counters problem to adapt here ~~
- ~~ Created a objectives dictionary callable like other: objectives[obj_count] ~~
- ~~ /Attention a objectif dans la télé' ~~

# ~~ Mapping ~~
- ~~ Map everything ~~
- ~~ Create smthg special with park ~~

# ~~ Enemies ~~
- ~~ Choose general assignments for number and counter ~~
- ~~ Download all images new enemies ~~
- ~~ resize all ~~
- ~~ min 1 for the objectives ~~

# ~~ Counters ~~
- ~~ Use the spots as counters (enemy_Spots, trap_spots, etc.) ~~
- ~~ Est-ce qu'on laisse phrase identiques pour ts traps / ts spots? ~~

# ~~ Generalization 1 ~~
- ~~ Most variables ~~
- ~~ Data files ~~
- ~~ Cheat ~~
- ~~ Code ~~
- ~~ Specific positions ~~

# ~~ Sound ~~
- ~~ Create enough for max as others ~~
- ~~ Assign to each ~~
- ~~ Pb l.247 (too many values to unpack) ~~
- ~~ Problem: I coded for 3 different groups of enemies but wanted themes, so just 1 group ~~
  ~~  -> Remove other 2 or could keep both ideas? ~~ 
  - ~~ Download all sounds new enemies ~~

# ~~ Phrases !!! ~~
- ~~ How many for what (specials, enemy, animal) ~~
- ~~ Adjust loading in lvlu ~~
- ~~ Phrase mapping to know which number goes to what, or simply descriptors in name ~~
- ~~ Adjust loading in module ~~
- ~~ evy : put a counter so that it goes through all 3 dictionaries, one at a time ~~

# ~~ Separate the zones ~~
- ~~ Areas (general) ~~
- ~~ Locations (specific) ~~

# ~~ Movements ~~
- ~~ no enter, just asdw ~~

# ~~ Assignments ~~
- ~~ Assign number to enemies and animals (for 'enemy', sound_dict, ...) ~~

# ~~ Static texts ~~
- ~~ Write for Evy Prep ~~

# ~~ * Save progress? ~~
- ~~ Data_id ~~
- ~~ print objectives when completed ~~
- ~~ invisible prompt for completions ~~
- ~~ Coded file save ~~

# ~~ * Kakachi_gang ~~
- ~~ Pareil que télé ~~



## Info

# Specials 
- Dynamic
    .Enemies: 1 - 5 (already a boss)
    .Trap + Shield: 1 - 5
    .Search: 1 - 4
        -> Max of 8 main (enemies or search) and 4-6 trap/shield
            Full Fight: 5 enemies, 1 boss, 1 search and 4 trap/shield (11)
            Full Riddle: 5 Searches, 1 enemy, 1 boss and 4 trap/shield (11)
            Balanced: a mix of enemies and searches (6 total), 1 boss and 4 trap/shield (11)

- Static
    .Boss: 1 : 
    .Anim: 3 :

# Objectives
- 1 for boss (defeat boss)
- 1 for enemies (defeat all enemies)
- 1 fr searches (complete all searches)

### General Batroy ###

# reduire taille des niveaux 2 et 3 (en re-screenshoot)

# voir si peut .exe


