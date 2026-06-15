#Close does is - it saves the changes , unlocks the file for other like os etc and frees up ram of our computer
#BUt we have an more modern way for this close

f = open("file.txt")
#Some other code or whatever
print(f.read())
f.close()

#Same as the default- method auto closes it when the code is done executing 
#Benefit:Even if code crashes it still closes the file
with open("file.txt") as f:
    #Give whatever code u wanna give within open f and f.close by the traditional method
    print(f.read())