LETTRES = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def lettredansmot(lettre, motrandom) :
    
    i = 0
    
    for lettre1 in motrandom :
        
        if lettre == lettre1 :
            i += 1
    return i

def positiondeslettres(i, motrandom, lettre) :
    
    k = []
    
    if i != 0 :
        j = -1
        
        for lettre1 in motrandom :
            j += 1
            
            if lettre == lettre1 :
                k.append(j)
    return k

def testlettre(lettre, lettresutilises):
    
    lettre = input("Veuillez entrer une lettre : ")
    
    while lettre not in LETTRES :
        lettre = input("Vous n'avez pas rentré de lettre. Veuillez recommencer et rentrer une lettre : ")
        
    while lettre in lettresutilises :
        lettre = input("Vous avez rentré une lettre déjà utilisé. Veuillez recommencer et rentrer une lettre que vous n'avez pas encore essayé : ")
    lettresutilises.append(lettre)
    
    return lettre