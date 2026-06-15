#list are containers of different things which can be any datatype
c = ["Hello", "123", 123,25,25.5,True]
#Same indexing works here as in string but list can be changed however string not
c[-1] = "potato"
print(c[-1]) #List are mutable

#Indexing used the same way as in string
print(c[0:4])

# c[0:4] = 1
# print(c[0:4])
#Python show error

# Experiment 1 - replace 4 elements with 4 elements
c[0:4] = [1, 2, 3, 4]
print(c)

# Experiment 2 - replace 4 elements with 2 elements
c = ["Hello", "123", 123, 25, 25.5, True]  # reset
c[0:4] = [1, 2]
print(c)

# Experiment 3 - replace 4 elements with 6 elements
c = ["Hello", "123", 123, 25, 25.5, True]  # reset
c[0:4] = [1, 2, 3, 4, 5, 6]
print(c)

c = ["Hello", "123", 123, 25, 25.5, True]
c[0:2] = "Hi"
print(c)  # ['H', 'i', 123, 25, 25.5, True] ?

c = ["Hello", "123", 123, 25, 25.5, True]
c[0:2] = "H"
print(c)  # ['H', 'i', 123, 25, 25.5, True] ?

# The thing is that only literable can be allocated like string ,tuple,list,range objects,Dictionaries
#Literable are like "ab"+"cd" = "abcd" but 1+2=!12 , i.e things python can strip down element wise 12 cannot be in 1,2
#but "ab" can be in 'a' +'b'