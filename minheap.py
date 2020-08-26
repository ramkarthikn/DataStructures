class minheap:
    def __init__(self):
        self.heap=[]
    def get_parent(self,i):
        return (i-1)//2 
    def get_left(self,i):
        return 2*i+1 
    def get_right(self,i):
        return 2*i+2 
    def has_parent(self,i):
        return self.get_parent(i) >=0
    def has_left(self,i):
        return self.get_left(i) < len(self.heap)
    def right_has(self,i):
        return self.get_right(i) <len(self.heap)
    #code to insert data in heap
    def insert(self,item):
        self.heap.append(item)
        self.heapify_up(len(self.heap)-1)
    #the code to maintain the heap property above
    def heapify_up(self,i):
        while self.has_parent(i) and self.heap[i] < self.heap[self.get_parent(i)]:
            self.swap(i,self.get_parent(i))
            i= self.get_parent(i)
    # code to swap the node values in heap
    def swap(self,i,j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    #code to delete the node in heap
    def delete_max(self):
        if len(self.heap)==0:
            return -1 
        else:
            self.swap(0,len(self.heap)-1)
            self.heap.pop(len(self.heap)-1)
            self.heapify_down(0)
    #code to maintain the heap property when the top is delted 
    def heapify_down(self,i):
        while self.has_left(i):
            max_node = self.max_node_child(i)
            if max_node == -1:
                break 
            if self.heap[i] < self.heap[max_node]:
                self.swap(i,max_node)
                i = max_node
    #code to find the min child to which we need to replace data
    def max_node_child(self,i):
        if self.has_left(i):
            left_child = self.get_left(i)
            if self.right_has(i):
                right_child = self.get_right(i)
                if self.heap[left_child] < self.heap[right_child]:
                    return left_child
                else:
                    return right_child
        else:
            return -1
    def print1(self):
        print(self.heap)
h1= minheap()
h1.insert(12)
h1.insert(23)
h1.insert(9)
h1.insert(7)
h1.insert(21)
h1.insert
h1.print1()

    

