c = [1,2,9,15,3,47,17]
#There are different fxn - these fxn does the things
#They do not give output of the result - but they make changes to c
#Only .pop fxn give the output of which element they delete
c.sort()#Will sort in increasing order
print(c)
c.reverse()#Will reverse all elements
print(c)
c.append(56)#add 56 at the end i.e app end- add at end
print(c)
c.insert(4,56)
print(c)
#Add 56 at index 4 - i.e index 4 will become 56 and next goes
print(c.pop(2))#Deletes element at index 2 and also gives output at index 2
print(c)
c.remove(56)#Will delete 56 from the list
print(c)
print(c.count(56))