def acıbul():
    acı1 =int(input("birinci açıyı girin: "))
    acı2 =int(input("ikinci açıyı girin: "))
    acı3 =180-(acı1+acı2)
    print(f"3. Açı:",acı3)
acıbul()

def ucgenAC():#AC = alan,çevre
    h = int(input("yüksekliği gir: "))
    a =int(input("a kenarını gir: "))
    b =int(input("b kenarını gir: "))
    c = int(input("tabanı gir:(c kenarı) "))
    print(f"üçgenin Alanı: {(h*c)/2}, Çevresi: {a+b+c}")
ucgenAC()
