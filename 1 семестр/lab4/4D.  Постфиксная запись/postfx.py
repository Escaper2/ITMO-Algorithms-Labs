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
    for i in to_do:
        (stack.printf())
        if i != '+' and i !='-' and i != '*':
            stack.push(i)
        else:
            firstVar = int(stack.pop())
            secondVar = int(stack.pop())
            if i == '+':
                stack.push(firstVar+secondVar)
            elif i == '-':
                stack.push(secondVar-firstVar)
            elif i == '*':
                stack.push(firstVar*secondVar)
    return stack.pop()




file = open('postfix.in')
output = open('postfix.out', 'w')
to_do = file.readline().split()
output.write(str(postfx(to_do)))