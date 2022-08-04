file = open("spantree3.in")
out = open("spantree3.out", "w")

from collections import defaultdict

import sys

sys.setrecursionlimit(2000000)

countString = file.readline().split()
countOfEdges = int(countString[1])
countOfVertices = int(countString[0])
answer = []

visited = []

subArr = []

edgesDict = defaultdict(list)

vis = []

anArr = []

for i in range(countOfVertices):
    tmp = {i + 1}
    vis.append(tmp)

for i in range(countOfVertices):
    temp = i + 1
    subArr.append([temp])
    visited.append(temp)
    anArr.append(temp - 1)


def adjacencyList():
    #     adjencyDict[i + 1] = []
    #     degreeDict[i + 1] = 0

    for i in range(countOfEdges):
        temp = list(map(int, file.readline().split()))
        start = temp[0]
        end = temp[1]
        value = temp[2]
        edgesDict[i].append(value)
        edgesDict[i].append(start)
        edgesDict[i].append(end)

        # edgesDict[temp[2]].append(temp[1])
        #
        # adjencyDict[temp[0]].append(temp[1])
        # adjencyDict[temp[1]].append(temp[0])


# def sort():
#     for i in range(1, len(adjencyDict) + 1):
#         temp = adjencyDict.get(i + 1)
#         for j in range(len(adjencyDict[i])):
#             degreeDict[adjencyDict[i][j]] = degreeDict[adjencyDict[i][j]] + 1
#
#     for i in degreeDict:
#         if degreeDict[i] == 0:
#             supQ.append(i)
#
#     while len(supQ) != 0:
#         temp = supQ.popleft()
#         answer.append(temp)
#         for i in adjencyDict[temp]:
#             degreeDict[i] = degreeDict[i] - 1
#             if degreeDict[i] == 0:
#                 supQ.append(i)
#     if (len(answer)) != countOfVertices:
#         garbage = 0


adjacencyList()
sa = sorted(edgesDict.items(), key=lambda i: i[1])
answers = 0
n = 0
z = countOfVertices - 1

#
# def find(find):
#     for i in vis:
#         if find in i:
#             return vis.index(i)
#

#
# for i in range(len(sa)):
#     end = sa[i][1][2]
#     start = sa[i][1][1]
#     a = find(start)
#     b = find(end)
#     if vis[a].isdisjoint(vis[b]):
#         n = n + 1
#         answers = answers + sa[i][1][0]
#         if n == z:
#             print(answers)
#             exit()
#         if vis[a] > vis[b]:
#             vis[a] = vis[a].union(vis[b])
#             vis[b].clear()
#         elif vis[a] < vis[b]:
#             vis[b] = vis[b].union(vis[a])
#             vis[a].clear()
#         else:
#             vis[a] = vis[a].union(vis[b])
#             vis[b].clear()


# for i in range(len(sa)):
#     if visited[sa[i][1][2] - 1] == visited[sa[i][1][1] - 1]:
#         continue
#     else:
#         end = visited[sa[i][1][2] - 1]
#         start = visited[sa[i][1][1] - 1]
#         startSize = len(subArr[start - 1])
#         endSize = len(subArr[end - 1])
#         if startSize < endSize:
#             for j in range(len(subArr[start - 1])):
#                 visited[subArr[start - 1][j] - 1] = subArr.index(subArr[end - 1]) + 1
#                 tmp = subArr[start - 1][j]
#                 subArr[end - 1].append(tmp)
#             subArr[start - 1].clear()
#         else:
#             for j in range(len(subArr[end - 1])):
#                 visited[subArr[end - 1][j] - 1] = subArr.index(subArr[start - 1]) + 1
#
#                 tmp = subArr[end - 1][j]
#                 subArr[start - 1].append(tmp)
#             subArr[end - 1].clear()
#         answers = answers + sa[i][1][0]
#         n = n + 1
#         if n == z:
#             print(answers)
#             exit()
# if (visited[sa[i][1][2]- 1] == visited[sa[i][1][1] - 1]):
#     continue
# else:
#     answers = answers + sa[i][1][0]
#     end = visited[sa[i][1][2]-1]
#     start = visited[sa[i][1][1]-1]
#     n = n + 1
#     if n == z:
#         print(answers)
#         exit()
#     for c in range(countOfVertices):
#         if visited[c] == end:
#             visited[c] = start

# if set(start).isdisjoint(set(end)):
#     print(set(start), set(end))
#     answers = answers + sa[i][1][0]
#     if set(start) < set(end):
#         set(start).union(set(end))
#         set(start).clear()
#     else:
#         set(end).union(set(start))
#         set(end).clear()

# gray[sa[i][1][j][0] - 1] = True
# gray[sa[i][1][j][1] - 1] = True
# if gray[sa[i][1][j][1]-1] == True:
#     visited[sa[i][1][j][0] - 1] = visited[sa[i][1][j][1] - 1]
# else:
#     visited[sa[i][1][j][1] - 1] = visited[sa[i][1][j][0] - 1]



def get(a):
    if a == anArr[a]:
        return a
    else:
        anArr[a] = get(anArr[a])
        return anArr[a]


for i in range(countOfEdges):
    end = visited[sa[i][1][2] - 1]-1
    start = visited[sa[i][1][1] - 1]-1
    if get(end) != get(start):
        answers = answers + sa[i][1][0]
        first = get(end)
        sec = get(start)
        if first != sec:
            anArr[first] = sec
print(answers)