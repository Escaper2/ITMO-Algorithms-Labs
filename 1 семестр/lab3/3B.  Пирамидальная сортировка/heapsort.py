file = open('sort.in')
output = open('sort.out','w')
number = file.readline()
array = list(map(int,file.readline().split()))
key = 0
def heapsort(array):
    for i in range(len(array),-1,-1):
        heap(array,len(array),i)
    for i in range(len(array)-1,0,-1):
        key = array[i]
        array[i] = array[0]
        array[0] = key
        heap(array,i,0)
def heap(array,l,i):
    m = i
    left = (2*i) + 1
    right = (2*i) + 2
    if left < l and array[left] > array[m]:
        m = left
    if right < l and array[right] > array[m]:
        m = right
    if m != i:
        key = array[i]
        array[i] = array[m]
        array[m] = key
        heap(array,l,m)
heapsort(array)
answer = ' '.join(list(map(str,array)))
output.write(answer)

