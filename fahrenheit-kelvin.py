print("Fahrenheit'i Kelvin'e çevirmek için 1 yazın")
print("Kelvin'i Fahrenheit'e çevirmek için 2 yazın")
islem = input()

def fahToKel():
    fah = int(input("Fahrenheit gir:"))
    print(fah,"Fahrenheit =",(fah-32)/1.800+273.15,"kelvin derece")
    

def kelToFah():
    kel = int(input("Kelvin gir:")) 
    print(kel,"kelvin =",(kel-273.15)*1.8000+32.00,"fahrenheit derece")
    


if islem == "1":
    fahToKel()

elif islem == "2":
    kelToFah()

else:
    print("yanlış yazmış olmalısın")


