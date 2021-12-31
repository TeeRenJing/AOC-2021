f = open("input9.txt", "r")
inputarray = [line[:-1] for line in f]


lowpoints = []
def findlowpointsfirstrow(inputarray, lowpoints):
    for i in range(1,len(inputarray[0])-1):
        if int(inputarray[0][i]) < int(inputarray[0][i+1]) and int(inputarray[0][i]) < int(inputarray[0][i-1]) and int(inputarray[0][i]) < int(inputarray[1][i]):
            lowpoints.append(int(inputarray[0][i]))



def findlowpointslastrow(inputarray, lowpoints):
    for i in range(1,len(inputarray[len(inputarray)-1])-1):
        if int(inputarray[len(inputarray)-1][i]) < int(inputarray[len(inputarray)-1][i+1]) and int(inputarray[len(inputarray)-1][i]) < int(inputarray[len(inputarray)-1][i-1]) and int(inputarray[len(inputarray)-1][i]) < int(inputarray[len(inputarray)-2][i]):
            lowpoints.append(int(inputarray[len(inputarray)-1][i]))

   

def findandappendlowpointsmiddle (inputarray, lowpoints):
    for i in range(1,len(inputarray)-1):
        for j in range(0,len(inputarray[i])):
            if j == 0:
                if int(inputarray[i][j]) < int(inputarray[i][j+1]) and int(inputarray[i][j]) < int(inputarray[i-1][j]) and int(inputarray[i][j]) < int(inputarray[i+1][j]):
                    lowpoints.append(int(inputarray[i][j]))
                    
            elif j == len(inputarray[i]) - 1:
                if int(inputarray[i][j]) < int(inputarray[i][j-1]) and int(inputarray[i][j]) < int(inputarray[i-1][j]) and int(inputarray[i][j]) < int(inputarray[i+1][j]):
                    lowpoints.append(int(inputarray[i][j]))
                    
            else:
                if int(inputarray[i][j]) < int(inputarray[i][j-1]) and int(inputarray[i][j]) < int(inputarray[i-1][j]) and int(inputarray[i][j]) < int(inputarray[i+1][j]) and int(inputarray[i][j]) < int(inputarray[i][j+1]):
                    lowpoints.append(int(inputarray[i][j]))
                    



testarr = '99999 49995 99999 49995 99999'.split(' ')
print(testarr)
findlowpointsfirstrow(inputarray,lowpoints)
findandappendlowpointsmiddle(inputarray,lowpoints)
findlowpointslastrow(inputarray, lowpoints)
print(lowpoints)

sum = 0
for num in lowpoints:
    sum = sum + num + 1

print(sum)



