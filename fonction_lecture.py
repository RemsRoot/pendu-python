import random

def lecture_txt():
    with open("liste_mot.txt", "r") as file :
        mots = []
        for ligne in file :
            mots.append(ligne[:len(ligne)-1])
    return mots

def random_word(liste_mots):
    id_random = random.randrange(1, len(liste_mots), 1)
    return liste_mots[id_random]

def enlever_accent(mot):
    liste_accent = [["é", "e"],
                    ["è", "e"],
                    ["ç", "c"],
                    ["à", "a"],
                    ["ù", "u"],
                    ["ï", "i"],
                    ["ê", "e"],
                    ["î", "i"],
                    ["â", "a"],
                    ["ô", "o"],
                    ["û", "u"]]
    mot_accent = mot
    
    for couple in liste_accent :
        mot_accent = [element.replace(couple[0], couple[1]) for element in mot_accent]
        
    mot_ok = ""
    
    for lettre in mot_accent :
        mot_ok += lettre
        
    return mot_ok