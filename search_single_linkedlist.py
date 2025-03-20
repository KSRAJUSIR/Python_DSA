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

    def display(self):
        n=self.head
        if n is None:
            print("no data")
        else:
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.Next
                if n.data==30:
                    print('found',n.data)
                    break
                
ll=single()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.insert(50)
ll.display()
       
