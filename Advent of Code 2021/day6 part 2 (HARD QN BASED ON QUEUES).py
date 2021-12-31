f = open("input6.txt", "r")
inputarray = [line[:-1] for line in f]
inputarray = inputarray[0].split(',')
inputarray = [int(i) for i in inputarray]

fishgroup = {
    0:{
        'numoffishes' : 0
    },
    1:{
        'numoffishes' : 0
    },
    2:{
        'numoffishes' : 0
    },
    3:{
        'numoffishes' : 0
    },
    4:{
        'numoffishes' : 0
    },
    5:{
        'numoffishes' : 0
    },
    6:{
        'numoffishes' : 0
    },
}


def givebirth(arr):
    arr.append(8)



def onedaypassed(inputarray):
    for i in range(len(inputarray)):

        if inputarray[i] == 0:
            givebirth(inputarray)
            inputarray[i] = 6
        else:
            inputarray[i] -= 1
    return inputarray

#test = [3,4,3,1,2]

#for element in test:
    #fishgroup[element]['numoffishes'] += 1


#for day in range (1,2):
    
    #numoffishtoadd = fishgroup[(day-1)%6]['numoffishes']
    #fishgroup[(day + 1) % 7]['numoffishes'] += numoffishtoadd
    


    
def determineimpact(fish,days):
    workarr = [fish]
    for j in range(0,days):
        for i in range(0,len(workarr)):
            if workarr[i] == 0:
                workarr.append(8)
                workarr[i] = 6
            else:
                workarr[i] -= 1
    return len(workarr)

def determineimpactoutputarr(fish,days):
    workarr = [fish]
    for j in range(0,days):
        for i in range(0,len(workarr)):
            if workarr[i] == 0:
                workarr.append(8)
                workarr[i] = 6
            else:
                workarr[i] -= 1
    return workarr
referencearr = []
for i in range(0,9):
    print(determineimpact(i,128))
    referencearr.append(determineimpact(i,128))
print(referencearr)
for fish in inputarray:
    fishgroup[fish]['numoffishes'] += 1

print(fishgroup)

arr1 = determineimpactoutputarr(1,128)
print(len(arr1))
output = []
for i in range(0,9):
    output.append(arr1.count(i))
    
print(output)
arrofarr = []
for i in range (1,6):
    output = []
    for j in range(0,9):
        output.append(determineimpactoutputarr(i,128).count(j))
    print(output)
    arrofarr.append(output)

print(arrofarr)
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0


for i in range(0,9):
    count1 += arrofarr[0][i] * referencearr[i]

for i in range(0,9):
    count2 += arrofarr[1][i] * referencearr[i]

for i in range(0,9):
    count3 += arrofarr[2][i] * referencearr[i]

for i in range(0,9):
    count4 += arrofarr[3][i] * referencearr[i]

for i in range(0,9):
    count5 += arrofarr[4][i] * referencearr[i]


tot1 = 130 * count1
tot2 = 44 * count2
tot3 = 36 * count3
tot4 = 51 * count4
tot5 = 39 * count5

total = tot1 + tot2 + tot3 + tot4 + tot5

print(total)