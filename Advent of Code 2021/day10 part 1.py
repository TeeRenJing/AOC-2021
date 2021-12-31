from os import terminal_size
import numpy as np

f = open("input10.txt", "r")
inputarray = [line[:-1] for line in f]

print(inputarray)



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

illegalarr = []
for str in inputarray:
    illegalarr.append(returnillegal(str))

count = 0
for illegal in illegalarr:
    if illegal == ')':
        count += 3
    elif illegal == ']':
        count += 57
    elif illegal == '}':
        count += 1197
    elif illegal == '>':
        count += 25137


print (count)