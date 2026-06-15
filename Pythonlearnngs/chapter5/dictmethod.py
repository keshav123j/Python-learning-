a = { "Hello":1,"Keshav":5,0: 56,True: 60}
#Get keys
print(a.keys())
#Get values
print(a.values())
#Update values - so if we pass some dictionary to update 
#And some key and value , so key which are there change their value and 
#New key added so it gets added
a.update({"Hello":5,"K":100})
print(a)

#Note :to get value of key we have 2 method .get and a[key]
#Difference: If key is not there - .get checks and than returns none but indexing give error
print(a.get("H"))
#print(a["H"])  - Thi gives error as .get specilally made to not give error
print(a)
#POP method - 1)remove key and value of the corresponding key
#2) Returns key and value
#3)If no such key than give default value entered if a.pop(key , 'default_value')used else error
print(a.pop("Keshav"))
print(a.pop("Ki",'5'))
print(a)
