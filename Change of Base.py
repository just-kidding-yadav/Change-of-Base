# Converting from one base to other

import from_decimal
import to_decimal

def convert():
    num1 = int(input("\n" + "Enter the number whose base is to be changed: "))
    b1 = int(input("Enter the base of the number: "))
    b2 = int(input("Enter the base of the final result: "))

    for i in range(len(str(num1))):
        if(int(str(num1)[i]) >= b1):
            print("\n"+  "The number is not in entered base" + "\n")
            convert()

    decimal = to_decimal.base_to_dec(num1, b1)
    num2 = from_decimal.dec_to_base(decimal, b2)

    print("\n" + "The number in final base is: " + str(num2) + "\n")

    return

def quit():
    pass

y = "c"
while(y == "c"):
    convert()
    y1 = input("Press C to continue or Press Q to quit: ")
    y = y1.lower()

quit()
