class graph:
    def __init__(self):
        self.graph= dict()
    def add_vertice(self,data):
        self.graph[data]= list()
    def add_edges(self,u,v):
        if u in self.graph and v in self.graph:
            self.graph[u].append(v)


    
