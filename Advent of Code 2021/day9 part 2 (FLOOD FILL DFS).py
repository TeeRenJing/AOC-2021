from os import terminal_size
import numpy as np

f = open("input9.txt", "r")
inputarray = [line[:-1] for line in f]

#print(inputarray)

for i in range(len(inputarray)):
    inputarray[i] = list(inputarray[i])

print(np.matrix(inputarray) ) 

seen = set()

print(seen)


# for row in range(len(inputarray)):
#     for column in range(len(inputarray[row])):
#         if (row,column) in seen:
#             continue
#         else:
#             floodfill(inputarray,row,column)


def floodfill(inputarray, row, column, seen):
    # print(f"{row},{column}")
    # print(len(inputarray[0]))

    if (row,column) in seen or row<0 or row >= len(inputarray) or column<0 or column >= len(inputarray[0]):
        return
    elif inputarray[row][column] == '9':
        return
        # print(inputarray[row][column])
    else:
        seen.append((row,column))
        floodfill(inputarray,row+1, column, seen)
        floodfill(inputarray,row-1, column, seen)
        floodfill(inputarray,row, column+1 , seen)
        floodfill(inputarray,row, column-1 , seen)
        return
    


lowpoints = []
lowpointscoords = []
def findlowpointsfirstrow(inputarray, lowpoints, lowpointscoords):
    for i in range(1,len(inputarray[0])-1):
        if int(inputarray[0][i]) < int(inputarray[0][i+1]) and int(inputarray[0][i]) < int(inputarray[0][i-1]) and int(inputarray[0][i]) < int(inputarray[1][i]):
            lowpoints.append(int(inputarray[0][i]))
            lowpointscoords.append((0,1))



def findlowpointslastrow(inputarray, lowpoints, lowpointscoords):
    for i in range(1,len(inputarray[len(inputarray)-1])-1):
        if int(inputarray[len(inputarray)-1][i]) < int(inputarray[len(inputarray)-1][i+1]) and int(inputarray[len(inputarray)-1][i]) < int(inputarray[len(inputarray)-1][i-1]) and int(inputarray[len(inputarray)-1][i]) < int(inputarray[len(inputarray)-2][i]):
            lowpoints.append(int(inputarray[len(inputarray)-1][i]))
            lowpointscoords.append((len(inputarray)-1,i))

   

def findandappendlowpointsmiddle (inputarray, lowpoints, lowpointscoords):
    for i in range(1,len(inputarray)-1):
        for j in range(0,len(inputarray[i])):
            if j == 0:
                if int(inputarray[i][j]) < int(inputarray[i][j+1]) and int(inputarray[i][j]) < int(inputarray[i-1][j]) and int(inputarray[i][j]) < int(inputarray[i+1][j]):
                    lowpoints.append(int(inputarray[i][j]))
                    lowpointscoords.append((i,j))
                    
            elif j == len(inputarray[i]) - 1:
                if int(inputarray[i][j]) < int(inputarray[i][j-1]) and int(inputarray[i][j]) < int(inputarray[i-1][j]) and int(inputarray[i][j]) < int(inputarray[i+1][j]):
                    lowpoints.append(int(inputarray[i][j]))
                    lowpointscoords.append((i,j))
                  
            else:
                if int(inputarray[i][j]) < int(inputarray[i][j-1]) and int(inputarray[i][j]) < int(inputarray[i-1][j]) and int(inputarray[i][j]) < int(inputarray[i+1][j]) and int(inputarray[i][j]) < int(inputarray[i][j+1]):
                    lowpoints.append(int(inputarray[i][j]))
                    lowpointscoords.append((i,j))



testarr = '2199943210 3987894921 9856789892 8767896789 9899965678'.split(' ')
testarr = [list(line) for line in testarr]
# print(testarr)
findlowpointsfirstrow(inputarray, lowpoints, lowpointscoords)
findandappendlowpointsmiddle(inputarray, lowpoints, lowpointscoords)
findlowpointslastrow(inputarray, lowpoints, lowpointscoords)
print(len(lowpointscoords))


lowpointstest = []
lowpointscoordstest = []
findlowpointsfirstrow(testarr,lowpointstest, lowpointscoordstest)
findandappendlowpointsmiddle(testarr,lowpointstest, lowpointscoordstest)
findlowpointslastrow(testarr, lowpointstest, lowpointscoordstest)
# print(lowpointstest)
# print(lowpointscoordstest)

storelength = []
for coord in lowpointscoords:
    seen = []
    floodfill(inputarray, coord[0], coord[1], seen)
    storelength.append(len(seen))
    
print(len(storelength))
storelength = sorted(storelength, reverse=True)
print(storelength)
product = 1
for i in range(3):
    product *= storelength[i]
print(product)





sum = 0
for num in lowpoints:
    sum = sum + num + 1

# def returnbasinmiddle(inputarray,i,j):
#     basin = []
#     basin.append[i-1][j]









