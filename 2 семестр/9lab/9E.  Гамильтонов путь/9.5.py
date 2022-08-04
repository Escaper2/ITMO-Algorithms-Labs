file = open("hamiltonian.in")
out = open("hamiltonian.out", "w")

from collections import defaultdict

countString = file.readline().split()
countOfEdges = int(countString[1])
countOfVertices = int(countString[0])

adjencyDict = defaultdict(list)

fa = []
sa = []
ars = []
cnt1 = 0
cnt2 = 0
fl = 0
for i in range(countOfVertices):
    adjencyDict[i + 1] = []
for i in range(countOfVertices):
    fa.append(0)
for i in range(countOfVertices):
    sa.append(0)

for i in range(countOfEdges):
    temp = (list(map(int, file.readline().split())))
    adjencyDict[temp[0]].append(temp[1])
    fa[temp[0] - 1] = fa[temp[0] - 1] + 1
    sa[temp[1] - 1] = sa[temp[1] - 1] + 1


def check(c,fl):
    cnt3 = 0
    for i in range(len(adjencyDict[c])):
        if (fa[adjencyDict[c][i] - 1] == 1) and (sa[adjencyDict[c][i] - 1] == 1):
            cnt3 += 1
    if cnt3 > 1:
        fl = 1
    return fl


cnt4 = 0
for i in fa:
    cnt4 = cnt4 + 1
    if i == 0:
        cnt1 = cnt1 + 1
    if i > 1:
        fl = check(cnt4,fl)
for i in sa:
    if i == 0:
        cnt2 = cnt2 + 1

if (cnt1 == 1) and (cnt2 == 1) and (fl == 0):
    out.write(str("YES"))
else:
    out.write(str("NO"))