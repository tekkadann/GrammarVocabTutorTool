class Vocab:
    def __init__(self, term, definition, priority):
        self.term = term
        self.definition = definition
        self.priority = priority
        self.n = 0
        
    def strInfo(self)->str:
        info = self.term + "|" + self.definition + "|" + self.priority + "\n"
        return info
        
    #TODO: Define Vocab object comparison. does __eq__ handle-less than and greater-than as well?a