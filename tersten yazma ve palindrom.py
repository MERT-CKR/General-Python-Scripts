metin = input("kelimeyi veya metni girin: ")
print("tersi: ",metin[::-1])
if metin==metin[::-1]:
    print("metin palindromdur")