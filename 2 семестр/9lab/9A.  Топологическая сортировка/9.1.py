file = open("topsort.in")
out = open("topsort.out", "w")

from collections import defaultdict
from collections import deque

supQ = deque()
countString = file.readline().split()
countOfEdges = int(countString[1])
countOfVertices = int(countString[0])
answer = []
adjencyDict = defaultdict(list)
degreeDict = dict()

if (countOfVertices or countOfEdges) == 0:
    (out.write(str(-1)))
    exit()


def adjacencyList():
    for i in range(countOfVertices):
        adjencyDict[i + 1] = []
        degreeDict[i + 1] = 0

    for i in range(countOfEdges):
        temp = list(map(int, file.readline().split()))
        adjencyDict[temp[0]].append(temp[1])


def sort():
    for i in range(1, len(adjencyDict) + 1):
        temp = adjencyDict.get(i + 1)
        for j in range(len(adjencyDict[i])):
            degreeDict[adjencyDict[i][j]] = degreeDict[adjencyDict[i][j]] + 1

    for i in degreeDict:
        if degreeDict[i] == 0:
            supQ.append(i)

    while len(supQ) != 0:
        temp = supQ.popleft()
        answer.append(temp)
        for i in adjencyDict[temp]:
            degreeDict[i] = degreeDict[i] - 1
            if degreeDict[i] == 0:
                supQ.append(i)
    if (len(answer)) != countOfVertices:
        out.write(str(-1))
        exit()


adjacencyList()

sort()



for i in range(len(answer)):
    out.write(str(answer[i]) + " ")



