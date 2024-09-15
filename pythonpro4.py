import os
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b


def fun():
    hi = True
    inp = float(input("enter a number"))
    sy = {"+": add, "-": sub, "*": mul, "/": div}
    for i in sy:
        print(i)
    while hi:

        oper = input("enter operarion")
        num = int(input("enter next number"))
        f = sy[oper]
        u = f(inp, num)
        print(f"{inp}{oper}{num}={u}")
        sel = input("y to continue or n to new or x to exit")
        if sel == "y":
            inp = u
        elif sel=="n":
            hi = False
            fun()
            os.system("cls")

        elif sel=="x":
            hi = False
            print("bye")
fun()
