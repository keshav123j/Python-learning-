#This is the program which checks whether 2 files are similar
with open("this.txt") as f:
    data = f.read()
with open("copyofthis.txt") as t:
    data2 = t.read()
if(data == data2):
    print("Yes the files are identical")
else:
    print("No they are not identical")