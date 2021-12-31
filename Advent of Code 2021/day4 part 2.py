# Write your code here :-)
f = open("input4.txt", "r")
inputarray = [line[:-1] for line in f]

numbpickedarr = inputarray[0].split(',')

inputarray.pop(0)

sets = []
for i in range(1,len(inputarray),6):
    sets += [inputarray[i:i+5]]

def replaceblank(arr):
    arr = [x for x in arr if x != '']
    print(arr)
    return arr

for arr in sets:
    for i in range(0,len(arr)):
        arr[i] = arr[i].split(' ')

for bigarr in sets:
    for i in range(0,len(bigarr)):
        bigarr[i] = replaceblank(bigarr[i])



def checkifhsuccess(arr):
    for row in arr:
        if row == ['#', '#', '#', '#', '#']:
            return True


def checkifvsuccess(arr):
    for i in range(0,5):
        count = 0
        for row in arr:
            if row[i] == '#':
                count += 1
            else:
                break

        if count == 5:
            return True


def replacecallednum(twodarr, changethisstr):
    for i in range(0,len(twodarr)):
        if changethisstr in twodarr[i]:
            twodarr[i] = ["#" if x==changethisstr else x for x in twodarr[i]]

def removebigarrfromsets(sets, storage, bigarr):
    sets.remove(bigarr)
    storage.append(bigarr)

storagearr = []

for num in numbpickedarr:
    record = num
    success = False
    i = 0
    while i < len(sets):
        print(len(sets))
        print(f'index is {i}')
        replacecallednum(sets[i], num)
        if checkifvsuccess(sets[i]) or checkifhsuccess(sets[i]):
            removebigarrfromsets(sets, storagearr, sets[i])
            print(f'removed a bigarr, index is {i}')
            i = i - 1
            print(f'removed a bigarr, index is {i}')
            if len(sets) == 0:
                print(sets)
                print(storagearr)
                print(record)
        i += 1
    if success == True:
        break
