class Node:
    def __init__(self,data=None,Next=None):
        self.data=data
        self.Next=Next

class single:
    def __init__(self):
        self.head=None

    def insert_at_end(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
        else:
            n=self.head
            while n.Next is not None:
                n=n.Next
            n.Next=node

    def display(self):
        if self.head is None:
            print('No data')
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.Next

ll=single()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_end(40)
ll.display()

