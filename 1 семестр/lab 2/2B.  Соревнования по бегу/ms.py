file = open('race.in')
output = open('race.out','w')
num = int(file.readline())
arr = []
for i in range(num):
    arr.append(list(map(str, file.readline().split())))
def mergeList(a,b):
    supportList = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i][0] < b[j][0]:
            supportList.append(a[i])
            i = i + 1
        elif a[i][0] > b[j][0]:
            supportList.append(b[j])
            j = j + 1
        else:
            supportList.append(a[i])
            i = i + 1
    if i<len(a):
        supportList += a[i:]
    if j<len(b):
        supportList += b[j:]
    return supportList
def mergeSort(array):
    if len(array) == 1:
        return array
    mid = len(array)//2
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])
    return mergeList(left,right)

arr = mergeSort(arr)
i = 0
print(arr)
answer = ''
for i in arr:
    if i[0] != answer:
        output.write('=== ' + i[0] + ' ===\n')
        answer = i[0]
    output.write(i[1] + '\n')
        