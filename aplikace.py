def soucet(a, b):
    return a + b

def fibonachi(maximum):
    result = [1, 1]
    soucet = result[-2] + result[-1]
    while soucet <= maximum:
        result.append(soucet)
        soucet = result[-2] + result[-1]
    return result
