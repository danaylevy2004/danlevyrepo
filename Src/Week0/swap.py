def num(num1,num2):
    print(num1, num2) # pre-swap
    num1, num2 = num1, num2
    return num1, num2

def swap():
    num1 = int(input("Select a number for the first number:"))
    num2 = int(input("select a number for the second number:"))
    x,y=num(num1,num2)
    print(x,y)