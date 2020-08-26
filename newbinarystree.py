class node:
    def __init__(self,value):
        self.data= value 
        self.left= None 
        self.right= None
        self.parent= None
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
            else:
                self._insert(data,cur_node.left)
        elif data> cur_node.data:
            if cur_node.right == None:
                cur_node.right = node(data)
                cur_node.right.parent= cur_node
            else:
                self._insert(data,cur_node.right)
        else:
            return -1 
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
    def inorder(self,cur_node):
        if self.root==None:
            return -1 
        else:
            if cur_node.left!=None:
                self.inorder(cur_node.left)
            print(cur_node.data)
            if cur_node.right!=None:
                self.inorder(cur_node.right)
b2= bintree()
b2.insert(12)
b2.insert(34)
b2.insert(9)
b2.insert(11)
b2.insert(35)
b2.insert(33)
b2.insert(23)
b2.inorder(b2.root)



