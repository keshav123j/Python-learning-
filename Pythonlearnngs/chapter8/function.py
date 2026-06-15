#Sometimes we want an piece of logic to stay and separate use it anywhere
#Like making program to count prime numbers till a number
#We can use a function which check prime and just use it in loop to not get messy
#Or whatever average can be an function , appending to an database can be function

#Syntax
# def functionname():
#     logic #This is function definition
#     print()
#     or whatever
# Than whenever we need we can simply call the function as
#functionname() and code inside it gets executed - said as function calling

#There are 2type function - user defined and premade
#Function with arguments 
# Some functions can take arguments which are given in paranthesis like
# fxn which finds whether a is prime so a is argument
 
def hello():
    print("Hello world")
#Now we can call the function - its without argument so we do not need one
hello()

def primecheck(a):
    prime = True
    for i in range(2,int(a**0.5+1)):
        if(a%i==0):
            prime  = False
    print(prime)

def primecheck2(a):
    for i in range(2,int(a**0.5+1)):
        if(a%i==0):
            print("Not prime")
            return(i)
            return(i+1)
            break
    else:
        print("Prime")
#Else - used not with same indent of if - as say it is checking for i = 3 than 4,5 so each time it print Not prime
#If we use else same indent of loop-first it checks the if conditions and if it gets met prints not prime and leaves
#If no if condition met than so no divisors hence its prime so does the else code execution
a = primecheck(6)
print(a)
#Since we put it equal to an variable and also called it so it also prints False
#However since nothing retuned here so its value is NONE - its not an error
b = primecheck2(6)
print(b)
#Same - it is called so it prints Not Prime 
#And we have returned the first divisor so it does return if - if its prime it also returns NONE
#Note: We can return anywhere inside function like inside loop/if whatever
#If we return 2 things than simply only first is taken 

#Returning an value in function- we can also return  an value in function
#If we assign a = fxn(parameter) and in fxn we have returned something so 
#a takes that value and fxn() gets executed also

#Default parameter 
def greet(name = "Keshav"):
    print(f"Hello {name}")
greet() #Default chosses name as Keshav
greet("Anadi")#Now switches name to Anadi