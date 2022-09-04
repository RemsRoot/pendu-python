def tiret_espace(mot_test):
    if "-" in mot_test :
       return mot_test.index("-")
    if " " in mot_test :
       return mot_test.index(" ")
    else:
        return 0 

def remplacement_see(lettre, position, mot):
    tableau = []
    for lettre_mot in mot :
        tableau.append(lettre_mot)
        
    for lettre_position in position:
        tableau[lettre_position] = lettre 
        
    mot_fonction = ""
    for item in tableau :
        mot_fonction += item   
    return str(mot_fonction)         