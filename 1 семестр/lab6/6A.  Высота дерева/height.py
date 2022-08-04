file = open('height.in')
output = open('height.out','w')
n = int(file.readline())
if n == 0:
    output.write(str(0))
    exit()
if n == 1:
    output.write(str(1))
    exit()
arr = [0] * n
arr[0] = 1
array = []
stringCount = 0
for i in range(n):
    array.append(list(map(int,file.readline().split())))
for i in range(n-1):
    stringCount = stringCount + 1
    if array[i][1] != 0:
        arr[array[i][1] - 1] = arr[stringCount-1] + 1
    if array[i][2] != 0:
        arr[array[i][2] - 1] = arr[stringCount - 1] + 1
answer = max(arr)
output.write(str(answer))