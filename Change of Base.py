# Converting from one base to other

import from_decimal
import to_decimal

def convert():
    num1 = input("\n" + "Enter a positive number whose base is to be changed: ")
    b1 = int(input("Enter the base of the number: "))
    b2 = int(input("Enter the base of the final result: "))
    if(int(num1)<0):
        print("The number is negative. Please enter a positive number.")
        return
    else:
        for i in num1:
            if not(i.isdigit()) and int(i) >= b1:
                print("Incorrect Base or Number.")
                return
    
    decimal = to_decimal.base_to_dec(int(num1), b1)
    num2 = from_decimal.dec_to_base(decimal, b2)

    print("\n" + "The number in final base is: " + str(num2) + "\n")
    return

def quit():
    pass

print("Choose a base: 2-10.")

y = "c"
while(y == "c"):
    convert()
    y1 = input("Press C to continue or Press Q to quit: ")
    y = y1.lower()

quit()
