from os import terminal_size
import numpy as np

f = open("input10.txt", "r")
inputarray = [line[:-1] for line in f]

print(len(inputarray))

def returnillegal(str):
    stack = []
    for char in str:
        if char == '(' or char == '{' or char == '<' or char == '[':
            stack.append(char)
        elif stack[-1] == '(' and char != ')':
            return char
        elif stack[-1] == '{' and char != '}':
            return char
        elif stack[-1] == '<' and char != '>':
            return char
        elif stack[-1] == '[' and char != ']':
            return char
        else:
            stack.pop()

def returntrueifillegal(str):
    stack = []
    for char in str:
        if char == '(' or char == '{' or char == '<' or char == '[':
            stack.append(char)
        elif stack[-1] == '(' and char != ')':
            return True
        elif stack[-1] == '{' and char != '}':
            return True
        elif stack[-1] == '<' and char != '>':
            return True
        elif stack[-1] == '[' and char != ']':
            return True
        else:
            stack.pop()

inputarray = [str for str in inputarray if returntrueifillegal(str) != True ]

print(len(inputarray))


def findendstr(str):
    stack = []
    endstr = []
    for char in str:
        if char == '(' or char == '{' or char == '<' or char == '[':
            stack.append(char)
        elif stack[-1] == '(' and char != ')':
            return char
        elif stack[-1] == '{' and char != '}':
            return char
        elif stack[-1] == '<' and char != '>':
            return char
        elif stack[-1] == '[' and char != ']':
            return char
        else:
            stack.pop()

    for opening in reversed(stack):
        if opening == '(':
            endstr.append(')')
        elif opening == '{':
            endstr.append('}')
        elif opening == '<':
            endstr.append('>')
        elif opening == '[':
            endstr.append(']')
    return endstr

print(np.matrix(inputarray))
print(type(inputarray[0]))
print('/n')
listofendstr = []

for str in inputarray:
    print(str)
    listofendstr.append(findendstr(str))

print(listofendstr)

def findtotalscores(list):
    score = 0
    for closingstr in list:
        score *= 5
        if closingstr == ")":
            score += 1
        elif closingstr == "]":
            score += 2
        elif closingstr == "}":
            score += 3
        elif closingstr == ">":
            score += 4
    return score

scorelist = []       
for list in listofendstr:
    scorelist.append(findtotalscores(list))

scorelist = sorted(scorelist)
#minus 1 because the first element is index 0
middleIndex = int((len(scorelist) - 1)/2)

print (scorelist[middleIndex])





# illegalarr = []
# for str in inputarray:
#     illegalarr.append(returnillegal(str))

# count = 0
# for illegal in illegalarr:
#     if illegal == ')':
#         count += 3
#     elif illegal == ']':
#         count += 57
#     elif illegal == '}':
#         count += 1197
#     elif illegal == '>':
#         count += 25137


# print (count)