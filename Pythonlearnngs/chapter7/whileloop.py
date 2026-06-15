#While loop executes the code inside it until condition in it is true
#If condition written is always true and code inside is also not changing it so it runs infintely
#It is kinda if loop is a subpart of while where i+= 1

#Usually in while loop we in code put code to change the condition or that isvalue of i here
#Like first it checks if i<1001 and it is so than it print1 and than makes it 2, now code executed and since its
#a loop it goes back and than again checks than again executes code 1 time and when condition gets false than gets to next code
i = 1
while(i<100001):
    print(i)
    i += 1
    #or use i = i +1 i.e i gets assigned to i+1 and at first i = 1 so it gets assigned 2 and than 3 
    #its like first loop uses i = 1 to execute code than i gets changed and so

#It is same as upper code
#Checks - 
for i in range(1,1000):
    print(i)