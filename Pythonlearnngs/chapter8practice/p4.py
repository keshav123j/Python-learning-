#To write an recursive fxn to fin sum of first n natural numbers

def sum(a):
    if(a==1):
        return(1)
    return(a+sum(a-1))
print(sum(10))
#Defining for a==1 = 1is necessary so as the fxn comes down it at some point stops that is sum(10) = 10+sum(9)= 10+9+sum(8) , this stops at a==1