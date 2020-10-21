# Converting decimal to any base

def dec_to_base(decimal, base):
    l = []
    d = int(decimal)
    
    remainder = d % base
    d = d // base
    l.append(str(remainder))

    while(d != 0):
        remainder = d % base
        d = d // base
        l.append(str(remainder))
    
    num = ""
    for i in range(len(l)):
        num += l[-i-1]
        
    return num
