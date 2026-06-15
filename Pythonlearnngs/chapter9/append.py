#w - this write mode clears the file and than enter what we put only
#a - this is append mode which adds it to the end but still we use the write fxn

#This erases whatever is there and now only Haha will be there
f = open("file.txt","w")
f.write("Haha")
f.close()

#This will add another Haha there
f = open("file.txt","a")
f.write("Haha")
f.close()

#Note:In .write it must be an string 
#If no mode is mentioned in opening than default is rt - read in text