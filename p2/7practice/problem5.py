#Doing myself to count prime numbers till an given number
a = int(input("Enter number till checking prime : "))
counter = 0
for i in range(2,a+1):
    for b in range(2,int(i**0.5)+1):
        if(i%b==0):
            break
    else:
        counter = counter+1
print(counter)
#I was kinda doing doing mistake was putting this else inside the b loop
#But it is like when say for an i = 57 , the loop gets completed and if there is
#Some multiple than it breaks else if it do not find and 
#The loop gets completed so counter is added by 1 
#If we place inside for that is with if - say 57 now many are not multiple
#so each time it adds 1 to it