sayi = int(input("Sayıyı giriniz: "))
faktoriyel = 1

if sayi <= 0:
    print("Sıfırın faktöriyeli 1'dir ve negatif sayıların faktöriyeli yoktur.")
else:
    for i in range(1, sayi + 1):
        faktoriyel *= i

    print(sayi, "sayısının faktöriyeli:", faktoriyel)
