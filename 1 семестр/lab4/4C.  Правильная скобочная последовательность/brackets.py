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

    def push(self, data):
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
    def printf(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

def postfx(to_do):
    stack = Stack()
    status = True
    for i in to_do:
        if i in '([':
            stack.push(i)
        elif i in ')]':
            bracket = stack.pop()
            if bracket == '(' and i == ')':
                continue
            if bracket == '[' and i == ']':
                continue
            status = False
            break
    if status and stack.empty():
        return('YES')
    else:
        return('NO')
file = open('brackets.in')
output = open('brackets.out', 'w')
to_do = file.readlines()
for i in range(len(to_do)):
    output.write(postfx(to_do[i])+'\n')