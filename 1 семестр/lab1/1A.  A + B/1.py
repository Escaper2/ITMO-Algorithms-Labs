q = open('aplusb.in')
w = open('aplusb.out', 'w')
e = q.readline()
a = e.split()
b = int(a[0])
c = int(a[1])
y = b + c
w.write(str(y))