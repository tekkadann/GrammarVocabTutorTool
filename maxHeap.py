from vocabDef import Vocab

class MaxHeap:
    #TODO: Test Heap and make sure building/maintaining heap works
    #TODO: Define methods for maintaining priority between vocab items. Implementation may not be present here
    def __init__(self):
        self.heap = []
        
    def add(self, item):
        self.heap.insert(0, item)
        n = len(self.heap)
        self.heapify(n,0)
    
    def heapify(self, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        
        if l < n and self.heap[l] > self.heap[i]: #May need to rework this logic to run properly
            largest = l
        if r < n and self.heap[r] > self.heap[i]:
            largest = r
            
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(n, largest)
            
    def heapSort(self):   
        n = len(self.heap)
        
        for i in range(n // 2 - 1, -1 , -1):
            self.heapify(n,i)
            
        for i in range(n - 1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.heapify(i,0)
            
    def print(self):
        print(f"Top Element: {self.heap[0]}")