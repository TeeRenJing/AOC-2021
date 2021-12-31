
f = open("input3.txt", "r")
inputarray = []


for line in f:
    inputarray.append(line)

#inputarray = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
container = []

for i in range(0,12):
    countzero = 0
    countone = 0
    for bnum in inputarray:
        if bnum[i] == "0":
            countzero+=1
        if bnum[i] == "1":
            countone+=1
    print(countzero)
    print(countone)
    if countzero>countone:
        for bnum in inputarray:
            if bnum[i] == "1":
                container.append(bnum)

    if countone>countzero:
        for bnum in inputarray:
            if bnum[i] == "0":
                container.append(bnum)

    if countone==countzero:
        for bnum in inputarray:
            if bnum[i] == "0":
                container.append(bnum)

    print (inputarray)
    print (container)
    inputarray = container
    container = []
    print (inputarray)
    print (container)


