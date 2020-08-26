#push() -> pop() -> peek() -> length() -> overflow()
class stack:
    def __init__(self,size):
        self.stack1= []
        self.size= size
    def push(self,item):
        self.stack1.append(item)
    def pop(self):
        item = self.stack1[len(self.stack1)-1]
        self.stack1.pop(len(self.stack1)-1)
        return item
    def peek(self):
        return self.stack1[len(self.stack1)-1]
    def length(self):
        return len(self.stack1)
    def overflow(self):
        if len(self.stack1)> self.size:
            print("Overflow")
        else:
            print("Not yet")
s1= stack(4)
s1.push(2)
s1.push(3)
s1.push(4)
s1.overflow()
s1.push(7)
s1.overflow()
s1.pop()
s1.push(5)
s1.overflow()