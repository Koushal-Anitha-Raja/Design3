#creating a class called minheap which defines the minheap property
class Minheap:
    #creating a array in constructor
    def __init__(self):
        #creating a heap array where i will do the operations
        self.heap=[]
    def getMin(self):
        #returns the minimum value in the heap (the first value)
        return self.heap[0]
     
    #bubbleup is recursive function for checking the values everytime it is inserted
    def BubbleUp(self,index):
        #for insert we need to perform bubbleup where it performs follows
        parentIndex=(index-1)//2
        
        #checking whether it is going out of bound
        if parentIndex<0:
            return
        #until the parentindex is small 
        if self.heap[parentIndex]<self.heap[index]:
            return
        #swapping the value if it is new element is minimum
        self.heap[parentIndex],self.heap[index]=self.heap[index],self.heap[parentIndex]
        self.BubbleUp(parentIndex)
        
        
    def BubbleDown(self,index):
        #bubbledowning the leftindex
        leftchild=2*index+1
        #bubbledowning the leftindex
        rightchild=2*index+2
        #the element that has to swapped is temp
        temp=index
        #checking whether my left child is going after the leaf node and the left child value is lesser 
        if leftchild<len(self.heap) and self.heap[temp]>self.heap[leftchild]:
            temp=leftchild
            
            
         #checking whether my right child is going after the leaf node and the right child value is lesser    
        if rightchild<len(self.heap) and self.heap[temp]>self.heap[rightchild]: 
            temp=rightchild
        
        
        if temp==index:
            return
        #swap the new element    
        self.heap[temp],self.heap[index]=self.heap[index],self.heap[temp]
        self.BubbleDown(temp)
        
    def insert(self,key):
        #inserting the value in the heap
        self.heap.append(key)
        #we are bubbleing up till last index 
        self.BubbleUp(len(self.heap)-1)
        
        
        
    def extractMin(self):
        #returning the first element by swapping it with the last element
        self.heap[0],self.heap[-1]=self.heap[-1],self.heap[0]
        #returning the minimum value
        temp=self.heap.pop()
        #bubble down the vlaue before returning
        self.BubbleDown(0)
        return temp
        
        
    def size(self): 
        #returns the lenght of the heap array
        return len(Self.heap)
    
    
    
    
"""    
h = Minheap()
h.insert(5);
h.insert(3);
h.insert(17);
h.insert(11);
h.insert(79);
h.insert(19);
h.insert(6);
h.insert(25);
h.insert(9);
print(h.heap)
print(h.getMin())
for i in range (len(h.heap)):
    print(h.extractMin())
"""