import heapq
class prority:
    def __init__(self):
        self.queue=[]
    def push(self,item,prority):
        heapq.heappush(self.queue,(prority,item))
    def dequeue(self):
        return heapq.heappop(self.queue)[1]
    def display(self):
        temp=self.queue.copy()
        temp.sort()
        for prority,item in temp:
            print(f"Item: {item}, Priority: {prority}")



pq=prority()
pq.push("walk",12)
pq.push("sleep",1)
pq.push("sit",2)
pq.dequeue()
pq.display()
