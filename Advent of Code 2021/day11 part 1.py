from os import terminal_size
import numpy as np
import pprint
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

f = open("input11.txt", "r")
inputarray = [line[:-1] for line in f]
inputarray = [list(str) for str in inputarray]
inputdict = {}

testarray = "5483143223 2745854711 5264556173 6141336146 6357385478 4167524645 2176841721 6882881134 4846848554 5283751526".split(' ')
testarray = [list(str) for str in testarray]
testarray = [convertelementstoint(list) for list in testarray]
testdict = {}
for row in range(len(testarray)):
    for column in range(len(testarray[row])):
        testdict[(row,column)] = testarray[row][column]
pprint.pprint(changedicttomatrix(testdict))

# testarray = "6594 3856 6375 7252".split(' ')
# testarray = [list(str) for str in testarray]
# testarray = [convertelementstoint(list) for list in testarray]
# testdict = {}
# for row in range(len(testarray)):
#     for column in range(len(testarray[row])):
#         testdict[(row,column)] = testarray[row][column]
# pprint.pprint(changedicttomatrix(testdict))








# print(inputarray)


inputarray = [convertelementstoint(list) for list in inputarray]
# print(inputarray)
# print(np.matrix(inputarray))

for row in range(len(inputarray)):
    for column in range(len(inputarray[row])):
        inputdict[(row,column)] = inputarray[row][column]

print(len(inputdict))


def alladdone(matrix):
    for row in range(len(matrix)):
        matrix[row] = [num+1 for num in matrix[row]]
    return matrix

# inputarray = alladdone(inputarray)
# print(np.matrix(inputarray))

def checkifmorethannineinmatrix(matrix):
    for row in matrix:
        for num in row:
            if num > 9:
                return True
    
    return False


# def baozha(row,column):
    # inputarray[row][column] = 0
    # if column+1 >= len(inputarray[0]):
    #     if row-1<0:
    #         inputarray[row+1][column] += 1
    #         inputarray[row][column-1] += 1
    #         inputarray[row+1][column-1] += 1

    #     elif row+1>= len(inputarray):
    #         inputarray[row-1][column] += 1
    #         inputarray[row][column-1] += 1
    #         inputarray[row-1][column-1] += 1

    #     else:
    #         inputarray[row-1][column] += 1
    #         inputarray[row][column-1] += 1
    #         inputarray[row+1][column] += 1
    #         inputarray[row-1][column-1] += 1
    #         inputarray[row+1][column-1] += 1


    # elif column-1 <0:
    #     if row-1<0:
    #         inputarray[row+1][column] += 1
    #         inputarray[row][column+1] += 1
    #         inputarray[row+1][column+1] += 1
    #     elif row+1>= len(inputarray):
    #         inputarray[row-1][column] += 1
    #         inputarray[row][column+1] += 1
    #         inputarray[row-1][column+1] += 1
    #     else:
    #         inputarray[row-1][column] += 1
    #         inputarray[row][column+1] += 1
    #         inputarray[row+1][column] += 1
    #         inputarray[row-1][column+1] += 1
    #         inputarray[row+1][column+1] += 1

    # elif row-1 <0:
    #     inputarray[row+1][column] += 1 
    #     inputarray[row][column+1] += 1
    #     inputarray[row][column-1] += 1
    #     inputarray[row+1][column-1] += 1
    #     inputarray[row+1][column+1] += 1

    # elif row+1 >= len(inputarray):
    #     inputarray[row-1][column] += 1
    #     inputarray[row][column+1] += 1
    #     inputarray[row][column-1] += 1
    #     inputarray[row-1][column-1] += 1
    #     inputarray[row-1][column+1] += 1

    # else:

def explode(coord, inputdict):
    if (coord[0]-1,coord[1]) in inputdict:
        if inputdict[(coord[0]-1,coord[1])] != 0:
            inputdict[(coord[0]-1,coord[1])] += 1

    if (coord[0]-1,coord[1]-1) in inputdict:
        if inputdict[(coord[0]-1,coord[1]-1)] != 0:
            inputdict[(coord[0]-1,coord[1]-1)] += 1

    if (coord[0]-1,coord[1]+1) in inputdict:
        if inputdict[(coord[0]-1,coord[1]+1)] != 0:
            inputdict[(coord[0]-1,coord[1]+1)] += 1

    if (coord[0],coord[1]-1) in inputdict: 
        if inputdict[(coord[0],coord[1]-1)] != 0:
            inputdict[(coord[0],coord[1]-1)] += 1

    if (coord[0],coord[1]+1) in inputdict:
        if inputdict[(coord[0],coord[1]+1)] != 0:
            inputdict[(coord[0],coord[1]+1)] += 1

    if (coord[0]+1,coord[1]-1) in inputdict:
        if inputdict[(coord[0]+1,coord[1]-1)] != 0:
            inputdict[(coord[0]+1,coord[1]-1)] += 1

    if (coord[0]+1,coord[1]) in inputdict:
        if inputdict[(coord[0]+1,coord[1])] != 0:
            inputdict[(coord[0]+1,coord[1])] += 1

    if (coord[0]+1,coord[1]+1) in inputdict:
        if inputdict[(coord[0]+1,coord[1]+1)] != 0:
            inputdict[(coord[0]+1,coord[1]+1)] += 1

def check_value_exist(test_dict, value):
    do_exist = False
    for key, val in test_dict.items():
        if val > value:
            do_exist = True
    return do_exist


flashcount = 0

def onedaypassed(inputdict):
    count = 0
    for key in inputdict:
        inputdict[key] += 1
    # print(inputdict)
    # print(9 in inputdict.values())
    while check_value_exist(inputdict,9):
        for coord in inputdict:
            if inputdict[coord] > 9:
                # print(coord)
                inputdict[coord] = 0
                explode(coord,inputdict)
                # print(changedicttomatrix(inputdict))
                count += 1
    # print(f"{flashcount} gonna output this yo")
    return inputdict, count
    
print(flashcount)

for i in range(100):

    # print(changedicttomatrix(testdict))
    results = onedaypassed(inputdict)

    # print(changedicttomatrix(results[0]))

    flashcount += results[1]
    # flashcount += onedaypassed(testdict)[1]


print(flashcount)
# pprint.pprint(inputdict)