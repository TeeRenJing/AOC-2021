# Write your code here :-)
def replacecallednum(twodarr, changethisstr):
    for i in range(0,len(twodarr)):
        if changethisstr in twodarr[i]:
            twodarr[i] = ["#" if x==changethisstr else x for x in twodarr[i]]


a = [[1,2,3,4,5],[6,7,8,9,10]]
replacecallednum(a, 69)

def replaceblank(arr):
    arr = [x for x in arr if x != '']
    print(arr)
    return arr

b = ['6','7','8','','9','','3']
b = replaceblank(b)

def removebigarrfromsets(sets, storage, bigarr):
    sets.remove(bigarr)
    storage.append(bigarr)

c = [[[1],[2]],[[3],[4]]]
storagearr = []
print (c)
print (storagearr)
removebigarrfromsets(c,storagearr,[[1],[2]])
removebigarrfromsets(c,storagearr,[[3],[4]])
print(c)
print (storagearr)
