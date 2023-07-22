default_isim ="Ali"
default_posta="ali@gmail.com"
default_sifre="12345678"

def kayit():
    global default_isim, default_posta, default_sifre
    default_isim = input("isim: ")
    default_posta = input("posta: ")
    default_sifre = input("şifre: ")
    return default_isim + default_posta + default_sifre

def giris():
    global default_isim, default_posta, default_sifre
    girilen_posta = input("e-postanızı girin: ")
    if girilen_posta == default_posta:
        print(f"merhaba {default_isim}, Şifrenizi Girin: ")
        girilen_sifre = input("")
        if default_sifre == girilen_sifre:
            print("giriş başarılı keyifli kullanımlar")
        else:
            print("yanlış şifre")
    else:
        print("e-postanız bulunamadı, kaydolduğunuza emin misiniz ?")

islem = int(input("kayıt olmak için 1'e basın, giriş yapmak için 2'ye basın: "))
if islem == 1:
    kayit()
    print("kayıt başarılı, şimdi giriş yapınız.")
    giris()
elif islem == 2:
    giris()
else:
    print("hatalı deneme")
