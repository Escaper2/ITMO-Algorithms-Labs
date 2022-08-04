file = open('check.in')
output = open('check.out','w')
n = int(file.readline())
if n == 0:
    output.write("YES")
    exit()
array = []
max = 10**9
min = -10**9
for i in range(n):
    array.append(list(map(int,file.readline().split())))
array[0].append(min)
array[0].append(max)
for i in range(n):
    if array[i][1] != 0:
        min = array[i][3]
        array[array[i][1]-1].append(min)
        max = array[i][0]
        array[array[i][1] - 1].append(max)
        if array[array[i][1]-1][0] > array[i][0]:
            output.write("NO")
            exit()
        if array[array[i][1]-1][0] == array[i][0]:
            output.write("NO")
            exit()
        if array[array[i][1]-1][0] <= array[i][3]:
            output.write("NO")
            exit()
        if array[array[i][1]-1][0] >= array[i][0]:
            output.write("NO")
            exit()
    if array[i][2] != 0:
        min = array[i][0]
        array[array[i][2]-1].append(min)
        max = array[i][4]
        array[array[i][2]-1].append(max)
        if array[array[i][2]-1][0] < array[i][0]:
            output.write("NO")
            exit()
        if array[array[i][2]-1][0] == array[i][0]:
            output.write("NO")
            exit()
        if array[array[i][2]-1][0] <= array[i][0]:
            output.write("NO")
            exit()
        if array[array[i][2]-1][0] >= array[i][4]:
            output.write("NO")
            exit()
output.write("YES")

