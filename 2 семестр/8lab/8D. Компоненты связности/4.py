file = open("components.in")
out = open("components.out", "w")
countString = file.readline().split()
countOfEdges = int(countString[1])
countOfVertices = int(countString[0])

gray = [False] * countOfVertices
adjacencyList = [[] for _ in range(countOfVertices)]
componentsList = [[] for _ in range(countOfVertices)]


def input():
    supCnt = 0
    for x in range(countOfEdges):
        first, second = 0, 0
        for j in file.readline().split():
            supCnt = supCnt + 1
            if supCnt % 2 != 0:
                first = int(j) - 1
            if supCnt % 2 == 0:
                second = int(j) - 1
            continue
        adjacencyList[first].append(second)
        adjacencyList[second].append(first)


def findComponents():
    numberOfComponents = 0
    for i in range(countOfVertices):
        if gray[i]:
            continue

        numberOfComponents = numberOfComponents + 1
        gray[i] = True
        Vertices = [i]
        while Vertices:
            v = Vertices.pop()
            for j in adjacencyList[v]:
                if not gray[j]:
                    gray[j] = True
                    Vertices.append(j)
                    componentsList[j] = numberOfComponents
        componentsList[i] = numberOfComponents

    return componentsList


def output():
    out.write(str(max(componentsList)) + "\n")
    for i in range(len(componentsList)):
        out.write(str(componentsList[i]) + " ")


input()

findComponents()

output()
