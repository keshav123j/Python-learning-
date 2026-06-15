#Tuple is immutable - kinda list which is immutable
a = (1,"xaz",6,7,9)
print(type(a))

#If we make like this than it considers whatever is inside and shows it string/int instead tuple
b = ("xaz")
print(type(b))
#To make it show tuple use ,
c = ("xaz",)
print(type(c))