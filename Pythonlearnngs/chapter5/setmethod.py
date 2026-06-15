a = {1,2,3,"Keshav"}
#Add new elements
a.add(5)
print(a)
#print(a[1])-Throws error bcz sets dont have an order so no index
#You can remove/add elements but like not change 5 to 15 , but instead first remove 5 and add 15
#Length of set a
print(len(a))
#Remove 5
a.remove(5)
print(a)

#Pop - removes an random element and returns the element removed
x = a.pop()
print(x)
#Clear - clears the set
a.clear()
print(a)
#Union and interssecion - these are the basic things in set , returns new set however , do not update one
#Union - returns union of a set with the the given argument set
a.add(5)
print(a)
x = a.union({1,5,6})
print(x)
#Intersection - returns set of intersection of given argument set
print(x.intersection({5}))