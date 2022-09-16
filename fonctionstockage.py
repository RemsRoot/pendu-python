def stock(lettre, stockage) :
   return stockage.append(lettre) 
   
def test_stockage(lettre, stockage):
    if lettre in stockage :
       return True
    else :
        return False 