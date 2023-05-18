print("Celciusu Fahrenheit'e çevirmek için 1 yazın")
print("fahrenayti Celcius'a çevirmek için 2 yazın")
islem = input()

def celToFah():
    Celcius = int(input("Celciusu gir:"))
    Fahrenheit =Celcius*9/5 +32
    print(Celcius,"Celcius = ",Fahrenheit,"Fahrenheit derece")


def fahToCel():
    Fahrenheit = int(input("Fahrenheit gir:"))
    Celcius =(Fahrenheit-32)*5/9
    print(Fahrenheit,"Fahrenheit = ",Celcius,"Celcius derece")


if islem == "1":
    celToFah()

elif islem == "2":
    fahToCel()

else:
    print("yanlış yazmış olmalısın")


