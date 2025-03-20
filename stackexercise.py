class web_browsing:
    def __init__(self):
        self.stack=[]
    def push(self,value):
        self.stack.append(value)
    def pop(self):
        self.stack.pop()
    def display(self):
        print(str(self.stack))
w=web_browsing()
w.push('google')
w.push('flipkart')
w.push('groceries')
w.push('fruits & veg')
w.pop()
w.pop()
w.display()