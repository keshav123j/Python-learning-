with open("table.txt","a") as f:
    a = int(input("Enter number of table :"))
    for i in range(1,11):
        f.write(str(a*i)+" " )
#This program - with ... as f in write mode first creates this file if it is not there
#Than we are running an loop to append the multiples
#NOte : We must use string in .write