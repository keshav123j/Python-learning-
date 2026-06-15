#Fool syntax of intax is x[intialindex:endingindex(not included):steps]
#So that is step of 2 means skip 1 in between - by default it is set to 1 , if we put -1 it go backward
x = "Keshav"
print(x[5:1:-2])
#That is it go from 5 - v to e while skipping 1 backwards so vh 
#Note - however 1 comes first normally but since its written in ending index - it will not that take this one