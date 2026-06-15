#Using while loop and readline to get readlines 
f = open("filemultipleline.txt")
line = f.readline()
while(line!=""):
    print(line)
    line = f.readline()
#That is it first puts line to first line of it , prints it , than makes it equal to 2nd line
#Than prints it , than again until the last line it like when line gets to 3rd line(last line)
#It prints it and than finds the next line by f.readline that is empty and hence the loop stopped
#That is at last line - prints it first than makes it empty than hence loop stops 
#That is first gets to first line than prints it than makes it to next line than prints it and prints until the line gets empty