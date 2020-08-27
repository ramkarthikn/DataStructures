class node:
    def __init__(self,item):
        self.data= item
        self.next = None
        self.prev= None 
class circularlist:
    def __init__(self):
        self.start = None
    def insert_end(self,data):
        newnode =node(data)
        if self.start==None:
            self.start= newnode
            newnode.next=newnode
        else:
            temp = self.start 
            while temp.next!=self.start:
                temp=temp.next 
            temp.next= newnode
            newnode.prev = temp 
            newnode.next= self.start
    def insert_beg(self,item):
        newnode= node(item)
        if self.start==None:
            self.start = newnode
            newnode.next= newnode
        else:
            temp=self.start 
            while temp:
                temp= temp.next 
                if temp==self.start:
                    break
            newnode.next= self.start 
            self.start = newnode
            temp.next = self.start
    def insert_k(self,data,k):
        newnode = node(data)
        if k==0:
            self.insert_beg(data)
        elif k==self.length():
            self.insert_end(data)
        else:
            temp= self.start
            count=0
            while True:
                previous= temp
                temp=temp.next 
                count+=1 
                if count==k:
                    newnode.next= temp 
                    newnode.prev = previous
                    previous.next = newnode
                    temp.prev= newnode
                    break

    def length(self):
        count=0
        if self.start ==None:
            return None
        else:
            temp = self.start 
            while temp:
                temp=temp.next
                count+=1
                if temp== self.start:
                    break
            return count 
                  
    def traverse(self):
        temp=self.start 
        while temp:
            print(temp.data)
            temp= temp.next 
            if temp ==self.start:
                break
    def delete_end(self):
        if self.start == None:
            return -1 
        else:
            temp = self.start 
            while temp.next!=self.start:
                prev= temp
                temp = temp.next
            prev.next = self.start 
            temp.prev = None 
            temp.next = None
    def delete_beg(self):
        if self.start== None:
            return -1 
        else:
            first= self.start 
            temp= self.start.next 
            self.start = temp
            first.next= None  
    def delete(self,k):
        if k==0:
            self.delete_beg()
        elif k==self.length():
            self.delete_end()
        else:
            temp = self.start 
            count=0 
            while True:
                prev = temp
                temp= temp.next
                count+=1 
                if count==k:
                    prev.next= temp.next 
                    temp.next.prev= prev 
                    temp.next= None 
                    temp.prev= None
                    break 
             
             
li = circularlist()
li.insert_beg(123)
li.insert_beg(124)
li.insert_end(89)
li.insert_k(45,2)
li.delete(3)
li.traverse()