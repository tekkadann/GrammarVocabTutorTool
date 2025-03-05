class Term:
    word = "NaN"
    definition = "Nan"
    strength = 0
    
class Heap:
    
    def __init__(self):
        self.heap = []
        
    def parent(self, i):
        return (i-1)/2
    
def heapify() -> list[int]:
    