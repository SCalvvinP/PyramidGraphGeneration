#author: Scalvvin
import numpy as np
num = 3123623623632362343254212123126236236323153212421812
res = list(map(int, str(num)))
successiveSum =  list(map(int, str(num)))
sum = 0
oSum = 0
for count, item in enumerate(res):
    oSum = oSum + item
    if count % 2 == 0 : 
        sum = sum + item
        successiveSum[count] = sum
    elif count % 2 == 1 : 
        sum = sum  - item
        successiveSum[count] = sum

maxValue = max(successiveSum)
indexOfMaxValue = successiveSum.index(maxValue)
matrix = []
new = []
for i in range (0, maxValue + 10):
    for j in range (0, oSum + 10):
        new.append(' ')
    matrix.append(new)
    new = []

x = 0
y = maxValue + 3 - 1
print(maxValue)
print(oSum)
for count, item in enumerate(res):
    if count == (indexOfMaxValue + 1) :
        print(y)
        print(x)
        tempy = y
        tempx = x
        y = y-1
        x= x-1
        matrix[y][x] = "<"
        x = x+2
        matrix[y][x] = ">"
        y = y-1
        x = tempx - 1
        matrix[y][x] = "/"
        x = x+1
        matrix[y][x] = "|"
        x = x+1
        matrix[y][x] = "\\"
        y = y-1
        x = tempx
        matrix[y][x] = "o"
        y = tempy
        x = tempx + 1

    if count % 2 == 0 :
        for val in range (0, item):
            matrix[y][x] = "/"
            x += 1
            y = y-1
        y = y+1    
    elif count % 2 == 1 :
        for val in range (0, item):
            matrix[y][x] = "\\"
            x +=1
            y = y+1
        y = y-1

# for r in matrix:
#     for c in r:
#         print(c,end = " ")
#     print()


np.savetxt('graph.txt', matrix,fmt='%s')