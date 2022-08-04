file = open("input.txt")
out = open("output.txt", "w")
countOfVertices = int(file.readline())
array = []


def input():
    for i in range(countOfVertices):
        array.append(list(map(int, file.readline().split())))
    return array


def matrixCheck():
    mainDiagonal = 0
    flag = None
    for i in range(countOfVertices):
        if array[i][i] == 0:
            mainDiagonal += 1
    for i in range(countOfVertices):
        for j in range(countOfVertices):
            if array[i][j] != array[j][i]:
                flag = 1

    if flag == 1 or mainDiagonal != countOfVertices:
        out.write("NO")
        exit()

    out.write("YES")


input()
matrixCheck()
