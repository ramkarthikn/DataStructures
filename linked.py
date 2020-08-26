class node:
    def __init__(self,data):
        self.data= data 
        self.next= None 
class linkedlist:
    def __init__(self):
        self.start= None 
    def insert_end(self,item):
        newnode= node(item)
        if self.start==None:
            self.start= newnode 
        else:
            temp= self.start
            while temp.next!=None:
                temp = temp.next
            temp.next= newnode 
    def traverse(self):
        temp = self.start
        while temp!=None:
            print(temp.data)
            temp= temp.next
    def insert_beg(self,item):
        newnode = node(item)
        if self.start==None:
             self.start= newnode 
        else:
            temp= self.start
            newnode.next=temp 
            self.start= newnode
    def insert_k(self,item,k):
        newnode= node(item)
        if  k==0:
            self.insert_beg(item)
        else:
            temp = self.start 
            count=0 
            while True:
                previous= temp
                temp= temp.next
                count+=1
                if count==k:
                    previous.next= newnode
                    newnode.next= temp
                    break
    def delete_end(self):
        temp= self.start 
        while temp.next!=None:
            previous= temp
            temp= temp.next 
        previous.next= None
    def delete_beg(self):
        if self.start==None:
            return -1 
        else:
            temp= self.start.next 
            self.start= temp 
    def delete_k(self,k):
        if k==0:
            self.delete_beg()
        else:
            temp= self.start 
            count= 0 
            while True:
                previous= temp
                temp= temp.next
                count+=1 
                if count==k:
                    previous.next= temp.next
                    break  
li =linkedlist()
li.insert_end(1)
li.insert_end(2)
li.insert_beg(3)
li.insert_beg(4)
li.insert_k(56,0)
li.insert_k(45,2)
li.delete_k(1)
li.traverse()