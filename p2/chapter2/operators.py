#arithmetic operators + - * /
a = 5 
b = 6
#  = is also assigment operator that is assign the value 
c = a*b
print(a*b)

#assignment operator 
b +=3
#that means to increament the value of b by 3 and than assign its value i.e now b equal 9 but c is still 30 
#bcz we did this thing after that 
print(b)
b -=9
#THat is decrease value by 9 and assign it now it is o
print(b)

# comparison operator :==,>,>=,<,!= i.e these values give like true or false about == if they are equal ,!= stands for not equal
#since b is not equal to a hence c is false 
c = b==a
print(c)

# now since b!=a is true we can assign it 
c = b!=a 
print(c)
d = c
# now we made an new variable d equal to c however its boolean value so d==c is true hence it shall give true 
e = d==c
print(e)
print("hello",e)
# now here we showed string and boolean together or we can also like convert boolean into string and than show 
# but currently i dont know how to 
#print("hello"+string(e))
#Confusion : assignment ke liye = use and to check if equal and get true or flase we use ==


#Logical operators - or , and , not
# or - anyone of it is true so the statement is correct - true else false
#and - both true only than true , not - flips it 
f = e or c
print(f)
g = f and c 
print(g)
 
x = not(g)
print(x)