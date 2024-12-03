def bin_to_dec(binarni_cislo):
    # funkce spocita hodnotu predavaneho binarniho cisla (binarni_cislo muze byt str i int!!!)
    # 111 -> 7
    # "101" -> 5
   cislo = str(binarni_cislo)
   cislo = cislo[::-1]
   i = 0
   vysledek = 0
   while i <= len(cislo):
    for i in range(len(cislo)):
        misto = int(cislo[i])
        mocnina = 2**i
        decimal = misto * mocnina
        vysledek += decimal
    i += 1
    return vysledek
   #i = 0
   #vysledek = 0
   #while i <= len(cislo):
    #if cislo[i] == "1":
     #  vysledek = vysledek + (2**int(i))
    #else:bbbbvbh
    #   vysledek = vysledek
    #i + 1




   #while i <= len(cislo):
    #if cislo[i] == "1":
     #  vysledek + (2^int(i))
      # i + 1
    #else:
     #  i+1    


def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128

print(bin_to_dec(10000000))
print(len("11101"))