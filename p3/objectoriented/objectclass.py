#An class is like an blueprint for an object , like an empty form 
#Object is when we fill up that form

#Its like say in game - you create an blueprint for rocks - that is class rock
#Now we can have parameters like radius,smoothness and filling those gives us an object

class Employee:
    name = "Keshav"
    age = 17
    Transforming  = True
#That is this class has attributes which  are assigned to an object
X = Employee()
X.length = "6ft" #We can also add special attribute to an single object or like this
#Name age Transforming are class attribute and length is object attribute
#Also if we use instance attribute like X.age = 25 ,so it will be preferred over clas atttribute
X.age = 25
print(X.age,X.name,X.length)

#We can also change attribute of an class
Employee.age = 18
Y = Employee()
print(Y.age)