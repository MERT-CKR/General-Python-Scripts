kenar = int(input("herhangi bir kenarı girin: "))

def alan(kenar):
  a = kenar ** 2
  return a


def cevre(kenar):
  c = kenar * 4
  return c


print(alan(kenar))
print(cevre(kenar))
