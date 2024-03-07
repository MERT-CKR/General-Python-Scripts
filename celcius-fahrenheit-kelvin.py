print("bu birimlerden hangisini hangisine dönüştürmek isterseniz?")

print("1. Celcius-> Fahrenheit \n2. Fahrenheit-> Celcius")
print("\n3. Celcius-> Kelvin  \n4. Kelvin-> Celcius")
print("\n5. Kelvin-> Fahrenheit \n6. Fahrenheit-> Kelvin\n")
print("(1,2,3,4,5,6)")

option = int(input("\n>>"))


def cel_to_fah():
    celcius = float(input("Celcius'u girin: "))
    fahrenheit = celcius * 9 / 5 + 32
    print(f"{celcius} Celcius = {fahrenheit} Fahrenheit derece")


def fah_to_cel():
    fahrenheit = float(input("Fahrenheit'i girin: "))
    celcius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit} Fahrenheit = {celcius} Celcius derece")


def fah_to_kel():
    fahrenheit = float(input("Fahrenheit'i girin: "))
    kelvin = (fahrenheit - 32) / 1.800 + 273.15
    print(f"{fahrenheit} Fahrenheit = {kelvin} Kelvin derece")


def kel_to_fah():
    kelvin = float(input("Kelvin'i girin: "))
    fahrenheit = (kelvin - 273.15) * 1.8000 + 32.00
    print(f"{kelvin} Kelvin = {fahrenheit} Fahrenheit derece")


def cel_to_kel():
    celcius = float(input("Celcius'u girin: "))
    kelvin = celcius + 273.15
    print(f"{celcius} Celcius = {kelvin} Kelvin derece")


def kel_to_cel():
    kelvin = float(input("Kelvin'i girin: "))
    celcius = kelvin - 273.15
    print(f"{kelvin} Kelvin = {celcius} Celcius derece")




def main(option):
    if option == 1:
        cel_to_fah()
    elif option == 2:
        fah_to_cel()
    elif option == 3:
        cel_to_kel()
    elif option == 4:
        kel_to_cel()
    elif option == 5:
        kel_to_fah()
    elif option == 6:
        fah_to_kel()
    else:
        print("Geçersiz seçim")


main(option)