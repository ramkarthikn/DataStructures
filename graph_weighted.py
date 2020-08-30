from collections import OrderedDict 
class node:
    def __init__(self,key):
        self.data= key 
        self.neighbourlist= OrderedDict()
        self.neigh= OrderedDict()
class graph:
    def __init__(self):
        self.verticelist= OrderedDict()
        self.verticecount= 0
    def add_node(self,data):
        self.verticecount+=1
        ver= node(data)
        self.verticelist[data] = ver 
    def get_node(self,data):
        return self.verticelist[data]
    def addedge(self,start,dest,weigh=0):
        if start not in self.verticelist:
            self.add_node(start)
        if dest not in self.verticelist:
            self.add_node(dest)
        self.verticelist[start].neighbourlist[dest]= weigh
        self.verticelist[dest].neighbourlist[start]= weigh
    def vertices(self):
        return self.verticelist 
g1= graph()
g1.add_node(12)
g1.add_node(13)
g1.add_node(14)
g1.addedge(12,13,5)
g1.addedge(12,14,6)
print(g1.verticelist)
print(g1.get_node(12).neighbourlist)
