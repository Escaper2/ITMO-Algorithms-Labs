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


def matrixCreation():
    matrix = [[0] * countOfVertices for _ in range(countOfVertices)]
    print(matrix)
    for i in range(countOfEdges):
        matrix[array[i][0] - 1][array[i][1] - 1] = matrix[array[i][0] - 1][array[i][1] - 1] + 1
        matrix[array[i][1] - 1][array[i][0] - 1] = matrix[array[i][1] - 1][array[i][0] - 1] + 1
    return matrix


def matrixCheck():
    flag = 0
    for i in range(countOfVertices):
        for j in range(countOfVertices):
            if matrix[i][j] > 1:
                flag = 1
    print(flag)
    if flag == 1:
        out.write("YES")
        exit()
    out.write("NO")


input()
matrix = matrixCreation()
matrixCheck()
