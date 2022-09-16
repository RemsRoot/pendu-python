from fonction_lecture import lecture_txt, random_word, enlever_accent
from fonction_affichage import gagner, remplacement_see, tiret_espace, tiret_espace_lettre
from fonctiontest import lettredansmot,positiondeslettres,testlettre
from fonctionstockage import stock, test_stockage
from pendu_design import design_life_pendu, win, loose, Hangman_games
import tkinter as tk

#################################################################################################################################################
################################################### CONTANTE ####################################################################################
#################################################################################################################################################
NBESSAIE = 10  


#################################################################################################################################################
################################################### Initialisation variable #####################################################################
#################################################################################################################################################
    
mot = ""
while len(mot) < 3 :
    mot = random_word(lecture_txt())
mot = mot.lower()
mot = enlever_accent(mot)

see = "_"*len(mot)   
if tiret_espace(mot) != 0 :
    see = remplacement_see(tiret_espace_lettre(mot), tiret_espace(mot), see) 

stockage = []  
#################################################################################################################################################
################################################### Fonction ####################################################################################
#################################################################################################################################################    

######################################################### fonction d'entrée ##################################################################### 
def Entry_fonction(event) :
    global NBESSAIE
    global mot
    global see
    
    if gagner(see) :
        chaine_see.configure(text = mot)
        chaine_essaie.configure(text =  win)
    else :    
        lettre = entree.get()
        
        if NBESSAIE > 0 and lettre != "" and len(lettre) >  1 and not test_stockage(lettre, stockage):
            stock(lettre, stockage)
            if lettre == mot :
                chaine_lettre.configure(text = lettre)
                chaine_see.configure(text = mot)
            else :
                NBESSAIE -= 1
                affichage = ""
                for item in stockage[:len(stockage)-1] : 
                    affichage += item + " / "
                affichage += stockage[len(stockage)-1]
                chaine_lettre.configure(text = affichage)
                chaine_see.configure(text = see)
                
        elif NBESSAIE > 0 and lettre != "" and len(lettre) ==  1 and not test_stockage(lettre, stockage) and testlettre(lettre):                
            stock(lettre, stockage)  
            if lettredansmot(lettre, mot) != 0 :
                see = remplacement_see(lettre, positiondeslettres(lettredansmot(lettre, mot),mot, lettre), see)
            else:
                NBESSAIE-=1
            affichage = ""
            for item in stockage[:len(stockage)-1] : 
                affichage += item + " / "
            affichage += stockage[len(stockage)-1]
            chaine_lettre.configure(text = affichage)
            chaine_see.configure(text = see)
            
        elif test_stockage(lettre) :
            chaine_lettre.configure(text = "\"" + lettre + "\" a déjà été tester")
            
        else :
            chaine_lettre.configure(text = "Entrer une lettre ou un mot")
            
        chaine_essaie.configure(text =  str(design_life_pendu(NBESSAIE)))
        if NBESSAIE == 0 :
            chaine_see.configure(text = mot)
            chaine_essaie.configure(text =  loose)
        

######################################################### fonction bouton #######################################################################     
def exit_bouton():
   exit() 

######################################################### fonction retry ########################################################################     
def retry_bouton():
    global mot
    global NBESSAIE
    mot = ""
    while len(mot) < 3 :
        mot = random_word(lecture_txt())
    mot = mot.lower()
    mot = enlever_accent(mot)  
    if tiret_espace(mot) != 0 :
        see = remplacement_see(tiret_espace_lettre(mot), tiret_espace(mot), see) 
    NBESSAIE = 10    
    see = "_"*len(mot) 
    chaine_essaie.configure(text =  str(design_life_pendu(NBESSAIE))) 
    chaine_see.configure(text = see)  
    chaine_lettre.configure(text = "Entrer une lettre ou un mot") 
    global stockage
    stockage = []
    chaine_essaie.configure(text = Hangman_games)

#################################################################################################################################################
################################################### objet graphique #############################################################################
#################################################################################################################################################
fenetre = tk.Tk()
entree = tk.Entry(fenetre)
chaine_lettre = tk.Label(fenetre)
chaine_see = tk.Label(fenetre)
chaine_essaie = tk.Label(fenetre)
btn = tk.Button(fenetre, text ="quitter", command = exit_bouton)
btn_rty = tk.Button(fenetre, text ="RETRY", command = retry_bouton)


################# personalisation de la page ##############################

fenetre.geometry("200x280")

#################################################################################################################################################
############################################################## MAIN ############################################################################# 
#################################################################################################################################################  

if __name__ == "__main__" :
    
    # définir paramètres de la page   
    chaine_essaie.pack()
    chaine_essaie.configure(text = Hangman_games)
    
    entree.pack()
    
    chaine_lettre.pack()
    chaine_lettre.configure(text = "Entrer une lettre ou un mot")
    
    chaine_see.pack()
    chaine_see.configure(text = see)
    
    entree.bind('<Return>', Entry_fonction) 
    
    btn_rty.pack()
    btn.pack()
    
    fenetre.mainloop()