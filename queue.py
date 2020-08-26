#enqueue() -> dequeue() -> isempty() -> length() -> start() -> back()
class queue:
    def __init__(self):
        self.queue1= []
    def enqueue(self,item):
        self.queue1.insert(0,item)
    def dequeue(self):
        item= self.queue1[len(self.queue1)-1]
        self.queue1.pop(len(self.queue1)-1)
        print(item)
    def isempty(self):
        if len(self.queue1)==0:
            print("Empty")
        else:
            print("not empty")
    def length(self):
        print(len(self.queue1))
    def start(self):
        print(self.queue1[len(self.queue1)-1])
    def last(self):
        print(self.queue1[0])
q1= queue()
q1.enqueue(43)
q1.enqueue(23)
q1.enqueue(57)
q1.length()
q1.dequeue()
q1.enqueue(56)
q1.length()
q1.last()
