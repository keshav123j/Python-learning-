f = open("poem.txt")
data = f.read()
if("Twinkle" or "twinkle" in data):
    print("Always prints it")
#This code always gives bcz like if("string"or condition2) - this is how it treats it 
# #Any non empty string is truthy 
#To make this to check if either twinkle or Twinkle is there
if("Twinkle"in data or "twinkle" in data):
    print("Either twinkle or Twinkle is in poem")