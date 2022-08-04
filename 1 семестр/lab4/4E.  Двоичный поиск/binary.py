file = open('binsearch.in')
output = open('binsearch.out','w')
number = int(file.readline())
array = list(map(int,file.readline().split()))
count = file.readline()
request = list(map(int,file.readline().split()))
def low(array,request):
    left = 0
    right = number-1
    while right > left:
        middle = (left + right)//2
        if array[middle] < request:

            left = middle + 1
        else:
            right = middle

    if array[right] == request:
        return right + 1
    else:
        return -1

def up(array,request):
    left = 0
    right = number
    while right > left + 1:
        middle = (left + right)//2
        if array[middle] > request:

            right = middle
        else:
            left = middle
    if array[right-1] == request:
        return right
    else:
        return -1
answer = []
for i in request:
    output.write(str(low(array, i)) + ' ')
    output.write(str(up(array, i)))
    output.write('\n')