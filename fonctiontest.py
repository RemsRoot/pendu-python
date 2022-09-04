LETTRES = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",\
           "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def lettredansmot(lettre, motrandom) :
    i = 0
    for lettre1 in motrandom :
        if lettre == lettre1 :
            i += 1
    return i

def positiondeslettres(position, motrandom, lettre) :
    table_position = []
    if position != 0 :
        counteur_lettre = 0
        for lettre1 in motrandom :
            if lettre == lettre1 :
                table_position.append(counteur_lettre)
            counteur_lettre += 1
    return table_position

def testlettre(lettre):
    
    if lettre in LETTRES :
        return True
    else :
        return False