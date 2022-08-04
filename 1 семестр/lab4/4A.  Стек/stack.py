class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    def empty(self):
        if self.head == None:
            return True
        else:
            return False
    def push(self,data):
        if self.empty():
            self.head = Node(data)
        else:
            tempnode = Node(data)
            tempnode.next = self.head
            self.head = tempnode
    def pop(self):
        if self.empty():
            return None
        else:
            poptemp = self.head
            self.head = self.head.next
            poptemp.next = None
            return poptemp.data
file = open('stack.in')
output = open('stack.out','w')
number = file.readline()
stack = Stack()
for i in range(int(number)):
    to_do = file.readline().split()
    if to_do[0] == '+':
        stack.push(to_do[1])
    elif to_do[0] == '-':
        output.write(stack.pop()+'\n')





