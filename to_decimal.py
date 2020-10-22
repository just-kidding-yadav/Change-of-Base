# Converting any base to decimal

def base_to_dec(num, base):
    decimal = 0
    m = 1
    for i in range(len(num)):
        decimal += (m) * num[-i-1]
        m = m * base
    return decimal
