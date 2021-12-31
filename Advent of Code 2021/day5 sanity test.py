# Write your code here :-)
a = [['1', '1'], ['5', '5']]
b = [['1', '1'], ['1', '5']]
c = [['2', '1'], ['5', '1']]
d = [['1', '5'], ['5', '1']]
e = [['4', '1'], ['1', '4']]

inputarray = [a,b,c,d,e]

def checkhorizontalorvert(bigarr):
    return bigarr[0][0] == bigarr[1][0] or bigarr[0][1] == bigarr[1][1]

datadict = {}

def printallinbtwdiag(bigarr):
    outputarr = []
    if bigarr[0][0] < bigarr[1][0] and bigarr[0][1] < bigarr[1][1]:
        x1 = int(bigarr[0][0])
        y1 = int(bigarr[0][1])
        x2 = int(bigarr[1][0])
        y2 = int(bigarr[1][1])
        for i in range(x1,x2 + 1):
                outputarr.append([i, y1])
                y1 += 1
        return outputarr
    if bigarr[0][0] > bigarr[1][0] and bigarr[0][1] > bigarr[1][1]:
        x1 = int(bigarr[0][0])
        y1 = int(bigarr[0][1])
        x2 = int(bigarr[1][0])
        y2 = int(bigarr[1][1])
        for i in range(x2,x1 + 1):
                outputarr.append([i, y2])
                y2 += 1
        return outputarr

    if bigarr[0][0] < bigarr[1][0] and bigarr[0][1] > bigarr[1][1]:
        x1 = int(bigarr[0][0])
        y1 = int(bigarr[0][1])
        x2 = int(bigarr[1][0])
        y2 = int(bigarr[1][1])
        for i in range(x1,x2 + 1):
                outputarr.append([i, y1])
                y1 -= 1
        return outputarr
    if bigarr[0][0] > bigarr[1][0] and bigarr[0][1] < bigarr[1][1]:
        x1 = int(bigarr[0][0])
        y1 = int(bigarr[0][1])
        x2 = int(bigarr[1][0])
        y2 = int(bigarr[1][1])
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


print ( len(datadict) )
print (datadict)
count = 0
for key in datadict:
    if datadict[key] > 1:
        count += 1

print(count)
print (printallinbtwdiag(e))
