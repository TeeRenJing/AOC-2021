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

def respawn(fish):
    fish[health] = 6

def givebirth(arr):
    arr.append(8)

arr = [1,2,3]
givebirth(arr)

def onedaypassed(inputarray):
    for i in range(len(inputarray)):

        if inputarray[i] == 0:
            givebirth(inputarray)
            inputarray[i] = 6
        else:
            inputarray[i] -= 1
    return inputarray

test = [3,4,3,1,2]

for i in range(0,80):
    onedaypassed(test)


print(len(test))
    
