islem=0
sayac=1
t2=0
t3=0
s=0
def saatTop():
    islem = int(input("kaç tane saat toplamak istersiniz: "))

    while sayac <= islem:
        sayac+=1
        t0 = int(input("saat gir (3): "))
        t1 = int(input("dakika gir (38): "))
        t2+=t1
        t3+=t0
    
    if t3>0:
        t3=t3*60
        t2=t2+t3
        print(t2,"dk")
        
    while t2>=60:
        s+=1
        t2-=60
    print(f"{s}.{t2} saat")
saatTop()