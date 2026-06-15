#We are using the f"" that is formatted string - we use like f"some variables and string "
#And also type(f"") is also string
#Always when we gotta use string but it also has to like has an variable than we use f"" 
#That is in the loop each time we gotta add new path for an table and it has the i variable
#This is called dynamic string

#Here we are creating an program which makes an folder and adds tables till numbers mentioned

def tablegen(a):
    table = ""
    for i in range(1,11):
        table+= f"{a} * {i} = {a*i}\n"#This \n will end the line and than new line starts
    return(table)#I was not returning table and hence in .write NOne was added so was giving error

    

a = int(input("Enter till what number u want the tables : "))
for i in range(1,a+1):
    with open(f"tables/tableof{i}.txt","w") as writer:
        writer.write(tablegen(i))

#NOte : I earlier tried this tables/table_n without the tables folder and it showed error
#That is we can create an file but not an directory / folder - it shall be there