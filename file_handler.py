from vocabDef import Vocab

"""
This class handles the file I/O for the heap/priority queue.
In the future, this could be used for handling other things.
However for the task at hand, the scope of implementation does not
exceed the heap ADT.
"""
class FileHandler:
    def __init__(self, fileName:str):
        self.fileName = fileName
    

    def bufferContents(self) -> list[str]:
        file = open(self.fileName, "r", encoding="utf8")
        lines = file.readlines()
        for line in lines:
            splitStr = line.rsplit("|")
            line = splitStr[0] + "|" + splitStr[1]
        file.close()
        return lines
        
    #Function for handling the initial write for program start.
    def initialWrite(self, initList:list[Vocab]):
        file = open(self.fileName, "a+", encoding="utf8")
        for i in range(len(initList)):
            word = initList[i].strInfo()
            file.write(word + "\n")
        
        file.close()
    
    #TODO: Write function to handle precise updating of a given word's priority
    def updatePriority(self, targetTerm:Vocab, newPriority:int):
        updated = False
        contentBuffer = self.bufferContents() 
        for i in range(len(contentBuffer)):
            if contentBuffer[i].find(targetTerm.strInfo()) != -1: #Replace with try/except
                editBuffer = contentBuffer[i].split("|")
                editBuffer[2] = newPriority
                word = Vocab("NaN", "NaN", -1)
                word.reassemble(editBuffer)
                contentBuffer[i] = word.strInfo() + "\n"
                updated = True
        
        if updated: print("targetTerm found, update successful.")
        else: print("targetTerm not found, update failed.")
        file = open(self.fileName, "w", encoding="utf8")        
        file.writelines(contentBuffer)