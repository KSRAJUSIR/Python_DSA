class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    def preorder(self):
        print(str(self.value)+"--->",end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
root=Node(5)
root.right=Node(20)
root.left=Node(10)
root.preorder()
    
