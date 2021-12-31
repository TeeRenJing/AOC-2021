f = open("input8.txt", "r")
inputarray = [line[:-1] for line in f]



print(inputarray[0][61:].split(' '))

inputarray = [line[61:].split(' ') for line in inputarray]
print(inputarray)

def countrecognisables(arr):
    count = 0
    for str in arr:
        if len(str) == 2 or len(str) == 3 or len(str) == 4 or len(str) == 7:
            count += 1

    return count

testarr = ['gb', 'ceafg', 'bcega', 'gb']

print(countrecognisables(testarr))

count = 0
for arr in inputarray:
    count += countrecognisables(arr)

print(count)