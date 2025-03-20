class dynamic:
    def __init__(self):
        self.size=0
        self.array=[]
    def add(self,value):
        self.array.append(value)
        self.size+=1
    def get(self,index):
        return self.array[index]
    def print_all(self):
        for i in range(self.size):
            print(self.array[i])
dynm=dynamic()
dynm.add(20)
dynm.add(30)
dynm.add(50)
val=dynm.get(0)
print("selected value",val)
dynm.print_all()