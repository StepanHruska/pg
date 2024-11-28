def obvod_ctverce(delka_strany):
    # funkce vypocita obvod ctverce z delky jeho strany
    a = int(delka_strany)
    obvod = 4*a
    return obvod

def obsah_ctverce(delka_strany):
    # funkce vypocita obsah ctverce z delky jeho strany
    obsah = int(delka_strany)*int(delka_strany)
    return obsah

def pocet_pismen(text, pismeno):
    i = 0
    #while pozice <= len(text) + 1:
    #   if str(text[pozice]) == pismeno:
    #        i += 1
    #        pozice += 1
    #    else:
    #        pozice +=1
    #return i
    for p in text:
        if p == pismeno:
            i+=1
    return i

def index_pismene(text, pismeno):
    index = []
    i = 0

    while i < len(text):
        if text[i] == pismeno:
            index.append(i)
        i+= 1
    return index

def fibonachi(maximum):
    cisla = [1, 1]
    soucet = cisla[-2] + cisla[-1]
    while soucet <= maximum:
        cisla.append(soucet)
        soucet = cisla[-2] + cisla[-1]
    return cisla


if __name__ == "__main__":
    print(obsah_ctverce(5))
    print(obsah_ctverce(5))
    print(pocet_pismen ("ahoj jak se mas?", "a"))
    print(index_pismene("ahoj jak se mas honzo", "a"))
    print(fibonachi(10))