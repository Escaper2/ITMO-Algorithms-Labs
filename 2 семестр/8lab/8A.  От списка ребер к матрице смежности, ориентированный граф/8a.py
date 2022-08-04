file = open("input.txt")
out = open("output.txt", "w")
array = []
countString = file.readline().split()
countOfEdges = int(countString[1])
countOfVertices = int(countString[0])


def input():
    for i in range(countOfEdges):
        array.append(list(map(int, file.readline().split())))
    return array


def output(matrix):
    for i in range(len(matrix)):
        for j in range(countOfVertices):
            out.write(str(matrix[i][j]) + " ")
        out.write('\n')


def matrixCreation():
    matrix = [[0] * countOfVertices for _ in range(countOfVertices)]
    for i in range(countOfEdges):
        matrix[array[i][0] - 1][array[i][1] - 1] = 1
    return output(matrix)


input()
matrixCreation()
