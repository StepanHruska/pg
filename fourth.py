def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    # Implementace pravidel pohybu pro různé figury zde.
    typ = figurka["typ"]
    pocatecni_pozice = figurka["pozice"]
    x_start, y_start = pocatecni_pozice
    x_cil, y_cil = cilova_pozice
    # 2. Ověření, že cílová pozice není obsazená
    if cilova_pozice in obsazene_pozice:
        return False

    # 3. Pravidla pohybu pro různé figury
    if typ == "pěšec":
        # Pohyb o jedno pole vpřed
        if x_cil == x_start + 1 and y_cil == y_start:
            if cilova_pozice not in obsazene_pozice:
                return True
        # Pohyb o dvě pole vpřed z výchozí pozice
        elif y_cil == y_start and x_cil == x_start + 2 and x_start == 2:
            if (x_start, y_start + 1) not in obsazene_pozice and cilova_pozice not in obsazene_pozice:
                return True
        else:
            return False

    elif typ == "jezdec":
        # Jezdec se pohybuje ve tvaru "L"
        if (abs(x_cil - x_start), abs(y_cil - y_start)) in [(2, 1), (1, 2)]:
            return True
        else:
            return False

    elif typ == "věž":
        # Věž se pohybuje vertikálně nebo horizontálně bez překážek
        if x_cil == x_start or y_cil == y_start:
            # Určíme směr pohybu
            x_krok = (x_cil - x_start) // max(1, abs(x_cil - x_start)) if x_cil != x_start else 0
            y_krok = (y_cil - y_start) // max(1, abs(y_cil - y_start)) if y_cil != y_start else 0

            # Kontrolujeme volná pole na cestě
            x, y = x_start + x_krok, y_start + y_krok
            while (x, y) != (x_cil, y_cil):
                if (x, y) in obsazene_pozice:
                    return False
                x += x_krok
                y += y_krok
            return True
        else:
            return False


    elif typ == "střelec":
        # Střelec se pohybuje diagonálně bez překážek
        if abs(x_cil - x_start) == abs(y_cil - y_start):
            # Určíme směr pohybu
            x_krok = (x_cil - x_start) // abs(x_cil - x_start)
            y_krok = (y_cil - y_start) // abs(y_cil - y_start)

            # Kontrolujeme volná pole na cestě
            x, y = x_start + x_krok, y_start + y_krok
            while (x, y) != (x_cil, y_cil):
                if (x, y) in obsazene_pozice:
                    return False
                x += x_krok
                y += y_krok
            return True
        else:
            return False

    elif typ == "dáma":
        # Dáma se pohybuje jako věž nebo střelec
        if (x_cil == x_start or y_cil == y_start) or (abs(x_cil - x_start) == abs(y_cil - y_start)):
            # Určíme směr pohybu
            x_krok = (x_cil - x_start) // max(1, abs(x_cil - x_start)) if x_cil != x_start else 0
            y_krok = (y_cil - y_start) // max(1, abs(y_cil - y_start)) if y_cil != y_start else 0

            # Kontrolujeme volná pole na cestě
            x, y = x_start + x_krok, y_start + y_krok
            while (x, y) != (x_cil, y_cil):
                if (x, y) in obsazene_pozice:
                    return False
                x += x_krok
                y += y_krok
            return True
        else:
            return False

    elif typ == "král":
        # Král se pohybuje o jedno pole libovolným směrem
        if max(abs(x_cil - x_start), abs(y_cil - y_start)) == 1:
            return True
        else:
            return False

    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # True, při prvním tahu, může pěšec jít o 2 pole dopředu
    print(je_tah_mozny(pesec, (5, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o tři pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True



    

#def cesta_je_volna(pocatecni_pozice, cilova_pozice, obsazene_pozice):
 #   x_start, y_start = pocatecni_pozice
  #  x_cil, y_cil = cilova_pozice

    # Směr pohybu
   # x_krok = (x_cil - x_start) // max(1, abs(x_cil - x_start)) if x_cil != x_start else 0
    #y_krok = (y_cil - y_start) // max(1, abs(y_cil - y_start)) if y_cil != y_start else 0

    # Projdeme všechna políčka na cestě
   # x, y = x_start + x_krok, y_start + y_krok
    #while (x, y) != (x_cil, y_cil):
     #   if (x, y) in obsazene_pozice:
      #      return False
       # x += x_krok
        #y += y_krok

 #   return True
