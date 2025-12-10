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


def sucet_parne(z: list) -> int:
    sucet = 0
    for i in range(len(z)):
        if z[i] % 2 == 0:
            sucet += z[i]
    return sucet

print(sucet_parne(generuj(10)))


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


def parne_pozicie(zoznam1) -> list:
    zoznam2 = []
    for i in range(len(zoznam1)):
        if i % 2 == 0:
            zoznam2.append(zoznam1[i])
    return zoznam2

print(parne_pozicie(generuj(10)))


def nie_cisla(zoznam1: list) -> list:
    zoznam2 = []
    for i in range(len(zoznam1)):
     if not (type(zoznam1[i])==int or type(zoznam1[i])==float):
         zoznam2.append(zoznam1[i])
    return zoznam2

print(nie_cisla(['kuk', 5, 'ahoj', -1, 2.5, 4, None, 7, [2, -12], 8, 'servus', 11]))


def spolu_do_retazca(zoznam1: list) -> str:
    retazec = ""
    for i in range(len(zoznam1)):
        retazec += str(zoznam1[i])
    return retazec

print(spolu_do_retazca(generuj(10)))


def zoznam_mocnin(n: int) -> list:
    zoznam1 = []
    for i in range(1,n):
        zoznam1.append(i**2)
    return zoznam1

print(zoznam_mocnin(10))





