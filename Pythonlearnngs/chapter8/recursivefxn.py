#Some fxn are recursive - that is defined by themselves like factorial 
#Say you gotta make factorial fxn so u can do like this
def factorial(n):
    if(n==1 or n==0):
        return(1)
    else:
        return(n*factorial(n-1))
a = factorial(5)
print(a)
#That is it will say u enter n = 5 ,so it will return 5*factorial(4) 
#Hence goes back to factorial(4)and so on until it gets to 1 -
#That is giving factorial(1or0) = 1 was necessary without it 
#It would have ran endlessly

def factorial2(n):
    if(n==2):
        return(2)
    if(n==1 or n==0):
        return(1)
    else:
        return(n*factorial(n-1))
#Here when we enter 5 so it simply goes to 5 *factorial(4) than again factorial gets called for 4
#5*4*factorial(3) = 5*4*3*factorial(2) given 2