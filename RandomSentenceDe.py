from random import choice 

nouns = ("der Bahnhof", "das Gepäck", "der Professor", "die Frist", "die Wurst")
verbs = ("führen", "halten", "leben", "lesen", "zeigen") 
adv = ("oft", "mittlerweile", "zuletzt", "nach", "links")
adj = ("schnell", "schön", "sicher", "odd", "frei")

# Benutzer fragen, wie viele Sätze er generieren möchte
for _ in range (int (input ("Wie viele Sätze? (Int): "))): 
    print(list(map(choice, [nouns, verbs, adv, adj])))
    print('Leo Steiner / Soar / ComputeSoar auf Github')

input('Drücken Sie zum Beenden ENTER')
    
# Leo Steiner / Soar / ComputeSoar auf Github
