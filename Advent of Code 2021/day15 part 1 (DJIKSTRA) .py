from os import terminal_size
import numpy as np
import pprint
import time
import math

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

f = open("input15.txt", "r")
inputarray = [line[:-1] for line in f]
inputarray = [list(str) for str in inputarray]
inputarray = [convertelementstoint(list) for list in inputarray]
inputdict = {}
for row in range(len(inputarray)):
    for column in range(len(inputarray[row])):
        # inputdict[(row,column)] = inputarray[row][column]
        inputdict[(row,column)] = dict(entercost = inputarray[row][column], lowestcost = math.inf)

print(len(inputdict))
inputdict[(0,0)]['lowestcost'] = 0
print(inputdict)

def relax_all_four_corners(coord:tuple,inputdict:dict):
    upcoord = (coord[0]-1,coord[1])
    downcoord = (coord[0]+1,coord[1])
    leftcoord = (coord[0],coord[1]-1)
    rightcoord = (coord[0],coord[1]+1)



    if upcoord in inputdict:
        if inputdict[coord]['lowestcost'] + inputdict[upcoord]['entercost'] < inputdict[upcoord]['lowestcost']:
            inputdict[upcoord]['lowestcost'] = inputdict[coord]['lowestcost'] + inputdict[upcoord]['entercost']

    if downcoord in inputdict: 
        if inputdict[coord]['lowestcost'] + inputdict[downcoord]['entercost'] < inputdict[downcoord]['lowestcost']:
            inputdict[downcoord]['lowestcost'] = inputdict[coord]['lowestcost'] + inputdict[downcoord]['entercost']

    if rightcoord in inputdict:
        if inputdict[coord]['lowestcost'] + inputdict[rightcoord]['entercost'] < inputdict[rightcoord]['lowestcost']:
            inputdict[rightcoord]['lowestcost'] = inputdict[coord]['lowestcost'] + inputdict[rightcoord]['entercost']

    if leftcoord in inputdict:
        if inputdict[coord]['lowestcost'] + inputdict[leftcoord]['entercost'] < inputdict[leftcoord]['lowestcost']:
            inputdict[leftcoord]['lowestcost'] = inputdict[coord]['lowestcost'] + inputdict[leftcoord]['entercost']

for coord in inputdict.copy():
    relax_all_four_corners(coord,inputdict)

print(inputdict[(99,99)])