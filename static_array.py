class Static:
    def __init__(self,size):
        self.size=size
        self.array=[None]*size
    def add_data(self,index,value):
        if index<0 or index>=self.size:
            raise IndexError("index is in correct")
        else:
            self.array[index]=value
    def get(self,index):
        return self.array[index]
    def print_all(self):
        for i in range(self.size):
            print(self.array[i])
stat=Static(5)
stat.add_data(0,11)
stat.add_data(1,44)
stat.add_data(2,55)
stat.add_data(2 ,99)
stat.add_data(4,66)
stat.add_data(4,67)
data=stat.get(4)
print(data)
stat.print_all()
