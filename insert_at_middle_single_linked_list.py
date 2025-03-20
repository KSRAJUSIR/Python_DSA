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


    def insert_in_middle(self,data,position):
        node=Node(data)
        if position==0:
            node.head=self.Next
            self.head=node
        else:
            n=self.head
            count=0
            while n is not None and count<position-1:
                n=n.Next
                count+=1
            
            node.Next=n.Next
            n.Next=node

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
ll.insert_in_middle(25,3)
ll.insert_in_middle(55,4)
ll.insert_in_middle(20,5)
ll.display()
            





    
    