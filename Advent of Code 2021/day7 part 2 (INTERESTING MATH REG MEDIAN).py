from statistics import mean, median, mode, stdev

f = open("input7.txt", "r")
inputarray = [line[:-1] for line in f]
inputarray = inputarray[0].split(',')
inputarray = [int(i) for i in inputarray]

#print(len(inputarray))
#print(max(inputarray))
#print(min(inputarray))

#avg = sum(inputarray) / len(inputarray)
#print(avg)

def finddistgivenp1dist(num):
    count = 0
    for i in range(0,num+1):
        count+=i
    return count

print(finddistgivenp1dist(2))


def finddistsum(list, num):
    count = 0
    for hposition in list:
        count += finddistgivenp1dist(abs(hposition - num))
    return count

testlist = [16,1,2,0,4,2,7,1,2,14]
inputarray = sorted(inputarray)

for i in range(len(testlist)):
   print(finddistsum(testlist,i))

results = []

for i in range(1788):
    results.append(finddistsum(inputarray,i))

print(min(results))
#print(median(inputarray))

#print(finddistsum(inputarray,median(inputarray)))