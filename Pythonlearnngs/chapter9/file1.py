#When an program is executed - its datatypes likes variables etc got stored in random access memory
#Ram is volatile - so once its finished execution - no data there 
#So we have to usse file/io if we want to store it 

#Also if we want to read an file - we do  like this
#We first open it , than read it and than close the same opening variable
f = open("file.txt")
d = f.read()
print(d)
f.close()

#If we want to extract data than we can make new file and make it write mode
#Running this creates an file
f = open("filemade.txt","w")
f.write("HELLO")
f.close()

#When reading an file of multiple lines
f = open("filemultipleline.txt")

#f.readline() gives the first lines which is not read till now
#f.readlines() gives all lines with each line remaining that is not read - datatype list
line1 = f.readline()
print(line1,type(line1))
line2 = f.readline()
print(line2,type(line2))
line3 = f.readline()
print(line3,type(line3))

#Now line1 will read 1st line as its not read yet , than line 2 will line2 bcz line 1 is read
#Now if we do readlines - and since there is no line now not yet read - it will give us []
#Readlines give empty list , readline give empty string
#That is empty string
line = f.readlines()
print(line,line=="")
f.close()

#if there would have been 5 lines and we perform 3 readline than readlines would give next 2 lines