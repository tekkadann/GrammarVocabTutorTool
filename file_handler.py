from vocabDef import Vocab

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
        preWrittenVocab = self.bufferContents()
        file = open(self.fileName, "w+", encoding="utf8")
        for i in range(len(initList)):
            word = initList[i].strInfo()
            if word not in preWrittenVocab: 
                file.write(word)
                print("New term detected: " + word + ". Written to file.")
        
        file.close()
    
    #TODO: Write function to handle precise updating of a given word's priority
    def updatePriority(): 
        return