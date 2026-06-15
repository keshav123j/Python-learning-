#Sometimes we want to check something repeatedly like also vary an number in range -
#So an loop does that
#It first goes to i = 1 than executes inside , than i = 2 than again
for i in range(1,100000):
        print(i)
#Prints till 99999 
#We can also use spacing in loop ,if first is not given than it assumes 0
#What for actually is - for i in somedatatype:
# code - gets executed , i gets varies across all the entries inside the datatype
#usually for variable we use range fxn its not a by default part of for
#range(start,end,step_size)- end not included by default start is 0,skip size is 1
l  = [1,2,3,"Keshav"]
for i in l:
        print(i)

#Step -size
for i in range(0,100,4):
        print(i)
    
#conclusion:i varies its value over all the entries in datatype(iterates the datatype) given in for i in datatype and executes the code
#range is also an datatype gives result as range(start,end,step) - end not included
#ONly interable datatype can be used in for

#Else loop can be used with for - else can be used when executes when the loop gets exhausted
for i in "Keshav":
        print(i)
else:
        print("String has been iterated and loop done")

#Break in for 
for i in "Keshav":
        print(i)
        if i == "K":
                break
        #WE can also use ()
        if(i =="K"):
                break
#At first i becomes k than inside it break gets executed and exits the loop 
 
#Continue in for loop - skip this iteration and than continue
#That is it will skip when "K" iteration comes and wont execute the next code written
#Than moves on to next iteration without executing next code and than again checks
for i in "Keshav":
        if(i=="K"):
                continue #Skips this iteration that is code below this for the current iteration
        print(i)

#Null statement in python - that is if we want nothing in loop use pass
#This will print nothing but leaving empty gives error
for i in range(0,41):
        pass