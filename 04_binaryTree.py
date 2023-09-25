class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if not self.data:
            self.data = data
            return
        
        if(data < self.data):
            if(not self.left):
                self.left = TreeNode(data)
                return
            else:
                self.left.insert(data)
        else:
            if(not self.right):
                self.right = TreeNode(data)
                return
            else:
                self.right.insert(data)

    def inOrder(self, pos):
        if(not pos.left):
            print(pos.data)
            return
        else:
            self.inOrder(pos.left)
        if(not pos.right):
            print(pos.data)
            return
        else:
            self.inOrder(pos.right)
myTree = TreeNode(100)
myTree.insert(110)
myTree.insert(90)
myTree.insert(85)
myTree.inOrder(myTree)