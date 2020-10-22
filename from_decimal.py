# Converting decimal to any base

def dec_to_base(decimal, base):
    l = []
    while(decimal != 0):
        remainder = decimal % base
        decimal = decimal // base
        l.append(remainder)
    l.reverse()
        
    return l
