file = open('smallsort.in')
output = open('smallsort.out','w')
number = int(file.readline())
array = file.readline().split()
for i in range(len(array)):
    array[i] = int(array[i])
for i in range(1,number):
    key = array[i]
    j = i - 1
    while j >= 0 and key < array[j]:
        array[j+1] = array[j]
        j = j - 1
    array[j+1] = key
line = ' '.join(map(str,array))
output.write(line)