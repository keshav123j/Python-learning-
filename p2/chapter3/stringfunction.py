#There are mutiple string functions
# 1)len(x) = gives length
# 2)x.endswith("av") - True if string ends with av else False
# 3)x.startswith("av") - True if string starts av else False
# 4)x.count("e") - Count how many times e is there
# 5)x.capatalize() - capitalize the first thing
# 6)x.find("x") - find when x came and returns the first occurance
# 7)x.replace("Hel","Kill") - Note: Makes a new string with replacement 
#Do not make changes but create a new string with changes - so u than gotta make changes 
#  and many more  like .lower , .upper , .replace

x="Hello keshav"
print(x.find("l"))

x = "Hello keshav"
x = x.replace("l","o")
#Strings are immutables that mean u cannot change them by running function
# on them but instead u can create another string and than use allocate operator
print(x)