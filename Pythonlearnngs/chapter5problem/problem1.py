wordmeaning = {
    "Madad":"Help",
    "Khana":"Food",
    "Soona":"Sleep"
}
userinput = input("Enter hindi to get english")
#print(wordmeaning[userinput])#This will give error if not in the dict
print(wordmeaning.get(userinput))