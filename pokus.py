
def hello_world():
    print("Hello world")

#funkce ktera vypise pozadovany pocet hvezd
def five_stars(limit):
    i = 0
    while i<limit:
        print("*")
        i += 1

#funkce overi zda je number v rozmezi minimum - maximum a vypise textovy vystup
def in_range(number, minimum, maximum):
    if minimum<number<maximum:
        print("Number", number, "in range", minimum, "-", maximum)
    else:
        print("Number", number, "is out of range", minimum, "-", maximum)

#funkce vrati nejvetsi z cisel a, b, c
def max_number(a, b, c):
    if a>b and a>c:
        return a
    if b>a and b>c:
        return b
    else:
        return c


m = max_number(1, 2, 3)
print(m)
m = max_number(100, 10 ,1)
print(m)
m = max_number(1.1, 1.3, 1.2)
print(m)