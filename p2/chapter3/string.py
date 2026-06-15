#Three type of string : 
x = 'hello'
y = "Hello"
z = ''' Hello'''
print(x==y)
print(y==z)
#This shows that strings are case-sensitive that is upper case also and also by gaps

#String slicing - that is using the index function
#We can find length of an string (using len)or we can find an element like if starting from first it go like 0 ,1,.. , if from last than -1,-2,...
print(len(x))
#That is we use variable[starting index (included): last index(not included)] - that is the ending 
#the ending string index i.e index 2 which was l will not be printed
#Start from 1 and end before 2
Slicedstring = x[1:2]
print(Slicedstring)
#That is start with 0 and end before 5 that is on 4 - that is full number
print(x[0:5])

#That is the empty is also an string 
print(z[0:1])

#To get an single index element
print(z[0])
#That is this is print(z[-6]) so gives first element
print(z[-len(z)])


#Note:String are immutable that is cannot be changed by function
#Even .replace create an new string , to change it we gotta change the assigned variable value itself
c = "Keshav"
c[3] = "x"
#Gives error bcz string is not assigment
#We cannot change the value "Keshav" to something but we can allocate
#something else value to c itself


#More clear picture is:
#That c = "Keshav" , now "Keshav" exist somewhere in memory as object
#Now we do c = "Keshav2" - its an brand new object , we did not change "Keshav"
#That is why doing c[3] = z give error