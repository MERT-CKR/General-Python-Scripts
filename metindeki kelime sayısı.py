kelime =input("kelimeyi giriniz: ")
metin = input("metni giriniz: ")
print("büyük harf küçük harf duyarlılığı vardır")

sayac = metin.count(kelime)
print("metin içinde {} kelimesi {} defa geçmektedir".format(kelime,sayac))

