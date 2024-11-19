def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    nact = {11: "jedenact", 12: "dvanact", 13: "trinact", 14: "ctrnact", 15: "patnact", 16: "sestnact", 17: "sedmnact", 18: "osmnact", 19: "devatenact"}
    desitky = {1: "deset", 2: "dvacet", 3: "tricet", 4: "ctyricet", 5: "padesat", 6: "sedesat", 7: "sedmdesat", 8: "osmdesat", 9: "devadesat"}
    jednoty = {1: "jedna", 2: "dva", 3: "tri", 4: "ctyri", 5: "pet", 6: "sest", 7: "sedm", 8: "osm", 9: "devet"}
    cislo = int(cislo)
    if cislo == 0:
        return "nula"
    elif cislo == 100:
        return "sto"
    elif cislo >= 11 and cislo <= 19:
        return nact[cislo]
    else:
        d = cislo // 10
        j = cislo % 10
        vysledek = desitky[d]
        if j != 0:
            vysledek += " " + jednoty[j]
        return vysledek


if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)
    #sdfsdf