def tiret_espace(mot_test):
    if "-" in mot_test :
       return [mot_test.index("-")]
    elif " " in mot_test :
       return [mot_test.index(" ")]
    else:
        return 0 

def tiret_espace_lettre(mot_test):
    if "-" in mot_test :
       return "-"
    elif " " in mot_test :
       return " "

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

def gagner(mot_test):
    if "_" not in mot_test:
        return True
    else :
        return False  