f = open("input8.txt", "r")
inputarray = [line[:-1] for line in f]


print(inputarray[0][61:].split(' '))

inputarray = [line.split(' | ') for line in inputarray]
print(inputarray)

def countrecognisables(arr):
    count = 0
    for str in arr:
        if len(str) == 2 or len(str) == 3 or len(str) == 4 or len(str) == 7:
            count += 1

    return count

#testarr = ['gb', 'ceafg', 'bcega', 'gb']

#print(countrecognisables(testarr))

count = 0
for arr in inputarray:
    count += countrecognisables(arr)

#print(count)

def returnoutputval(arr , config):
    outputstr = ''
    for str in arr:
        if sorted(str) == sorted(config[8]):
            outputstr = outputstr + '8'
        if sorted(str) == sorted(config[5]):
            outputstr = outputstr + '5'
        if sorted(str) == sorted(config[2]):
            outputstr = outputstr + '2'
        if sorted(str) == sorted(config[3]):
            outputstr = outputstr + '3'
        if sorted(str) == sorted(config[7]):
            outputstr = outputstr + '7'
        if sorted(str) == sorted(config[9]):
            outputstr = outputstr + '9'
        if sorted(str) == sorted(config[6]):
            outputstr = outputstr + '6'
        if sorted(str) == sorted(config[4]):
            outputstr = outputstr + '4' 
        if sorted(str) == sorted(config[0]):
            outputstr = outputstr + '0' 
        if sorted(str) == sorted(config[1]):
            outputstr = outputstr + '1' 
    return int(outputstr)

def returnsconfig(str):
    outputdict = {
        0:'',
        1:'',
        2:'',
        3:'',
        4:'',
        5:'',
        6:'',
        7:'',
        8:'',
        9:''
    }

    arr = str.split(' ')
    arr.sort(key=len)
    print (arr)
    outputdict[8] = arr[9]
    outputdict[1] = arr[0]
    outputdict[7] = arr[1]
    outputdict[4] = arr[2]

    arr.remove(outputdict[8])
    arr.remove(outputdict[1])
    arr.remove(outputdict[7])
    arr.remove(outputdict[4])

    # Use 7 identify 3
    for i in range(0, len(arr)):
        #str is arr[i]
        if all(item in sorted(arr[i]) for item in sorted(outputdict[7])) and len(arr[i]) == 5:
            outputdict[3] = arr[i]
            arr.remove(arr[i])
            break
    
    #Use 4 identify 9
    for i in range(0, len(arr)):
        if all(item in sorted(arr[i]) for item in sorted(outputdict[4])) and len(arr[i]) == 6:
            outputdict[9] = arr[i]
            arr.remove(arr[i])
            break

    #Use 7 identify 0          
    for i in range(0, len(arr)):
        if all(item in sorted(arr[i]) for item in sorted(outputdict[7])) and len(arr[i]) == 6:
            outputdict[0] = arr[i]
            arr.remove(arr[i])
            break        

    #Identify 6
    for str in arr:
        if len(str) == 6:
            outputdict[6] = str
            arr.remove(str)
            break
    
    #5 is in 9
    for i in range(0, len(arr)):
        if all(item in sorted(outputdict[9]) for item in sorted(arr[i])):
            outputdict[5] = arr[i]
            arr.remove(arr[i])
            break

    #last one is 2
    outputdict[2] = arr[0]            
    return outputdict

#teststr = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab'
#print(returnsconfig(teststr))

count = 0
for arr in inputarray:
    config = returnsconfig(arr[0]) 
    count += returnoutputval(arr[1].split(' '),config)

print(count)
