#This is to read an file and convert Donkey into ######

with open("donkey.txt")as f:
    data = f.read()
if ("Donkey" in data or "donkey" in data):
    newdata = data.replace("Donkey","######")#This wont work as it will first make newdata equal to replacing
    newdata = data.replace("donkey","######")#Donkey with ###### , while data is same , and than newdata is assigned to data where donkey is changed to ###### 
    #That is kinda newdata is assigned to 1st data changed (Donkey - ######) and than donkey to #####
    #The one which is finally is kept , instead we have to do like this
    new = data.replace("Donkey", "#"*len("Donkey"))

    with open("donkey.txt","w") as f:
        f.write(new)