from fonction_lecture import lecture_txt, random_word, enlever_accent
from fonction_affichage import remplacement_see
from fonctiontest import lettredansmot,positiondeslettres,testlettre
from fonctionstockage import stock, stockage, test_stockage
NBESSAIE = 10  

if __name__ == "__main__" :
    
    mot = random_word(lecture_txt())
    mot = enlever_accent(mot)
    print(mot)
    see = "_"*len(mot)   
     
    while NBESSAIE > 0 or lettre == "EXIT" :
        lettre = []
        
        while testlettre(lettre) == False :
            lettre = input("Veuillez entrer une lettre : ")
        if test_stockage(lettre) :
            continue
        
        stock(lettre)
            
        if lettredansmot(lettre, mot) != 0 :
            see = remplacement_see(lettre, positiondeslettres(lettredansmot(lettre, mot),mot, lettre), see)
        else:
            NBESSAIE-=1
            
        print(see)
        print("essaies ; ", NBESSAIE)
        
    print("PERDU")