from fonction_lecture import lecture_txt, random_word, enlever_accent
from fonction_affichage import gagner, remplacement_see, tiret_espace, tiret_espace_lettre
from fonctiontest import lettredansmot,positiondeslettres,testlettre
from fonctionstockage import stock, stockage, test_stockage
NBESSAIE = 10  

if __name__ == "__main__" :
    
    mot = random_word(lecture_txt())
    mot = mot.lower()
    mot = enlever_accent(mot)
    see = "_"*len(mot)   
    if tiret_espace(mot) != 0 :
        see = remplacement_see(tiret_espace_lettre(mot), tiret_espace(mot), see) 
        
        
    while NBESSAIE > 0 :
        lettre = []
        print(see)
        while testlettre(lettre) == False :
            lettre = input("Veuillez entrer une lettre : ")
        if test_stockage(lettre) :
            continue
        
        stock(lettre)
            
        if lettredansmot(lettre, mot) != 0 :
            see = remplacement_see(lettre, positiondeslettres(lettredansmot(lettre, mot),mot, lettre), see)
        else:
            NBESSAIE-=1
        
        if gagner(see) :
            print("YOU WIN !!!")
            exit()
        print("essaies ; ", NBESSAIE)
        
    print("PERDU")