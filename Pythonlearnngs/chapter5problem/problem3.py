#4 friends enter their favourite lanquage and those get added into it
#If 2 friends name are same as the update fxn if there is key and value there
# and we give same key with different value - it updates value keeping key same
a = "Keshav"
b = "Keshav"
c= "Avni"
d = "Akshit"
x = {}
a1 = input("Keshav enter your lanq ")
a2 = input("Anadi enter your lanq ")
a3 = input("Avni enter your lanq ")
a4 = input("Akshit enter your lanq ")
x.update({a:a1,b:a2,c:a3,d:a4})
print(x)