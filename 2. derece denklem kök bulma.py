import math
def diskriminant():
    a = int(input("denklemdeki A değerini giriniz: "))
    b = int(input("denklemdeki B değerini giriniz: "))
    c = int(input("denklemdeki C değerini giriniz: "))

    diskriminant = b**2 -4*a*c
    print("diskriminant: ",diskriminant)

    if diskriminant==0:
        cakısıkKok =-b/2*a
        print("denklemin 2 kökü aynıdır:",cakısıkKok)

    elif diskriminant <=0:
        print("reel kök yok")
    else:
        x1 = (-b - math.sqrt(diskriminant))/2*a
        x2 = (-b + math.sqrt(diskriminant))/2*a
        print("denklemin 2 farklı reel kökü vardır, x1:",x1,", x2",x2)
diskriminant()
