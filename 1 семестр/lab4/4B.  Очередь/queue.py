class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Que:
    def __init__(self):
        self.head = None
        self.tail = None
    def headEmpty(self):
        if self.head is None:
            return True
        else:
            return False
    def headNextEmpty(self):
        if self.head.next is None:
            return True
        else:
            return False
    def push(self,data):
        tempNode = Node(data)
        if self.headEmpty():
            self.head = self.tail = tempNode
        elif self.headNextEmpty():
            self.head.next = self.tail = tempNode
        else:
            self.tail.next = tempNode
            self.tail = self.tail.next
    def pop(self):
        if self.headEmpty():
            return None
        else:
            popTemp = self.head
            self.head = self.head.next
            popTemp.next = None
            return popTemp.data
file = open('queue.in')
output = open('queue.out','w')
number = file.readline()
que = Que()
for i in range(int(number)):
    to_do = file.readline().split()
    if to_do[0] == '+':
        que.push(to_do[1])
    elif to_do[0] == '-':
        output.write(que.pop()+'\n')





