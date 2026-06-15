#This is an program to make an copy of an file "this.txt"
with open("this.txt") as f:
    data = f.read()
    with open("copyofthis.txt","w") as t:
        t.write(data)