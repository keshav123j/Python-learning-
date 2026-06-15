#Detect spam comments - if it contains buy now,click this
message = input("Enter your comment :")
a = "Click this"
b = "Buy now"

#  a in b checks if its there and returns boolean
if(a in message or b in message):
    print("Spam message detected")
#Also its case sensitive of Capital , gaps this that