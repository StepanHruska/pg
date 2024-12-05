#F = C * 9 / 5 + 32

def prevod_c_na_f(stupne): 
    mezivypocet /= 5
    f = mezivypocet + 32
    return f

def test_prevod_c_na_f():
    assert prevod_c_na_f(100) == 212
    assert prevod_c_na_f(0) == 32