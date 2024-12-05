def sudy_lichy(cislo):
    cislo = int(cislo)
    if cislo % 2 == 0:
        return "sudy"
    else:
        return "lichy"

def test_sudy_lichy():
    assert sudy_lichy(2) == "sudy"
    assert sudy_lichy(5) == "lichy"
    assert sudy_lichy(215) == "lichy"
    assert sudy_lichy("84") == "sudy"
