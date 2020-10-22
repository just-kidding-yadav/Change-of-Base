# Converting from one base to other

import from_decimal
import to_decimal

def string_to_list(s, base):
    l = []
    for i in s:
        if i.isdigit():
            l.append(int(i))
        elif i.isupper():
            l.append(ord(i) - 65 + 10)
        elif i.islower():
            l.append(ord(i) - 97 + 36)
        else:
            return -2
        if l[-1] >= base:
            return -1
    return l

def list_to_string(inp):
    s = ""
    for i in inp:
        if i<10:
            s += str(i)
        elif 10 <= i <= 35:
            s += chr(i - 10 +65)
        else:
            s += chr(i - 36 + 97)
    return s

def convert():
    num1 = input("\n" + "Enter a positive number whose base is to be changed: ")
    b1 = int(input("Enter the base of the number: "))
    b2 = int(input("Enter the base of the final result: "))
    num_1 = string_to_list(num1, b1)

    if b2 > 61:
        print("Please use the output base value less than 62.")
    if(num1[0] == "-"):
        print("The number is negative. Please enter a positive number.")
        return
    elif num_1 == -2:
        print("Invalid Number.")
        return
    elif num_1 == -1:
        print("The number is not in the base input.")
        return
    
    decimal = to_decimal.base_to_dec(num_1, b1)
    num_2 = from_decimal.dec_to_base(decimal, b2)
    out = list_to_string(num_2)
    
    print("\n" + "The number in final base is: " + out + "\n")
    return

y = "c"
while(y == "c"):
    convert()
    y1 = input("Press C to continue or Press Q to quit: ")
    y = y1[0].lower()
