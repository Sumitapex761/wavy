# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
ch=int(input("choose your choice 1.addition 2.subtraction 3.multiplication 4.division 5.mudulos"))
match ch:
    case 1:
        print(num1+num2)
    case 2:
        print(num1-num2)
    case 3:
        print(num1*num2)
    case 4:
        print(num1//num2)
    case 5:
        print(num1%num2)
    case default:
        print("incorrect choice")