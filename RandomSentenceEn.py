from random import choice

nouns = ("puppy", "car", "rabbit", "girl", "monkey")
verbs = ("runs", "hits", "jumps", "drives", "barfs") 
adv = ("crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally.")
adj = ("adorable", "clueless", "dirty", "odd", "stupid")

# asking user as to how many sentences he would like to generate 
for _ in range (int (input ("How many sentences? (Int): "))): 
    print(list(map(choice, [nouns, verbs, adv, adj])))
    print('Leo Steiner / Soar / ComputeSoar on Github')

input('Press ENTER to exit')

# Leo Steiner / Soar / ComputeSoar on Github
