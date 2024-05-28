def ucgenAC():
    h = int(input("yüksekliği gir: "))
    a = int(input("a kenarını gir: "))
    b = int(input("b kenarını gir: "))
    c = int(input("tabanı gir (c kenarı): "))
    
    if a + b > c and a + c > b and b + c > a:
        print(f"Üçgenin Alanı: {(h * c) / 2}, Çevresi: {a + b + c}")
    else:
        print("Geçersiz üçgen kenarları.")

ucgenAC()

def acibul():
    aci1 = int(input("birinci açıyı girin: "))
    aci2 = int(input("ikinci açıyı girin: "))
    
    if aci1 + aci2 < 180:
        aci3 = 180 - (aci1 + aci2)
        print(f"Üçüncü açı: {aci3}")
    else:
        print("Açıların toplamı 180'den büyük olamaz.")

acibul()
