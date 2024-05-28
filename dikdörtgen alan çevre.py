kısaKenar = int(input("kısa kenar: "))
uzunKenar = int(input("uzun kenar kenar: "))

def alan(kısaKenar,uzunKenar):
  alan = uzunKenar*kısaKenar
  return alan


def cevre(kısaKenar,uzunKenar):
  cevre = (uzunKenar+kısaKenar)*2
  return cevre


print(alan(kısaKenar,uzunKenar))
print(cevre(kısaKenar,uzunKenar))
