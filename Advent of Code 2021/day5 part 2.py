# Write your code here :-)
#read from text file and remove all /n
f = open("input5.txt", "r")
inputarray = [line[:-1] for line in f]

for i in range(0, len(inputarray)):
    inputarray[i] = inputarray[i].split(' -> ')


for i in range(0,len(inputarray)):
    arrone = inputarray[i]
    for j in range(0,len(arrone)):
        arrone[j] = arrone[j].split(',')
#all above steps are just to get to the format [['x1','y1'],['x2','y2']]



def checkhorizontalorvert(bigarr):
    return bigarr[0][0] == bigarr[1][0] or bigarr[0][1] == bigarr[1][1]

datadict = {}

def printallinbtwdiag(bigarr):
    outputarr = []
    x1 = int(bigarr[0][0])
    y1 = int(bigarr[0][1])
    x2 = int(bigarr[1][0])
    y2 = int(bigarr[1][1])
    if x1 < x2 and y1 < y2:
        for i in range(x1,x2 + 1):
                outputarr.append([i, y1])
                y1 += 1
        return outputarr
    if x1 > x2 and y1 > y2:
        for i in range(x2,x1 + 1):
                outputarr.append([i, y2])
                y2 += 1
        return outputarr

    if x1 < x2 and y1 > y2:
        for i in range(x1,x2 + 1):
                outputarr.append([i, y1])
                y1 -= 1
        return outputarr
    if x1 > x2 and y1 < y2:
        for i in range(x2,x1 + 1):
                outputarr.append([i, y2])
                y2 -= 1
        return outputarr

def printallinbtw(bigarr):
    outputarr = []
    if bigarr[0][0] == bigarr[1][0]:
        x1 = int(bigarr[0][0])
        y1 = int(bigarr[0][1])
        y2 = int(bigarr[1][1])
        if y1 > y2:
            for i in range(y2,y1 + 1):
                outputarr.append([x1, i])
        else:
            for i in range(y1,y2 + 1):
                outputarr.append([x1, i])
        return outputarr
    if bigarr[0][1] == bigarr[1][1]:
        y1 = int(bigarr[0][1])
        x1 = int(bigarr[0][0])
        x2 = int(bigarr[1][0])
        if x1 > x2:
            for i in range(x2,x1 + 1):
                outputarr.append([i, y1])
        else:
            for i in range(x1,x2 + 1):
                outputarr.append([i, y1])
        return outputarr

for bigarr in inputarray:
    if checkhorizontalorvert(bigarr):
        expanded = printallinbtw(bigarr)
        for coord in expanded:
            if tuple(coord) in datadict:
                datadict[tuple(coord)] += 1
            else:
                datadict[tuple(coord)] = 1
    else:
        expanded = printallinbtwdiag(bigarr)
        for coord in expanded:
            if tuple(coord) in datadict:
                datadict[tuple(coord)] += 1
            else:
                datadict[tuple(coord)] = 1

count = 0
for key in datadict:
    if datadict[key] >= 2:
        count += 1

print(count)


