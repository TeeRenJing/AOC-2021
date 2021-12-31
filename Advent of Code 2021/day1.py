# Write your code here :-)
f = open("input.txt", "r")
numarray = []
counter = 0
for line in f:
    numarray.append(int(line))
print(numarray)
for num in range(0,len(numarray)-3):
    firstsum=numarray[num]+numarray[num+1]+numarray[num+2]
    secondsum=numarray[num+3]+numarray[num+1]+numarray[num+2]
    if firstsum < secondsum:
        counter+=1

print(counter)
