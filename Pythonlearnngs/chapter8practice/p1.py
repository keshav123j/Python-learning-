#To make an fucntion which finds greatest of 3 numbers
def great(a,b,c):
    if(a>b and a>c):
        print(f"a is greatest {a}")
    elif(b>a and b>c):
        print(f"b is greatest {b}")
    else:
        print(f"Either they are equal or {c} is greatest")
great(1,2,4)