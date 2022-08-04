file = open('turtle.in')
output = open('turtle.out','w')
read = file.readline().split()
row = int(read[0])
column = int(read[1])
print(row, column)
array = []
for i in range(row):
    array.append(list(map(int, file.readline().split())))
print(array)
for i in range(1,column):
    array[-1][i] = array[-1][i-1] + array[-1][i]
print(array)
arrayReversed = list(reversed(array))
print(arrayReversed)
for i in range(1,row):
    print(i)
    arrayReversed[i][0] = arrayReversed[i-1][0] + arrayReversed[i][0]
print(arrayReversed)
for i in range(1,row):
    for j in range(1,column):
        arrayReversed[i][j] = arrayReversed[i][j] + max(arrayReversed[i][j-1],arrayReversed[i-1][j])
print(arrayReversed)
print(arrayReversed[-1][-1])
answer = ''.join(str(arrayReversed[-1][-1]))
output.write(answer)
print(answer)