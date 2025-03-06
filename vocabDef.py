class Vocab:
    def __init__(self, term:str, definition:str, priority:int):
        self.term = term
        self.definition = definition
        self.priority = priority
        self.age = 0
        
    def reassemble(self, line:list[str,str,int]):
        #params = line.split("|")
        self.term = line[0]
        self.definition = line[1]
        self.priority = line[2]
        
    def __lt__(self, other):
        if isinstance(other, Vocab):
            return self.priority < other.priority
        return NotImplemented    
        
        
    def __eq__(self, other):
        if isinstance(other, Vocab):
            return self.priority == other.priority
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Vocab):
            return self.priority > other.priority
        return NotImplemented
    
    def strInfo(self)->str:
        info = self.term + "|" + self.definition + "|" + str(self.priority)
        return info