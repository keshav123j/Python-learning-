#To print multiplication table using recursive functions
# def mul(a):
#     print(a)  
#     return(a+mul(a))
# mul(5)
#Note:Since this just keep going to mul(a) and do not find the ultimate value- so throws error of recursion limit
#I have to also try with recursive function





def table(a):
    for i in range(1,11):
        print(a*i)
table(45637894)

