import os
# so this is the path we need
path = "/"
# this gets the value in a variable
contents = os.listdir(path)
# this shows  it
for item in contents:
    print(item)