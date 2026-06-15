#We can also use multiple if
#Each if is indivial statement 

#That is first it checks the first if , than stops its complete than goes to next code
a = input("Enter number :")
#WE use == bcz = is assignment not comparative and here we need True/false
if(int(a)%2 == 0):
    print("Number is even ")
#Now its stop
if(int(a)%3 == 0):
    print("Number is multiple of 3")
else:
    print("Number is neither divisible by 2 nor by 3")
 
#Note:This code is wrong
#Bcz if we enter 4 - it shows Number is even ,Number is neither divisible by 2 nor by 3
#This is bcz in multiple if 
#It first finishes first if , its elif and else .than stop and than next
#So it first finished first if - in 4 so prints even , than next if not satisfies so print its else
#Since the else is of 2nd if only so - print shall  be not divisible by 3
