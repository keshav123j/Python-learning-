a = ("Hello","Keshav",1,2,3)
print(a.count(1))

#Here it does not give the element with index = 3 but index of the element 3 in tuple
y = a.index(3)
print(y)
#That is what give element at index 3
print(a[3])

#Than there are concatination(+ karna), repetition(*karna), len(),
#Also we can if there is an element in tuple
b = a*3
print(b)

#TO check if elemnt there - element in tuple gives boolean
c = 2 in b
print(c)

#Get max ,min
#print(max(b)) #Here since there are string it gives an error

#Slicing- same way as in string - slicing gives an new tuple as in string we get an new string
#as these are immutable
print(b[0:6:2])

#Unpacking that is assing values
#Even putting b here do not give an error but i thought python reads forward or it makes a,b,c.. equal to ("Keshav..")
#That is we did not change the value of b earlier it was the tuple itself
#Now we put it equal to b unpacking so b now takes the value of unpacking the b i.e it gets assigned value
#Python do not read what b is and even whatever it is , it just unpacks that b and than assigns
#As x = y , so x is what gets assigned value y 
a , b ,c ,d,e,f,g,h,i,j,k,l,m,n,o= b
print(a,b,c)