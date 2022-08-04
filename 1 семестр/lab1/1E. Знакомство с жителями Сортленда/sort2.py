file = open('sortland.in')
output = open('sortland.out','w')
number = int(file.readline())
id = list(map(float,file.readline().split()))
array = id.copy()
for i in range(number):
    key = array[i]
    j = i - 1
    while j >= 0 and key < array[j]:
        array[j + 1] = array[j]
        j = j - 1
    array[j + 1] = key
answer = [id.index(array[0])+1,id.index(array[(number-1)//2])+1, id.index(array[number-1])+1]
string = ' '.join(map(str,answer))
output.write(string)
