def je_prvocislo(cislo):
    """
    Funkce overi, zda zadane cislo je nebo neni prvocislo a vrati True nebo False

    Prvocislo je takove cislo vetsi nez 1, ktere neni delitelne zadnym jinym cislem jenom 1 a samo sebou.

    Napoveda jak otestova prvocislo:
    Cislo 36 vznikne nasobenim:
    1 * 36
    2 * 18
    3 * 12
    4 * 9
    6 * 6
    9 * 4
    12 * 3
    18 * 2
    36 * 1
    Jak vidite v druhe polovine se dvojice opakuji, tzn. v tomto pripade staci overit delitelnost pouze do 6 (vcetne)
    """
    cislo = int(cislo)
    if cislo == 2 or cislo == 3 or cislo == 5 or cislo == 7:
        return cislo
    elif cislo == 1 or cislo == 4:
        return  False
    elif cislo >  5 and cislo % 2 == 0 or cislo % 3 == 0 or cislo % 5 == 0 or cislo % 7 == 0: 
        return False
    else:
        return cislo

def vrat_prvocisla(maximum):
    #seznam = []
    #maximum = int(cislo)
    #i = 1
    #i = int(i)
    #while je_prvocislo(i) == True and maximum >= i:
        #seznam.append(i)
        #i += 1
    #i = int(cislo)
    #maximum = int(maximum)
    #for i in range(1, maximum):
        #while je_prvocislo(i) == True and i <= maximum:
            #seznam.append(i)
            #i += 1
    #if je_prvocislo(i) == True and maximum >= i:
        #seznam.append(i)
    #else:
        #while je_prvocislo(i) == False and maximum >= i:
        #i += 1
    maximum = int(maximum)
    cisla = range(1, maximum)
    prvocisla_list= list(filter(lambda x:je_prvocislo(x), cisla))
    return prvocisla_list

if __name__ == "__main__":
    cislo = input("Zadej maximum: ")
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)
    #print(je_prvocislo(10))
