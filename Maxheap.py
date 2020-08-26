class heap1():
    def __init__(self):
        self.heap= [] 
    def get_parent(self,i):
        return (i-1)//2 
    def get_left_child(self,i):
        return 2*i+1 
    def get_right_child(self,i):
        return 2*i+2 
    def has_parent(self,i):
        return self.get_parent(i) >=0 
    def has_left_child(self,i):
        return self.get_left_child(i) < len(self.heap)
    def has_right_child(self,i):
        return self.get_right_child(i) <len(self.heap)
    def swap(self,i,j):
        self.heap[i],self.heap[j] = self.heap[j], self.heap[i]
    def insert(self,key):
        self.heap.append(key)
        self.heapify_up(len(self.heap)-1)
    def heapify_up(self,i):
        while self.has_parent(i) and self.heap[i]> self.heap[self.get_parent(i)]:
            self.swap(i, self.get_parent(i))
            i= self.get_parent(i)
    def print1(self):
        print(self.heap)

    def delete_root(self):
        if len(self.heap)==0:
            return -1 
        self.swap(0,len(self.heap)-1)
        self.heap.pop()
        self.heapify_down(0)
    def heapify_down(self,i):
        while self.has_left_child(i):
            max_node_ind= self.get_max_ind(i)
            if max_node_ind ==-1:
                break 
            if self.heap[i]< self.heap[max_node_ind]:
                self.swap(i,max_node_ind)
                i=max_node_ind
            else:
                break
    def get_max_ind(self,i):
        if self.has_left_child(i):
            left_c= self.get_left_child(i)
            if self.has_right_child(i):
                right_c= self.get_right_child(i)
                if self.heap[left_c] > self.heap[right_c]:
                    return left_c
                else:
                    return right_c
        else:
            return -1 


h1= heap1()
h1.insert(12)
h1.insert(23)
h1.insert(9)
h1.insert(7)
h1.insert(21)
h1.print1()