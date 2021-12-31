from os import terminal_size
import numpy as np
import pprint
import time

def convertelementstoint(list):
    return [int(str) for str in list]
def changedicttomatrix(dict):
    # Convert Coordinate Dictionary to Matrix
    # Using loop + max() + list comprehension
    temp_x = max([cord[0] for cord in testdict.keys()])
    temp_y = max([cord[1] for cord in testdict.keys()])
    res = [[0] * (temp_y + 1) for ele in range(temp_x + 1)]
    
    for (i, j), val in testdict.items():
        res[i][j] = val

    return np.matrix(res)
  
    # # printing result 
    # print("The dictionary after creation of Matrix : " + str(res)) 

    # print(np.matrix(res))

f = open("input13.txt", "r")
inputarray = [line[:-1] for line in f]
inputarray = [str.split(',') for str in inputarray]
inputdict = {}

inputarray = inputarray[:len(inputarray)-13]
print(inputarray)
for list in inputarray:
    list[0] = int(list[0])
    list[1] = int(list[1])
    coord = tuple(list)
    inputdict[coord] = '#'

print(inputdict)
print(len(inputdict))

def foldxaxis(inputdict,num):
    for coord in inputdict.copy():
        if coord[0] < num:
            continue
        else:
            disttoline = coord[0] - num
            newxcoord = num - disttoline
            if (newxcoord,coord[1]) in inputdict:
                inputdict.pop(coord)
                continue
            else: 
                inputdict[(newxcoord,coord[1])] = '#'
                inputdict.pop(coord)

def foldyaxis(inputdict,num):
    for coord in inputdict.copy():
        if coord[1] < num:
            continue
        else:
            disttoline = coord[1] - num
            newycoord = num - disttoline
            if (coord[0],newycoord) in inputdict:
                inputdict.pop(coord)
                continue
            else: 
                inputdict[(coord[0],newycoord)] = '#'
                inputdict.pop(coord)

foldxaxis(inputdict,655)



            
            

print(len(inputdict))
