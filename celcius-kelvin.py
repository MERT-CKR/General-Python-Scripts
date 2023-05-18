print("Celcius'u Kelvin'e çevirmek için 1 yazın")
print("Kelvin'i Celcius'a çevirmek için 2 yazın")
islem = input()

def celToKel():
    cel = int(input("Celcius gir:"))
    print(cel,"Celcius =",273.15 + cel,"derece")

def kelToCel():
    kel = int(input("Kelvin gir:"))  
    print(kel,"kelvin =",kel-273.15,"derece")


if islem == "1":
    celToKel()

elif islem == "2":
    kelToCel()

else:
    print("yanlış yazmış olmalısın")


