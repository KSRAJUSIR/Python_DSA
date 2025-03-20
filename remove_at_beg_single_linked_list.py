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

    def remove_at_beg(self):
        if self.head is None:
            print("empty")
        else:
            self.head=self.head.Next
    
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
ll.remove_at_beg()
ll.display()
            