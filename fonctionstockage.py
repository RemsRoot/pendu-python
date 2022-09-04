stockage = []
def stock(lettre) :
   stockage.append(lettre) 
   
def test_stockage(lettre):
    if lettre in stockage :
       return True
    else :
        return False 