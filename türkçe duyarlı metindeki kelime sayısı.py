import unicodedata

def normalize_turkish(text):
    text_normalized = unicodedata.normalize('NFKC', text)
    text_normalized = text_normalized.replace("İ", "i")
    text_normalized = text_normalized.casefold()
    return text_normalized

kelime = input("Kelimeyi girin: ")

metin = input("metni girin:")

islem = input("Büyük harf küçük harf duyarlılığı olsun mu? (Evet/Hayır): ")

if islem.lower() == "evet" or islem == "1":
    sayac = metin.count(kelime)
else:
    metin = normalize_turkish(metin)
    kelime = normalize_turkish(kelime)
    sayac = metin.count(kelime)

print(f"Metin içinde '{kelime}' kelimesi {sayac} defa geçmektedir.")
