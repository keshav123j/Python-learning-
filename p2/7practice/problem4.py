#To check whether an given number is prime
#Just an bit of optimization is instead of checking till the number a itself
#We can can only till root(a) and also coniditon to remove 1
#also to put outside the loop as it check a = 1 range(2,1)hence none so goes to else and says its prime
a = int(input("Enter number to be checked prime : "))
if(a<2):
    print("Number is not prime")
else:
    for i in range(2,int(a**0.5)+1):
      if(a%i)==0:
        print("Number is not prime")
        break
    else:
        print("Number is prime")