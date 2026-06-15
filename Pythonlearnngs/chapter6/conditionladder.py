#if elif else work as ladder , 
#if 1st condition met than it skips other , if none than goes to else
a = input("Enter your age :")
if(int(a)<=0):
    print("Sorry not born yet")
elif(int(a)>80):
    print("Hello grandpa")
elif(int(a)>30):
    print("Hello still young")
elif(int(a)>18):
    print("Hello getting young")
elif(int(a)>0):
    print("Congratulation you are born")

#Important note: The order matters - if i would have first put a>0 than 
#even for a = 45 , it would choose the newly born one as it will be first so it executes it
#From ai -It's called condition ordering or more specifically the guard clause concept. 
#The idea that in a ladder of conditions, more specific/restrictive conditions must come before broader ones.

#IN condition ordering the condition to be placed first is 
#condition 1 and condition 2 - condition 1 is true always when condition 2 is
#Like a>0 is always true if a>80
#So we have to first place condiition 2 so if condiition 2 true than it gets executed and condition 1 neglected
#If we place condition 1 first and originally condition 2 is true so condition 1 will be exceuted instead which we not want
#We want specific condition first and general later so it do not catch everything