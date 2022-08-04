file = open('antiqs.in')
output = open('antiqs.out','w')
num = int(file.readline())
arr = [i for i in range(1,num+1)]
for i in range(2,num):
    arr[i],arr[i//2] = arr[i//2],arr[i]
answer = ' '.join(map(str,arr))
print(answer)
output.write(answer)