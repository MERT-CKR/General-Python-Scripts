print("Celciusu Fahrenheit'e çevirmek için 1 yazın")
print("fahrenayti Celcius'a çevirmek için 2 yazın")
islem = input()

def fah():
    Celcius = int(input("Celciusu gir:"))
    Fahrenheit =Celcius*9/5 +32
    print(Fahrenheit,"Fahrenheit derece")


def cel():
    Fahrenheit = int(input("Fahrenheit gir:"))
    Celcius =(Fahrenheit-32)*5/9
    print(Celcius,"Celcius derece")


if islem == "1":
    fah()

elif islem == "2":
    cel()

else:
    print("yanlış değer")


