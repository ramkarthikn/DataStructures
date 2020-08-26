class Node:
    def __init__(self,item):
        self.data= item 
        self.left= None 
        self.right= None 
class Binary:
    def __init__(self):
        self.root=None 
    def insert(self,item):
        newnode= Node(item)
        if self.root==None:
            self.root= newnode
            return 
        else:
            queue=[]
            queue.append(self.root)
            while True:
                node = queue.pop(0)
                if node.left!= None and node.right!=None:
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    if node.left== None:
                        node.left= newnode 
                        queue.append(node.left)
                    else:
                        node.right= newnode
                        queue.append(node.right)
                    break
    def inorder(self,node):
        if self.root == None:
            print("tree empty")
        else:
            if node.left!=None:
                self.inorder(node.left)
            print(node.data)
            if node.right!=None:
                self.inorder(node.right)
    def delete(self,key):
        if self.root==None:
            return None 
        if self.root.left==None and self.root.right==None:
            if self.root.data==key:
                return None
        key_node=None 
        q=[]
        q.append(self.root)
        while len(q):
            temp= q.pop(0)
            if temp.data == key:
                key_node= temp
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        if key_node:
            x= temp.data 
            self.deleteDeepest(self.root,temp)
            key_node.data=x 
    def deleteDeepest(self,root,d_temp):
        q=[]
        q.append(root)
        while len(q):
            temp= q.pop(0)
            if temp is  d_temp:
                temp=None
            if temp.right:
                if temp.right == d_temp:
                    temp.right=None
                else:
                    q.append(temp.right) 
            if temp.left:
                if temp.left ==d_temp:
                    temp.left=None
                else:
                    q.append(temp.left)

b1= Binary()
b1.insert(12)
b1.insert(14)
b1.insert(24)
b1.insert(34)
b1.delete(14)
b1.inorder(b1.root)



