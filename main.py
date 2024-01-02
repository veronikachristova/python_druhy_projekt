import random
import math

#1
def vzdialenost(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


x1 = int(input("x1 ="))
y1 = int(input("y1 ="))
x2 = int(input("x2 ="))
y2 = int(input("y1 ="))

dlzka = vzdialenost(x1, y1, x2, y2)
print("dlzka je:", dlzka)

#2
vstup = [random.randint(-5, 5) for i in range(10)]
vstup.sort()

def distinct_cisla(vstup):
  vstup_set = set(vstup)
  return len(vstup_set)

distinct_cisla(vstup)

print(f"pre list: {vstup} plati, ze obsahuje {distinct_cisla(vstup)} unikatnych cisel")

