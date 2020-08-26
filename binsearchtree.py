class node:
    def __init__(self,value):
        self.data= value 
        self.left= None 
        self.right= None 
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
            else:
                self._insert(data,cur_node.left)
        elif data> cur_node.data:
            if cur_node.right == None:
                cur_node.right = node(data)
            else:
                self._insert(data,cur_node.right)
        else:
            return -1 
    def find(self,data):
        if self.root:
            is_found = self._find(data,self.root)
            if is_found:
                return True
            return False  
        else:
            return None
    def _find(self,data,cur_node):
        if data>  cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        if data== cur_node.data:
            return True
b2= bintree()
b2.insert(12)
b2.insert(34)
b2.insert(45)
b2.insert(11)
print(b2.find(15))



