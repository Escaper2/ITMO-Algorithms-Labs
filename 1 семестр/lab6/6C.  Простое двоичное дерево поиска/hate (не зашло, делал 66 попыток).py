file = open("bstsimple.in")
output = open("bstsimple.out",'w')
array = []

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class bst:
    def __init__(self):
        self.root = None

    def insert(self,node,data):
        if node:
            if data < node.data:
                if node.left is None:
                    node.left = TreeNode(data)
                else:
                    self.insert(node.left,data)
            elif data > node.data:
                if node.right is None:
                    node.right = TreeNode(data)
                else:
                    self.insert(node.right,data)
        else:
            self.root = TreeNode(data)

    def exists(self,node,data):
        if node is None:
            return "false"
        if node.data is None:
            return "false"
        if data < node.data:
            if node.left is None:
                return "false"
            return self.exists(node.left,data)
        elif data > node.data:
            if node.right is None:
                return "false"
            return self.exists(node.right,data)
        else:
            return "true"
    def minimum(self,node):
        if node.left is None:
            return node
        return self.minimum(node.left)

    def next(self, data):
        current = self.root
        next = None
        while current != None:
            if current.data > data:
                next = current
                current = current.left
            else:
                current = current.right
        # if successor != None:
        #     return successor.data
        # else:
        #     return "none"
        return next
    def prev(self,data):
        current = self.root
        prev = None
        while current != None:
            if current.data < data:
                prev = current
                current = current.right
            else:
                current = current.left
        return prev

        # if node is None:
        #     return None
        # if data < node.data:
        #     node.left = self.delete(node.left, data)
        #     return node
        # elif data > node.data:
        #     node.right = self.delete(node.right, data)
        #     return node
        # if node.left == None and node.right == None:
        #     return None
        # elif node.left != None and node.right != None:
        #     node.data = self.minimum(node.right).data
        #     node.right = self.delete(node.right, node.data)
        # else:
        #     if node.left != None and node.right == None:
        #         return node.left
        #     elif node.right != None and node.left == None:
        #         return node.right
        # return node
    def delete(self,node, data):
        if node is None:
            return None
        if self.root.data == data:
            if self.root.left != None and self.root.right == None:
                self.root = self.root.left
            elif self.root.left == None and self.root.right == None:
                self.root = None
            else:
                curr = self.root.right
                if curr.left == None:
                    self.root.data = curr.data
                    self.root.right = curr.right
                else:
                    while curr.left != None:
                        curr = curr.left
                    self.root.data = curr.data
                    if curr.right != None:
                        curr.data = curr.right.data
                        curr.right = None
        if data < node.data:
            node.left = self.delete(node.left,data)
        elif data > node.data:
            node.right = self.delete(node.right,data)
        elif node.right != None and node.left != None:
            node.data = self.minimum(node.right).data
            node.right = self.delete(node.roight,node.data)
        else:
            if node.left != None:
                node = node.left
            else:
                node = node.right
        return node
bst = bst()
for i in file:
    array = i.split()
    if array[0] == "insert":
        bst.insert(bst.root,int(array[1]))
    elif array[0] == "exists":
        output.write(str(bst.exists(bst.root,int(array[1])))+"\n")
    elif array[0] == "next":
        answ = bst.next(int(array[1]))
        if answ:
            output.write(str(answ.data)+"\n")
        else:
            output.write("none")
            output.write("\n")
    elif array[0] == "delete":
        bst.delete(bst.root,int(array[1]))
    elif array[0] == "prev":
        answ = bst.prev(int(array[1]))
        if answ:
            output.write(str(answ.data)+"\n")
        else:
            output.write("none")
            output.write("\n")
