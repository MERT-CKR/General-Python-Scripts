h = int(input("yüksekliği gir (m): "))
g = 9.8
t = (2 * h / g) ** 0.5

print("Bu formül, yalnızca yerçekimi ivmesi sabit kabul edildiğinde ve diğer faktörler (hava sürtünmesi vb.) göz ardı edildiğinde doğru sonuçlar verir.")
print("yere düşeceği süre (saniye):", t)
