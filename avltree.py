class node:
    def __init__(self,value):
        self.data= value 
        self.left= None 
        self.right= None
        self.parent= None
        self.height = 1 
class bintree:
    def __init__(self):
        self.root = None 
    def insert(self,value):
        newnode= node(value)
        if self.root== None:
            self.root= newnode 
        else:
            self._insert(value,self.root)
    def _insert(self,data,cur_node):
        if data< cur_node.data:
            if cur_node.left == None:
                cur_node.left= node(data)
                cur_node.left.parent= cur_node
                self.inspect_insertion(cur_node.left)

            else:
                self._insert(data,cur_node.left)
        elif data> cur_node.data:
            if cur_node.right == None:
                cur_node.right = node(data)
                cur_node.right.parent= cur_node
                self.inspect_insertion(cur_node.right)
            else:
                self._insert(data,cur_node.right)
        else:
            return -1 
    def inspect_insertion(self,cur_node,path=[]):
        if cur_node.parent==None:return 
        path = [cur_node]+path 
        left_height= self.get_height(cur_node.parent.left)
        right_height= self.get_height(cur_node.parent.right)
        if abs(left_height-right_height)>1:
            path= [cur_node.parent]+ path 
            self.rebalance(path[0],path[1],path[2])
            return 
        new_height= 1 + cur_node.height
        if new_height> cur_node.parent.height:
            cur_node.parent.height= new_height
        self.inspect_insertion(cur_node.parent)
    def inspect_deletion(self,cur_node):
        if cur_node==None: return
        left_height= self.get_height(cur_node.left)
        right_height= self.get_height(cur_node.right)
        if abs(left_height-right_height)>1:
            x= self.tallest_child(cur_node)
            y= self.tallest_child(x)
            self.rebalance(cur_node,y,x)
        self.inspect_deletion(cur_node.parent)
    def rebalance(self,z,y,x):
        if y==z.left and x==y.left:
            self.right_rotation(z)
        if y==z.left and x==y.right:
            self.left_rotation(y)
            self.right_rotation(z)
        if y==z.right and x==y.right:
            self.left_rotation(z)
        if y==z.right and x==y.left:
            self.right_rotation(y)
            self.left_rotation(z)
    def right_rotation(self,z):
        sub_root= z.parent 
        y= z.left
        t3= y.right 
        y.left= z
        z.parent= y 
        z.left = t3
        if t3!=None: t3.oarent= z 
        y.parent = sub_root
        if y.parent.left ==z:
            y.parent.left=y
        else:
            y.parent.right = y 
        z.height= 1+ max(self.get_height(z.left),self.get_height(z.right))
        y.height= 1+max(self.get_height(y.left), self.get_height(y.right))
    def left_rotation(self,z):
        sub_root= z.parent 
        y= z.right
        t3= y.left  
        y.right= z
        z.parent= y 
        z.right = t3
        if t3!=None: t3.oarent= z 
        y.parent = sub_root
        if y.parent.left ==z:
            y.parent.left=y
        else:
            y.parent.right = y 
        z.height= 1+ max(self.get_height(z.left),self.get_height(z.right))
        y.height= 1+max(self.get_height(y.left), self.get_height(y.right))
    def find(self,data):
        if self.root!=None:
            return self._find(data,self.root)
        else:
            return None
    def _find(self,data,cur_node):
        if data>  cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        if data== cur_node.data:
            return cur_node
    def delete_value(self,value):
        return self.delete_node(self.find(value))
    def delete_node(self,node):
        def min_value_node(n):
            current= n 
            while current.left!= None:
                current= current.left
            return current
        def num_children(n):
            num_children=0 
            if n.left!=None:
                num_children+=1 
            if n.right!=None:
                num_children+=1 
            return num_children
        node_parent= node.parent 
        node_children= num_children(node)
        if node_children ==0:
            if node_parent.left==node:
                node_parent.left=None 
            else:
                node_parent.right= None
        if node_children==1:
            if node.left!=None:
                child= node.left
            else:
                child= node.right
            if node.parent.left== node:
                node_parent.left=child
            else:
                node_parent.right=child 
        if node_children==2:
            successor = min_value_node(node.right)
            node.data= successor.data
            self.delete_node(successor)
            return 
        if node_parent!=None:
            node_parent.height= 1+ max(self.get_height(node_parent.left),self.get_height(node_parent.right))
            self.inspect_deletion(node_parent)
    def inorder(self,cur_node):
        if self.root==None:
            return -1 
        else:
            if cur_node.left!=None:
                self.inorder(cur_node.left)
            print(cur_node.data)
            if cur_node.right!=None:
                self.inorder(cur_node.right)
    def tallest_child(self,cur_node):
        left_height= self.get_height(cur_node.left)
        right_height=self.get_height(cur_node.right)
        if left_height>=right_height:
            return cur_node.left_height
        else:
            return cur_node.right_height
    def get_height(self,cur_node):
        if cur_node==None:
            return 0 
        return cur_node.height
b2= bintree()
b2.insert(12)
b2.insert(34)
b2.insert(9)
b2.insert(11)
b2.insert(35)
b2.insert(33)
b2.insert(23)
b2.insert(62)
b2.delete_value(35)
b2.inorder(b2.root)