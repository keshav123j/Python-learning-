x   = "Keshav"
print(x[-2:-5])
# So that is that going fromm back to first gives no result - as at default when step is not defined it first goes to -2 i.e a 
#, Than it tends to go forward by default to v but finds its not between those hence gives nothing

#This means if front left blank than its 0 , that is from start till 5-1 index
print(x[:5])

#If last left blank than its length , that is till last from start
print(x[0:])