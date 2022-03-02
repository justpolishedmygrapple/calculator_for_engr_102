##Author:   Austin Mangel
##Github:   justpolishedmygrapple
##Date:     1 March 2022
##Descrip:  Calculator that takes two numbers, real or complex, from a user and performs mathematical operations
##          based off of the given operation code. Validates all three user inputs.


def validate_num():
    num = input("enter a real or complex number: ")
    try:
        float(num)
        if float(num):
            num = float(num)
            return num
    except ValueError:
        pass
    try:
        complex(num)
        if complex(num):
            num = complex(num)
            return num
    except ValueError:
        print("Enter a valid real or complex number you silly gööse")
        return validate_num()

def validate_opcode():
    opcode = input("Enter opcode from 1-5: ")
    try:
        z = int(opcode)
        int(opcode)
        if not int(opcode):
            print("enter a valid opcode you silly gööse")
            return validate_opcode()
        if z == 1 or z == 2 or z == 3 or z == 4 or z == 5:
            opcode = int(opcode)
            return opcode
    except ValueError:
        print("enter a valid opcode you silly gööse")
        return validate_opcode()
def validate_wyl():
    would_you_like = input("Would you like to use the calculator again: ")
    would_you_like = would_you_like.lower()
    if would_you_like == "yes":
        return would_you_like
    elif would_you_like == "no":
        print("thanks for using the calculator")
    else:
        print("enter yes or no you silly gööse")
        return validate_wyl()
print("opcodes: 1 is addition, 2 is subtraction, 3 is multiplication, 4 is division, 5 is exponentiation\n")
would_you_like = "yes"
while would_you_like == "yes":
    first_num = validate_num()
    print("enter another number")
    second_num = validate_num()
    opcode = validate_opcode()
    if opcode == 1:
        print(first_num + second_num)
    if opcode == 2:
        print(first_num - second_num)
    if opcode == 3:
        print(first_num * second_num)
    if opcode == 4:
        print(first_num / second_num)
    if opcode == 5:
        print(first_num ** second_num)
    would_you_like = validate_wyl()
