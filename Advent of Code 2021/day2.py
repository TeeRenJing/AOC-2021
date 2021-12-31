# Write your code here :-)
f = open("input2.txt", "r")
inputarray = []
dist = 0
depth = 0
aim = 0
for line in f:
    inputarray.append(line)
print(inputarray)
for element in inputarray:
    if "forward" in element:
        dist += int(element[-2])
        depth += aim * int(element[-2])
    if "down" in element:
        aim += int(element[-2])
    if "up" in element:
        aim -= int(element[-2])

print(dist)
print(depth)
print(dist * depth)
