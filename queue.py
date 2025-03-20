class Queue:
    def __init__(self):
        self.queue=[]
    def push(self,value):
        self.queue.insert(0,value)
    def remove(self):
        self.queue.pop()
    def get_item(self,index):
        print(self.queue[index])
    def display(self):
        print(str(self.queue)) 
s=Queue()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.remove()
s.display()
s.get_item(2)