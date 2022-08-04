array = []
size = 10000
table = [[] for i in range(size)]
def hash(i):
    index = abs(i % size)
    return index
with open("set.in", "r", encoding='utf-8') as file:
    with open("set.out","w",encoding="utf-8") as output:
        for i in file:
            array = i.split()
            if array[0] == "insert":
                digit = int(array[1])
                index = hash(digit)
                if digit not in table[index]:
                    table[index].append(digit)
            elif array[0] == "exists":
                find = int(array[1])
                index = hash(find)
                if find not in table[index]:
                    output.write("false\n")
                else:
                    output.write("true\n")
            elif array[0] == "delete":
                delete = int(array[1])
                index = hash(delete)
                if delete in table[index]:
                    table[index].remove(delete)
