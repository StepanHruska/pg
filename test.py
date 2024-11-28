from aplikace import soucet, fibonachi
from zkouska1.py import pozpatku

def test_soucet2():
    assert soucet(1, 1) == 2

def text_soucet3():
    assert soucet(1, 2) == 3

def test_fibonachi_5():
    assert fibonachi(5) == [1, 1, 2, 3, 5]

def test_fibonachi_10():
    assert fibonachi(10) == [1, 1, 2, 3, 5]

def test_pozpatku():
    assert pozpatku("ahoj") == "joha"
    assert pozpatku("ahoj jak se mas") == "sam es kaj joha"