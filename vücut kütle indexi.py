def vki():
    kilo = float(input("Kilonuzu girin (kg): "))
    boy = float(input("Boyunuzu girin (m): "))
    vki = kilo / (boy * boy)
    
    if vki <= 18.5:
        print("Zayıf")
    elif 18.5 < vki < 25:
        print("Normal")
    elif 25 <= vki < 30:
        print("Kilolu")
    elif 30 <= vki < 35:
        print("Obez")
    elif 35 <= vki < 40:
        print("2. Dereceden Obez")
    else:
        print("3. Dereceden Obez")

vki()

    

