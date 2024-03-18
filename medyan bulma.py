import math
liste = [1,2,3,4,5,6,7,8]

def medyan(L):
    L.sort()
    eleman = len(L)
    if eleman%2==0:
        print("Çift sayı")
        return(eleman/2+eleman/2+1)/2
    else:
        print("Tek sayı")
        return math.ceil(eleman/2)
    
print(medyan(liste))
