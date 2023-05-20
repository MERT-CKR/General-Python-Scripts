import unicodedata
def trLower(text):
    #bu fonksiyon metinleri küçük harfe çevirirken İ,i,I,ı harflerinin uyumunu dikkate alarak çevirir
    #lower ve casefold methodlarında yaşadığım uft-8 uyumsuzluğu sonucunda yapmaya karar verdim.
    text_normalized = unicodedata.normalize('NFKC', text)
    text_normalized = text_normalized.replace("İ", "i").replace("I","ı")
    text_normalized = text_normalized.casefold()
    return text_normalized

kelime = input("Kelimeyi girin: ")

metin = input("metni girin:")

islem = input("Büyük harf küçük harf duyarlılığı olsun mu? (Evet/Hayır): ")

if islem.lower() == "evet" or islem == "1":
    sayac = metin.count(kelime)
else:
    metin = trLower(metin)
    kelime = trLower(kelime)
    sayac = metin.count(kelime)

print(f"Metin içinde '{kelime}' kelimesi {sayac} defa geçmektedir.")
