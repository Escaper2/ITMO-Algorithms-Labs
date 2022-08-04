file = open("radixsort.in")
output = open("radixsort.out", "w")
read = list(map(int, file.readline().split()))
strcount = read[0]
strlen = read[1]
digitalcount = read[2]
array = file.read().split()
#nmk
def sort(array, digitalcount):
    alphabet = [0]*26
    for i in range(len(array)):
        alphabet[ord(array[i][digitalcount-1])-ord('a')] += 1
    for i in range(1, 26):
        alphabet[i] = alphabet[i]+alphabet[i-1]
    answer = [0]*len(array)
    for i in range(len(array)-1, -1, -1):
        answer[alphabet[ord(array[i][digitalcount-1])-ord('a')]-1] = array[i]
        alphabet[ord(array[i][digitalcount-1])-ord('a')] -= 1
    return answer
while(digitalcount > 0):
    array = sort(array, strlen)
    strlen = strlen - 1
    digitalcount = digitalcount - 1
for i in range(len(array)):
    output.write(str(array[i])+'\n')
