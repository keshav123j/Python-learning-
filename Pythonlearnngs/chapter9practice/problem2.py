#This is that game() function does is that we are given an highscore file which is either empty or has previous high score
#So we make have to make an function which if user breaks the high-score than updates it
#At start it is made custom to 1000
f = open("highscore.txt")
high = int(f.read())
a = int(input("Enter your score"))
print(f"{high} was your previous high score")
f.close()
if(a>=high):
    f = open("highscore.txt","w")
    f.write(str(a))
    f.close()
    print(f"Your new high score is {a}")
else:
    print("Your previous high score is higher")
    
#w - this mode erases whats inside and than writes what we say 
#Also we must write an string in the file - and if another write used same it does is first erase earlier and add what we gave only