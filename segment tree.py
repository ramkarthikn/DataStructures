li=[1, 2, 3, 4, 5, 6, 7,8]
tree = [0]*2*len(li)
n= len(li)
def gentree(a):
    for i in range(n):
        tree[n+i] = a[i]
    for i in range(n-1,0,-1):
        tree[i] = tree[2*i] + tree[2*i+1]
    return tree 
print(gentree(li))
def updateValue(index,data):
    tree[index+n]= data 
    index+=n 
    i = index 
    while i>1:
        tree[i//2]= tree[i]+ tree[i+1]
        i=i//2 
    return tree 
print(updateValue(3,5))
def querysum(l,r):
    sum=0
    l+=n 
    r+=n 
    while l<r:
        if l&1 >0 :
            sum+=tree[l]
            l+=1 
        if r&1 >0:
            r-=1 
            sum+=tree[r]
        l=l//2 
        r=r//2
    return sum 
print(querysum(1,3)) 
            
