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

print (sets)
print(sets[0])
for bigarr in sets:
    for i in range(0,len(bigarr)):
        bigarr[i] = replaceblank(bigarr[i])

print (sets)

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



for num in numbpickedarr:
    record = num
    success = False
    for bigarr in sets:
        replacecallednum(bigarr, num)
        if checkifvsuccess(bigarr) or checkifhsuccess(bigarr):
            print(bigarr)
            print(record)
            success = True
            break
    if success == True:
        break


