class Vocab:
    def __init__(self, term, definition, priority):
        self.term = term
        self.definition = definition
        self.priority = priority
        self.n = 0
        
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
        info = self.term + "|" + self.definition + "|" + self.priority + "\n"
        return info
        
    #TODO: Define Vocab object comparison. does __eq__ handle-less than and greater-than as well?a