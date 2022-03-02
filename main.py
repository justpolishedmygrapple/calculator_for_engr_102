def validate_num():
    num = input("number: ")
    try:
        float(num)
        if not float(num):
            return validate_num()
        else:
            num = float(num)
            return num
    except ValueError:
        print("Enter a valid number you silly gööse")
        return validate_num()
def validate_opcode():
    opcode = input("Enter opcode fron 0-3: ")
    try:
        z = int(opcode)
        int(opcode)
        if not int(opcode):
            return validate_opcode()
        if z == 0 or z == 1 or z == 2 or z == 3:
            return int(opcode)
        else:
            print("enter a valid opcode you silly gööse")
            return validate_opcode()
    except ValueError:
        print("enter a valid opcode")
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
print("opcodes: 0 is addition, 1 is subtraction, 2 is multiplication, 3 is division\n")
would_you_like = "yes"
while would_you_like == "yes":
    first_num = validate_num()
    print("enter another number")
    second_num = validate_num()
    opcode = validate_opcode()
    if opcode == 0:
        print(first_num + second_num)
    if opcode == 1:
        print(first_num - second_num)
    if opcode == 2:
        print(first_num * second_num)
    if opcode == 3:
        print(first_num / second_num)
    would_you_like = validate_wyl()