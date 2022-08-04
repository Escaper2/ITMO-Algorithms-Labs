inp = open('aplusbb.in')
output = open('aplusbb.out','w')
q = inp.readline()
a = q.split()
b = int(a[0])
c = int(a[1])
d = c**2
e = b + d
output.write(str(e))
