from os import terminal_size
import numpy as np
import pprint
import time

def convertelementstoint(list):
    return [int(str) for str in list]
def changedicttomatrix(testdict):
    # Convert Coordinate Dictionary to Matrix
    # Using loop + max() + list comprehension
    temp_x = max([cord[0] for cord in testdict.keys()])
    temp_y = max([cord[1] for cord in testdict.keys()])
    res = [[' '] * (temp_y + 1) for ele in range(temp_x + 1)]
    
    for (i, j), val in testdict.items():
        res[i][j] = val

    return np.matrix(res)
  
    # # printing result 
    # print("The dictionary after creation of Matrix : " + str(res)) 

    # print(np.matrix(res))

f = open("input14.txt", "r")
inputarray = [line[:-1] for line in f]
inputarray = [str.split(' -> ') for str in inputarray]
inputdict = {}

print(inputarray)
temp = inputarray[2:]
# print('/n')
# print(temp)

for arr in temp:
    inputdict[arr[0]] = arr[1]

# print(inputdict)

strinquestion = inputarray[0][0]
# strinquestion = strinquestion[0:4]
# print(strinquestion)

def mutatestr1day(strinquestion):
    nextstrinqn = ''
    for i in range(0,len(strinquestion)-1):
        # print(strinquestion[i:i+2])
        addchar = inputdict[strinquestion[i:i+2]]
        nextstrinqn += strinquestion[i] + addchar
    nextstrinqn += strinquestion[-1]
    # print(nextstrinqn + ' AT THE END')
    strinquestion = nextstrinqn
    # print(strinquestion + ' AT THE VERY END')
    return strinquestion



# for j in range(40):
#     # print(strinquestion + ' AT THE START')
#     strinquestion = mutatestr1day(strinquestion)
#     # print(strinquestion + ' cmon its mutated')
    

# print(strinquestion)
# Program to find most frequent
# element in a list
# def mostandleastfrequent(List):
#     return max(set(List), key = List.count), min(set(List), key = List.count)

# print(mostandleastfrequent(strinquestion))

# print(  strinquestion.count(mostandleastfrequent(strinquestion)[0])   -     strinquestion.count(mostandleastfrequent(strinquestion)[1]) )


for key in inputdict.copy():
    inputdict[key] = [key[0] +  inputdict[key] ,  inputdict[key] + key[1]]

# print(inputdict)
# print('hihih')

dictinquestion = {}

for i in range(len(strinquestion)-1):
    if strinquestion[i:i+2] in dictinquestion:
        dictinquestion[strinquestion[i:i+2]] += 1
    else:
        dictinquestion[strinquestion[i:i+2]] = 1

print(dictinquestion)

def addandremove(dictinquestion:dict,inputdict:dict,key:str,num:int, store:dict):
    print(f'removing {num} of {key} adding {inputdict[key][0]} and {inputdict[key][1]}')
    if inputdict[key][0] in dictinquestion and inputdict[key][1] in dictinquestion:
        dictinquestion[inputdict[key][0]] += num
        dictinquestion[inputdict[key][1]] += num
        dictinquestion[key] -= num
    elif inputdict[key][0] in dictinquestion and inputdict[key][1] not in dictinquestion:
        dictinquestion[inputdict[key][0]] += num
        dictinquestion[inputdict[key][1]] = num
        dictinquestion[key] -= num
    elif inputdict[key][0] not in dictinquestion and inputdict[key][1] in dictinquestion:
        dictinquestion[inputdict[key][0]] = num
        dictinquestion[inputdict[key][1]] += num
        dictinquestion[key] -= num
    else:
        dictinquestion[inputdict[key][0]] = num
        dictinquestion[inputdict[key][1]] = num
        dictinquestion[key] -= num

def mutatedictoneday(dictinquestion,inputdict,store):
    for key in store:
        addandremove(dictinquestion,inputdict,key,store[key], store)

for i in range(40):
    print(f'before {dictinquestion}')
    store = dictinquestion.copy()
    mutatedictoneday(dictinquestion, inputdict, store)
    print(f"after{dictinquestion}")

print(dictinquestion)

countdict = {}

for strkey in dictinquestion:
    if strkey[0] in countdict:
        countdict[strkey[0]] += dictinquestion[strkey]
    else:
        countdict[strkey[0]] = dictinquestion[strkey]
    if strkey[1] in countdict:
        countdict[strkey[1]] += dictinquestion[strkey]
    else:
        countdict[strkey[1]] = dictinquestion[strkey]

for strkey in countdict.copy():
    if strkey == strinquestion[0] or strkey == strinquestion[-1]:
        countdict[strkey] = (countdict[strkey] + 1) / 2
    else:
        countdict[strkey] = (countdict[strkey]) / 2


print(countdict)
countarr = []

for key in countdict:
    countarr.append(countdict[key])

print(max(countarr) - min(countarr))