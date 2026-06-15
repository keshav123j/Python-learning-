#Dictionary can be used to map 2 object and store multiple such mapped pairs
#It contain pairs of key-value like this
#Key can also be anydata type but if assigning like some x , then first define it 
x = True
a = { "Hello":1,"Keshav":5,x:56,0: 56,True: 60}
#a[key] = this gives the value
print(a["Hello"])
print(a[x])
print(a[True])

#Properties - unordered - no order
#Mutable - that is can be changed originally
#INdexed - that is with key indexed and no duplicate(same) key 
c = {}#to create empty dictionary