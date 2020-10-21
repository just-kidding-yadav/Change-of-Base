# Converting any base to decimal

def add(list):
    l = len(list)
    result = 0
    for i in range(l):
        result += list[i]
    return result

def base_to_dec(num, base):
    l = []
    m = str(num)
    x = len(m)

    for i in range(x):
        l.append(m[-1-i])
    a = []

    for i in range(x):
        a.append((base ** i) * int(l[i]))

    decimal = add(a)
    return decimal
