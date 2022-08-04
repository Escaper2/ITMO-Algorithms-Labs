file = open("isheap.in")
output = open("isheap.out", "w")
number = int(file.readline())
arr = list(map(int, file.readline().split()))
i = 1
count = 0
for i in range(number+1):
    if i > 0:
        if 2*i <= number:
            if arr[i - 1] <= arr[2*i - 1]:
                count = count + 1
        if 2*i + 1 <= number:
            if arr[i - 1] <= arr[2*i]:
                count = count + 1
    i += 1
if count == number-1:
    output.write('YES')
else:
    output.write('NO')
