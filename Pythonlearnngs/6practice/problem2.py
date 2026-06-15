#Tell whether student passed or not - 40% overall and 33% inn each
a = int(input("Enter marks of subject 1 :"))
b= int(input("Enter marks of subject 2 :"))
c = int(input("Enter marks of subject 3 :"))

if(a>33 and b >33 and c>33 and a+b+c>120):
    print("You passed")
else:
    print("Failed,dont worry try again")