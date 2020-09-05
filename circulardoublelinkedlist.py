class node:
    def __init__(self,data):
        self.data= data
        self.prev= None   
        self.next= None
class linkedlist:
    def __init__(self):
        self.start = None
    def insert_beg(self,data):
        newnode= node(data)
        if self.start==None:
           self.start=newnode
           newnode.next= newnode
        else:
            temp=self.start 
            while temp.next!=self.start:
                temp=temp.next 
            newnode.next=self.start 
            self.start=newnode
            temp.next=self.start
    def insert_end(self,data):
        newnode= node(data)
        if self.start==None:
            self.start= newnode
        else:
            temp=self.start 
            while temp.next!=self.start:
                temp=temp.next 
            temp.next=newnode
            newnode.next= self.start
            newnode.prev=temp
    def insert_at(self,k,data):
        newnode = node(data)
        if k==0:
            self.insert_beg(data)
        elif k==self.length():
            self.insert_end(data)
        else:
            temp=self.start 
            count=0
            while True:
                prev= temp
                temp=temp.next 
                count+=1 
                if count==k:
                    prev.next=newnode
                    newnode.prev= prev 
                    newnode.next=temp 
                    temp.prev= newnode 
                    break
    def delete_end(self):
        if self.start==None:
            return -1 
        else:
            temp=self.start 
            while temp.next!=self.start:
                prev=temp
                temp=temp.next
            prev.next=self.start 
            temp.next =None 
            temp.prev=None
    def delete_beg(self):
        if self.start==None:
            return -1 
        else:
            temp=self.start 
            while temp.next!=self.start:
                temp= temp.next
            first= self.start 
            temp1 = self.start.next 
            self.start= temp1
            first.next=None
            temp1.prev= None
            temp.next= self.start
    def delete_k(self,k):
        if k==0:
            self.delete_beg()
        elif k==self.length():
            self.delete_end()
        else:
            temp=self.start 
            count=0
            while True:
                preve= temp 
                temp=temp.next 
                count+=1 
                if count==k:
                    preve.next=temp.next 
                    temp.next.prev= preve
                    temp.next= None 
                    temp.prev= None 
                    break
    def length(self):
        count=0
        temp=self.start
        while True:
            temp=temp.next
            count+=1
            if temp==self.start:
                break 
        return count
    def traverse(self):
        temp=self.start 
        while True:
            print(temp.data)
            temp=temp.next
            if temp == self.start:
                break
li = linkedlist()
li.insert_beg(90)
li.insert_beg(56)
li.insert_end(78)
li.insert_at(2,23)
li.insert_at(2,56)
li.insert_end(90)
li.traverse()
li.delete_k(2)
print("")
li.traverse()

