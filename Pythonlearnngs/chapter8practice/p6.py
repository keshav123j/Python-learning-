#This is to make an star pattern
def pattern(n):
    if(n==0):
        return#This return means ki bas ab hogya ab aage nahi aana - jao
    print("*"*n)
    return(pattern(n-1))#Doing this so that it comes back to say we put for 5,so it comes for 4 than 3
pattern(5)