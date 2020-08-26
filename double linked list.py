class node:
    def __init__(self,data):
        self.data= data 
        self.next_node= None 
        self.prev_node= None 
class doublelinkedlist:
    def __init__(self):
        self.start= None 
    def insert_end(self,data):
        newnode= node(data)
        if self.start==None:
            self.start= newnode 
        else:
            temp= self.start
            while temp.next_node!=None:
                temp = temp.next_node
            temp.next_node= newnode
            newnode.prev_node= temp
    def traverse(self):
        temp= self.start 
        while temp!=None:
            print(temp.data)
            temp= temp.next_node
    def insert_beg(self,data):
        newnode = node(data)
        if self.start==None:
            self.start = newnode
        else:
            temp = self.start
            newnode.next_node = temp 
            self.start= newnode
    def insert_k(self,data,k):
        newnode = node(data)
        if k==0:
            self.insert_beg(data)
        else:
            temp= self.start 
            count= 0 
            while True:
                prev = temp
                temp= temp.next_node 
                count+=1 
                if k==count:
                    newnode.next_node= temp
                    newnode.prev_node = prev 
                    prev.next_node = newnode 
                    break
    def delete_end(self):
        if self.start== None:
            return -1 
        else:
            temp= self.start 
            while temp.next_node!=None:
                prev= temp
                temp= temp.next_node
            prev.next_node= None
            temp.prev_node = None
    def delete_beg(self):
        if self.start==None:
             return -1 
        else:
            temp = self.start
            next1= self.start.next_node 
            temp.next_node=None 
            self.start= next1
    def delete_k(self,k):
        if k==0:
            self.delete_beg()
        else:
            temp = self.start 
            count=0
            while True:
                prev = temp
                temp = temp.next_node
                count+=1
                if count==k:
                    next1= temp.next_node
                    prev.next_node = next1 
                    next1.prev_node = prev
                    break
                    
d1= doublelinkedlist()
d1.insert_end(12)
d1.insert_end(45)
d1.insert_end(34)
d1.insert_beg(14)
d1.insert_beg(144)
d1.delete_k(2)
d1.traverse()
