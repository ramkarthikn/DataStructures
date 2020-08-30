class graph:
    def __init__(self):
        self.graph= dict()
    def add_vertice(self,data):
        self.graph[data]= list()
    def add_edges(self,u,v):
        if u in self.graph and v in self.graph:
            self.graph[u].append(v)
g1= graph()
g1.add_vertice(18)
g1.add_vertice(19)
g1.add_vertice(78)
g1.add_vertice(67)
g1.add_vertice(76)
g1.add_edges(18,19)
g1.add_edges(78,18)
print(g1.graph)
    
