def operace(typ, a, b):
    moperace = 0
    if typ == "+":
        moperace = a + b
    elif typ == "-":
        moperace = a - b
    elif typ == "*":
        moperace = a * b
    elif typ == "/":
        moperace = a / b
    return moperace

if __name__ == "__main__":
    operace("+", 1, 2)
    operace("-", 2, 2)
    operace("*", 3, 2)
    operace("/", 6, 2)
