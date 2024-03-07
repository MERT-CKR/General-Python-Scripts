a = float(input("sayı1: "))
b = float(input("sayı2: "))
print("toplama için 1\nçıkarma için 2\nçarpma için 3\nbölme için 4")
islem = int(input("islem: "))
def toplama (a,b):
    print(a+b)
    
def cikarma (a,b):
    print("a-b: ",a-b)

def carpma (a,b):
    print("a*b: ",a*b)

def bolme (a,b):
    print("a/b: ",a/b)

if islem ==1:
    toplama(a,b)
elif islem ==2:
    cikarma(a,b)
elif islem ==3:
    carpma(a,b)
elif islem ==4:
    bolme(a,b)
else:
    print("sayi 1 ile 4 arasında olmalı")
