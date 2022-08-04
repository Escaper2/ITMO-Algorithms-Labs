import math

countOfSubsequence = int(input())

arrayOfLen = []

arrayOfParents = []

[arrayOfLen.append(math.inf) for i in range(countOfSubsequence)]

[arrayOfParents.append(math.inf) for i in range(countOfSubsequence)]

# arrayOfSubsequence = list(map(int,input().split()))

arrayOfSubsequence = input().split()

path = []

pos = 0

# arrayOfLen[0] = -math.inf
#
# for i in range(countOfSubsequence):
#     for j in range(1, countOfSubsequence):
#         if float(arrayOfLen[j - 1]) < float(arrayOfSubsequence[i]) < float(arrayOfLen[j]):
#             arrayOfLen[j] = arrayOfSubsequence[i]

# tmp = []

# for i in arrayOfLen:
#     if i != math.inf and i != -math.inf:
#         tmp.append(i)
#     print(i)

# print(len(tmp))

# if len(tmp) == 0:
#     exit()

# print(int(tmp[0])+1)
# cnt = 0
# for i in range(len(tmp)):
#
#     # if i != len(tmp)-1:
#     #     if arrayOfSubsequence.index(tmp[i]) > arrayOfSubsequence.index(tmp[i+1]):
#     #         print(int(tmp[i])+1)
#     #         continue
#
#     print(tmp[i])

for i in range(countOfSubsequence):
    arrayOfLen[i] = 1
    arrayOfParents[i] = -1
    for j in range(i):
        if float(arrayOfSubsequence[j]) >= float(arrayOfSubsequence[i]):
            continue
        if 1 + float(arrayOfLen[j]) > float(arrayOfLen[i]):
            arrayOfLen[i] = 1 + float(arrayOfLen[j])
            arrayOfParents[i] = j

ans = arrayOfLen[0]


for i in range(countOfSubsequence):
    if arrayOfLen[i] > ans:
        ans = arrayOfLen[i]
        pos = i

while pos != -1:
    path.append(pos)
    pos = arrayOfParents[pos]

path.reverse()

print(int(ans))

for i in range(len(path)):
    print(arrayOfSubsequence[path[i]])


