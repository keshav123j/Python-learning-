#That is something happens when some condition met
#if(condition):
  #print("hello")
#elif(condition2 ):
#do this
#else : when no condition true
 #DO this that

#Like program which checks if user is above 18
a = input("Enter your age :")
if(int(a)>=18):
    print("You can enter")
elif(int(a)<0):
    print("You are yet an sperm - not allowed")
else:
    print("Not allowed")

#Important note: What python does is step wise and stop
#1)Check if condition is true if true execute the inside and stop there - not check elif
#2)check elif condition only if was not true , if its true than execute
#if none than else

#Where both if and elif are true - it only execute if 
if(int(a)>=18):
    print("You can enter")
elif(int(a)>=18):
    print("You are maybe not yet even an sperm - not allowed")
else:
    print("Not allowed")
#That is only prints "You can enter"

#Notice how ther autospace there - that is indentation -
#   INdentation is proper spacing if inside a fxn or some condition so 
#You gotta leave an space else not

