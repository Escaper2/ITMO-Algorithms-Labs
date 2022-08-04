import math
#
# file = open("pathmgep.in")
# out = open("pathmgep.out", "w")

#from collections import defaultdict

#import sys

#from math import sqrt

#sys.setrecursionlimit(2000000)

# countString = file.readline().split()
# countOfVertices = int(countString[0])
# startVert = int(countString[1])
# endVert = int(countString[2])
# countOfVertices, startVert, endVert = map(int,input().split())

visited = []

matrixx = []

anArr = []

subArr = []


class vertex():

    def __init__(self, x1=None, y1=None):
        self.x = x1
        self.y = y1
        self.distance = 1000000000



def getWeight(fisrt, second):
    return (((pow((second[0] - fisrt[0]), 2) + pow((second[1] - fisrt[1]), 2))))



def dinput():
    matrixx = [[math.inf] * countOfVertices for _ in range(countOfVertices)]
    [subArr.append(list(map(int,file.readline().split()))) for i in range(countOfEdges)]

    for i in range(countOfEdges):
        matrixx[subArr[i][0] -1][subArr[i][1] - 1] = subArr[i][2]
    return matrixx
    # for i in range(countOfVertices):
    #     matrix.append(list(map(int,file.readline().split())))
    # for i in range(countOfVertices):
    #     tmp = list(map(int, file.readline().split()))
    #     matrix.append([])
    #     for j in range(countOfVertices):
    #         if tmp[j] == -1:
    #             matrix[i].append(math.inf)
    #             continue
    #         matrix[i].append(tmp[j])




def matrixCreation():
    matrix = [[math.inf] * countOfVertices for _ in range(countOfVertices)]

    for i in range(countOfVertices):
        first = matrix[i]
        # matrix[array[i][0] - 1][array[i][1] - 1] = matrix[array[i][0] - 1][array[i][1] - 1] + 1
        # matrix[array[i][1] - 1][array[i][0] - 1] = matrix[array[i][1] - 1][array[i][0] - 1] + 1
        for j in range(countOfVertices):
            if i == j:
                continue
            else:
                sec = matrix[j]
                matrix[i][j] = getWeight(first, sec)
    return matrix


#answers = 0

#answer = []

#subArr = []


def check(answers,min):
    a = -1
    for j in range(countOfVertices):
        if anArr[j][0] < min and (visited[j] == 0):
            min = anArr[j][0]
            a = j
    visited[a] = 1
    return a




def prim(c):
    answers = 0
    [anArr.append([math.inf]) for i in range(countOfVertices)]
    [visited.append(0) for i in range(countOfVertices)]
    anArr[c] = [0]
    for i in range(countOfVertices):
        mind = math.inf
        a = check(answers,mind)
        for j in range(countOfVertices):
            if (anArr[a][0] + matrix[a][j] < anArr[j][0]):
                anArr[j][0] = anArr[a][0] + matrix[a][j]
            # anArr[j][0] = min(anArr[j][0],anArr[a][0] + matrix[a][j])
    return anArr








with open("pathsg.in", "r", encoding='utf-8') as file:
    with open("pathsg.out","w",encoding="utf-8") as output:
        countString = file.readline().split()
        countOfVertices = int(countString[0])
        countOfEdges = int(countString[1])
        matrix = dinput()
        for i in range(countOfVertices):
            answ = prim(i)
        # if anArr[endVert-1][0] == math.inf:
        #     print(-1)
        #     exit()
            for i in answ:
                output.write(str(i[0]) + " ")
            output.write("\n")
            anArr.clear()
            visited.clear()

# for i in range(countOfVertices):
#     tmp = {i + 1}
#     vis.append(tmp)
#
# for i in range(countOfVertices):
#     temp = i + 1
#     subArr.append([temp])
#     visited.append(temp)
#     anArr.append(temp - 1)

#
# def adjacencyList():
#     #     adjencyDict[i + 1] = []
#     #     degreeDict[i + 1] = 0
#
#     for i in range(countOfEdges):
#         temp = list(map(int, file.readline().split()))
#         start = temp[0]
#         end = temp[1]
#         value = temp[2]
#         edgesDict[i].append(value)
#         edgesDict[i].append(start)
#         edgesDict[i].append(end)


