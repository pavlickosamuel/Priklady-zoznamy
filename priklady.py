#1
import random
def generuj(n: int) -> list:
    zoz = []
    for i in range(n):
        zoz.append(random.randrange(5, 101))
    print (zoz)    
    return zoz

jojo = generuj(10)

print(jojo)
 
for prvok in jojo:
    print(prvok)

for i in range(len(jojo)):
    print(jojo[i])

for i, prvok in enumerate(jojo):
    print(i, prvok)

#2
def sucet_parne(z: list) -> int:
    sucet = 0
    for i in range(len(z)):
        if z[i] % 2 == 0:
            sucet += z[i]
    return sucet

print(sucet_parne(generuj(10)))

#3
def coho_je_viac(z: list) -> str:
    parne = 0
    neparne = 0
    for prvok in range(len(z)):
        if prvok % 2 == 0:
            parne += 1
        else:
            neparne += 1
    if parne > neparne:
        return "parne"
    elif neparne > parne:
        return "neparne"
    else:
        return "rovnake"
    
print(coho_je_viac(generuj(10)))

#4
def parne_pozicie(zoznam1) -> list:
    zoznam2 = []
    for i in range(len(zoznam1)):
        if i % 2 == 0:
            zoznam2.append(zoznam1[i])
    return zoznam2

print(parne_pozicie(generuj(10)))

#5
def nie_cisla(zoznam1: list) -> list:
    zoznam2 = []
    for i in range(len(zoznam1)):
     if not (type(zoznam1[i])==int or type(zoznam1[i])==float):
         zoznam2.append(zoznam1[i])
    return zoznam2

print(nie_cisla(['kuk', 5, 'ahoj', -1, 2.5, 4, None, 7, [2, -12], 8, 'servus', 11]))

#6
def spolu_do_retazca(zoznam1: list) -> str:
    retazec = ""
    for i in range(len(zoznam1)):
        retazec += str(zoznam1[i])
    return retazec

print(spolu_do_retazca(generuj(10)))

#7
def zoznam_mocnin(n: int) -> list:
    zoznam1 = []
    for i in range(1,n):
        zoznam1.append(i**2)
    return zoznam1

print(zoznam_mocnin(10))

#8
import math
def ludolf(n: int) -> list:
    if n <= 15:
        zoznam1 = []
        for i in range(1, n + 1):
            zoznam1.append(round(math.pi, i))
        return zoznam1
    else:
        return False

print(ludolf(6))
print(ludolf(16))
 
#9
def je_usp(zoznam1: list) -> bool:
    for i in range(len(zoznam1) - 1):
        if zoznam1[i] > zoznam1[i + 1]:
            return False
    return True

print(je_usp([1,5,7,12]))
print(je_usp([4,1,5,2, 7,12]))

#10
def maxx(z: list) -> int:
    maximum = z[0]
    for i in range(0, len(z)):
        if z[i] > maximum:
            maximum = z[i]
    return maximum

print(maxx([4, 1, 5, 27, 7, 12]))

#11
def ktory_min(z: list) -> int:
    minimum = z[0]
    index = 0
    for i in range(0, len(z)):
        if z[i] < minimum:
            minimum = z[i]
            index = i
    return index

print(ktory_min([4, 1, 5, 27, -7,12]))

#12
def p_n(z: list) -> list:
    parne = []
    neparne = []
    for i in range(len(z)):
        if z[i] % 2 == 0:
            parne.append(z[i])
        else:
            neparne.append(z[i])
    return [parne, neparne]

print(p_n([2,3,5,2,1,4,6,5,3,7]))






