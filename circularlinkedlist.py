class node:
    def __init__(self,item):
        self.data= item
        self.next = None 
class circularlist:
    def __init__(self):
        self.start = None
    def insert_beg(self,data):
        newnode= node(data)
        newnode.next = self.start 
        if self.start==None:
            newnode.next=newnode
            self.start = newnode
        else:
            temp=self.start 
            while temp.next!=self.start:
                temp = temp.next
            temp.next= newnode
            self.start= newnode
    def insert_end(self,data):
        newnode = node(data)
        temp= self.start
        if self.start==None:
             newnode.next= newnode
             self.start= newnode 
        else:
            while temp.next!=self.start:
                temp=temp.next 
            temp.next= newnode
            newnode.next = self.start
    def length(self):
        temp=self.start
        count=0 
        while temp:
            temp=temp.next
            count+=1 
            if temp==self.start:
                break
        return count
    def insert_k(self,data,k):
        newnode = node(data)
        if k==0:
          self.insert_beg(data)
        elif k==self.length():
            self.insert_end(data)
        else:
            temp = self.start 
            count=0
            while True:
                present= temp
                temp=temp.next 
                count+=1 
                if count==k:
                    present.next= newnode
                    newnode.next= temp
                    break
    def traverse(self):
        temp=self.start
        while temp:
            print(temp.data)
            temp= temp.next 
            if temp==self.start:
                break
    def delete_end(self):
        if self.start == None:
            return -1 
        else:
            temp=self.start
            while temp.next!=self.start:
                prev= temp
                temp=temp.next
            temp.next = None 
            prev.next = self.start
    def delete_beg(self):
        if self.start==None:
            return None
        else:
            temp= self.start.next 
            self.start.next = None
            self.start= temp
    def delete_k(self,k):
        if k==0:
            self.delete_beg()
        elif k==self.length():
            self.delete_end()
        else:
            temp= self.start 
            count=0
            while True:
                prev= temp
                temp=temp.next 
                count+=1 
                if count==k:
                    prev= temp.next 
                    break
li = circularlist()
li.insert_beg(1)
li.insert_beg(2)
li.insert_beg(3)
li.insert_end(12)
li.insert_end(124)
li.insert_k(56,2)
li.traverse()
li.delete_k(3)
li.traverse()