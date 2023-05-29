import unicodedata
def text_normalized(text):
    #bu fonksiyon metinleri küçük harfe çevirirken İ,i,I,ı harflerinin türkçe uyumunu dikkate alarak çevirir
    #lower ve casefold methodlarında yaşadığım unicode uyumsuzluğu sonucunda yapmaya karar verdim.
    text_normalized = unicodedata.normalize('NFKC', text)
    text_normalized = text_normalized.replace("İ", "i").replace("I","ı")
    text_normalized = text_normalized.casefold()
    return text_normalized

kelime = input("Aramak istediğiniz kelimeyi girin: ")

metin = input("içinde aranacak metni girin:")

islem = input("Büyük harf küçük harf duyarlılığı olsun mu? (Evet/Hayır): ")

if islem.lower() == "evet" or islem == "1":
    sayac = metin.count(kelime)
else:
    metin = text_normalized(metin)
    kelime = text_normalized(kelime)
    sayac = metin.count(kelime)

print(f"Metin içinde '{kelime}' kelimesi {sayac} defa geçmektedir.")
