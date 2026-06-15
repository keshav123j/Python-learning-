#Program to find out in which line Python is present in log.txt
with open("log.txt") as f:
    lines = f.readlines()

#F.readlines this gives us lines which include lines from .readline and it is iterable 
#Lines is iterable by each line , we could also have used i  instead of line
for line in lines:
    lineno = 1
    if("Python" in line):
        print(f"Python is in line number {lineno}" )
        break
    else:
        lineno = lineno+1#Same i got confused and in this else put that no python text here
        #But actually it is the one that if it runs for 1st line and no Python than it updates lineno by 1 
else:
    print("There is no Python")  
