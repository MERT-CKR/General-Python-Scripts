import math

def Daire():

    pi = math.pi
    r =float(input("yarıçapı girin(r): "))
    def daireAlan(pi,r):
        print("Dairenin Alanı:",pi*r**2)
    daireAlan(pi,r)

    def daireCevre(pi,r):
        print("dairenin çevresi: ",2*pi*r)
    daireCevre(pi,r)
Daire()