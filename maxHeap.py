class Vocab:
    def __init__(self, term, definition, priority):
        self.term = term
        self.definition = definition
        self.priority = priority
        self.n = 0
    #TODO: Define Vocab object comparison. does __eq__ handle-less than and greater-than as well?
    
        
class MaxHeap:
    #TODO: Test Heap and make sure building/maintaining heap works
    #TODO: Define methods for maintaining priority between vocab items. Implementation may not be present here
    def __init__(self):
        self.heap = []
        
    def formatVocab(input) -> list[Vocab]:
        A = []
        for n in range(len(input)):
            currTerm = Vocab(input[0], input[1], 0)
            A.append(currTerm)
        return A
    
    def heapify(self, i):
        larget = i
        l = 2 * i + 1
        r = 2 * i + 2
        
        if l < self.n and self.heap[l].priority > self.heap[i].priority: #May need to rework this logic to run properly
            largest = l
        if r < self.n and self.heap[r] > self.heap[i]:
            largest = r
            
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(self.n, largest)
            
    def heapSort(self):   
        for i in range(self.n - 1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.heapify(i)
            
        
    def buildHeap(self, vocabList):
        self.heap = self.formatVocab(vocabList)
        self.n = len(self.heap)
        self.heapify(0)
        
        