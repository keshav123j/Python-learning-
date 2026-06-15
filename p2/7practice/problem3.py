#To generate table using while loop
i = int(input("Enter your number : "))
b = i
while(i<=10*b):
    print(b ,"*",i/b, "="," ",i)
    i = i +b

#This is an good one bcz here first we gotta secure the number into another
#Variable as i will keep changing so we gotta first make it to some value and keep changing that i
#Now keep adding that b

#Cleaner approach is to get an counter however so to avoid the float thing
counter = 1
b  = int(input("Enter your number"))
while(counter<=10):
    print(b," * ",counter , " = ",b*counter)

    counter = counter+1

#More cleaner way to print while both strings , variables there is to use f"" - formatted string literal
#Here write string normally and variables like{b}
counter = 1
b  = int(input("Enter your number"))
while(counter<=10):
    print(f"{b} * {counter} = {b*counter}")

    counter = counter+1