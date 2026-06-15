x = "Hello  we are checking  if there is   double    space"
print(x.replace("  "," "))
#So here i expect is Hello we are checking if there is  double  space
#So that is in between is - 3spaces first 3 spaces it will convert to 1 space
#And than it will skip both those and see if there are other 2 space next
#That is like 2 converted to one , forget what it was and see if next are 2 space
# so 3 converted to 2 and also 4 like between space