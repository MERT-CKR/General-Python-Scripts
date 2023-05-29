# Araç 1
v1 = int(input("Araç 1 hız/sa : "))
x1 = int(input("Araç 1 başlangıç konumu : "))

# Araç 2
v2 = int(input("Araç 2 hız/sa : "))
x2 = int(input("Araç 2 başlangıç konumu: "))


# Kafa kafaya çarpışma durumu
distance = abs(x2 - x1)  # Mesafeyi hesapla
collision_time = distance / (v1 + v2)  # Çarpışma süresini hesapla
collision_point = x1 + v1 * collision_time  # Çarpışma noktasını hesapla

print("Kafa kafaya çarpışma durumu:")
print("Çarpışma süresi:", collision_time)
print("Çarpışma noktası:", collision_point)
