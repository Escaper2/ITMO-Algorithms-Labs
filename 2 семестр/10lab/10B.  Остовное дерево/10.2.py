import math

file = open("spantree.in")
out = open("spantree.out", "w")

from collections import defaultdict

import sys

from math import sqrt

sys.setrecursionlimit(2000000)

countString = file.readline().split()
countOfVertices = int(countString[0])

visited = []

array = []

anArr = []


class vertex():

    def __init__(self, x1=None, y1=None):
        self.x = x1
        self.y = y1
        self.distance = 1000000000


def getWeight(fisrt,second):

    return (((pow((second[0]-fisrt[0]),2)+pow((second[1]-fisrt[1]),2))))

[visited.append(0) for i in range(countOfVertices)]

[anArr.append([math.inf]) for i in range(countOfVertices)]

def input():
    for i in range(countOfVertices):
        array.append(list(map(int,file.readline().split())))
    anArr[0] = [0]

input()


def matrixCreation():
    matrix = [[0] * countOfVertices for _ in range(countOfVertices)]
    for i in range(countOfVertices):
        first = array[i]
        # matrix[array[i][0] - 1][array[i][1] - 1] = matrix[array[i][0] - 1][array[i][1] - 1] + 1
        # matrix[array[i][1] - 1][array[i][0] - 1] = matrix[array[i][1] - 1][array[i][0] - 1] + 1
        for j in range(countOfVertices):
            if i == j:
                continue
            else:
                sec = array[j]
                matrix[i][j] = getWeight(first,sec)
    return matrix


matrix = matrixCreation()
answers = 0


answer = []



subArr = []

edgesDict = defaultdict(list)

def prim():
    answers = 0
    for i in range(countOfVertices):
        min = math.inf
        for j in range(countOfVertices):
            if anArr[j][0] < min and (visited[j] == 0):
                min = anArr[j][0]
                a = j
        answers = answers + min
        visited[a] = 1
        for j in range(countOfVertices):
            if (matrix[a][j] < anArr[j][0] and visited[j] != 1):
                anArr[j][0] = matrix[a][j]


import math

file = open("spantree.in")
out = open("spantree.out", "w")

from collections import defaultdict

import sys

from math import sqrt

countString = file.readline().split()
countOfVertices = int(countString[0])

visited = []

array = []

anArr = []
def printa():
    res = 0
    for i in range(countOfVertices):
        res = res + sqrt(answers[i][0])
    print(res)


def getWeight(fisrt, second):
    return (((pow((second[0] - fisrt[0]), 2) + pow((second[1] - fisrt[1]), 2))))


[visited.append(0) for i in range(countOfVertices)]

[anArr.append([math.inf]) for i in range(countOfVertices)]


def input():
    for i in range(countOfVertices):
        array.append(list(map(int, file.readline().split())))
    anArr[0] = [0]


input()


def matrixCreation():
    matrix = [[0] * countOfVertices for _ in range(countOfVertices)]
    for i in range(countOfVertices):
        first = array[i]
        # matrix[array[i][0] - 1][array[i][1] - 1] = matrix[array[i][0] - 1][array[i][1] - 1] + 1
        # matrix[array[i][1] - 1][array[i][0] - 1] = matrix[array[i][1] - 1][array[i][0] - 1] + 1
        for j in range(countOfVertices):
            if i == j:
                continue
            else:
                sec = array[j]
                matrix[i][j] = getWeight(first, sec)
    return matrix


matrix = matrixCreation()
answers = 0

answer = []

subArr = []

edgesDict = defaultdict(list)


def check(answers,min):
    for j in range(countOfVertices):
        if anArr[j][0] < min and (visited[j] == 0):
            min = anArr[j][0]
            a = j
    answers = answers + min
    visited[a] = 1
    return answers,a



def prim():
    answers = 0
    for i in range(countOfVertices):
        min = math.inf
        answers,a = check(answers,min)
        for j in range(countOfVertices):
            if (matrix[a][j] < anArr[j][0] and visited[j] != 1):
                anArr[j][0] = matrix[a][j]

    return anArr






answers = prim()
res = 0
printa()

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


