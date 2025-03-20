class queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,value):
        self.queue.insert(0,value)
    def dequeue(self):
        self.queue.pop()
    def get_item(self,index):
        print(self.queue[index])
    def print_all(self):
        print(str(self.queue))
q=queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.dequeue()
q.get_item(1)
q.print_all()