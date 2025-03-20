class Node:
    def __init__(self,data=None,Next=None):
        self.data=data
        self.Next=Next
class single:
    def __init__(self):
        self.head=None

    def insert(self,data):
        node=Node(data)
        node.Next=self.head
        self.head=node

    def remove_at_end(self):
        if self.head is None:
            return 
        if self.head.Next is None:
            self.head=None
            return
        current_node=self.head
        previous_node=None
        while current_node.Next is not None:
            previous_node=current_node
            current_node=current_node.Next
        previous_node.Next=None
    
    def display(self):
        if self.head is None:
            self.head=Node
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.Next

ll=single()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.remove_at_end()
ll.display()
            