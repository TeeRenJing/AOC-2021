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

f = open("input12.txt", "r")
inputarray = [line[:-1] for line in f]
inputarray = [str.split('-') for str in inputarray]
inputdict = {}
# print(inputarray)

def changearraytodictgraph(inputarray,inputdict):
    for list in inputarray:
        if list[0] in inputdict:
            inputdict[list[0]].append(list[1])
        else:
            inputdict[list[0]] = [list[1]]
        if list[1] in inputdict:
            inputdict[list[1]].append(list[0])
        else:
            inputdict[list[1]] = [list[0]]

testarr = 'start-A start-b A-c A-b b-d A-end b-end'.split(' ')
testarr = [str.split('-') for str in testarr]
# print(testarr)
testdict = {}
changearraytodictgraph(testarr, testdict)
print(testdict)
changearraytodictgraph(inputarray, inputdict)


stack = ['start','start']
def findnumofroutes(inputdict,node,stack):
    print(f'looking at {node}')
    if node.islower() and stack[-2].islower() and len(inputdict[node]) == 1:
        print('dead end')
        return 0
    elif node == 'end':
        return 1
    # elif node.islower() and stack[-1].isupper() and len(inputdict[node]) == 1:
    #     return 1
    else:
        
        count = 0
        for ele in inputdict[node]:
            if ele.islower() and ele in stack:
                continue
            else:
                print (f"gonna func {ele} next")
                
                print(f'this is the stack now {stack}')
                print(f'this is the stack for the next one {stack + [ele]}')
                
                count += findnumofroutes(inputdict,ele,stack+[ele])
                print(f'count is {count} for {node}')
        return count

    
print(findnumofroutes(inputdict,'start',stack))
    


# print('to'.isupper())