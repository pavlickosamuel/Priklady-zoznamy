# na vstupe retazec z anglickej abecedy napiste funkciu kde tento retazec bude ako vstupny parameter a funkcia vrati retazec 
# kde male pismena budu vymemene za velke a naopak ostatne ynakz necha tak 

def vymena_pismen(retazec):
    vysledok = ""
    for znak in retazec:
        if znak.islower():
            vysledok += znak.upper()
        elif znak.isupper():
            vysledok += znak.lower()
        else:
            vysledok += znak
    return vysledok

vysledok = vymena_pismen("abcdEFGH1234") 
print(vysledok)  