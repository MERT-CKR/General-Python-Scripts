import random

girilen = int(input("bir ile kaç arasında bir tahminde bulunmak istersiniz? "))
hak = int(input("kaç deneme hakkı istersiniz ?"))

if hak >= girilen:
    hak = int(girilen/2)
    if hak == float:
        hak = hak-0.5
    print(f"Deneme Hakkınız bu kadar büyük olmamalı, hakkınız {hak} olarak ayarlandı")
cevap = random.randint(1,girilen+1)

while hak>0:
    tahmin = int(input(f"Tahmin Et: "))
    
    if tahmin < cevap:
        print("Yukarı")
        hak-=1

    elif tahmin > cevap:
        print("Aşşağı")
        hak-=1
    else:
        print(f"Tebrikler doğru cevabı buldun Cevap:{cevap}, kalan hakkınız:{hak}")
        break
        
if hak==0:
    print(f"hakkınız bitti, sayıyı bulamadınız doğru cevap {cevap} olmalıydı")