from vocabDef import Vocab
from file_handler import FileHandler
from maxHeap import MaxHeap
import random

"""
IMPORTANT DATA TYPES:
    term_and_def: List[term, definition]
    vocabBank: List[term_and_def]
    grammarBank: List[str] NOTE: this str is a grammar term    
"""

#Split each term into two parts, term and definition, and then add those parts to an array to represent our "dictionary"
def createVocabBank(viList) -> list[Vocab]: 
    wordBank = [] #Declare array for storing words
    for n in range(len(viList)):
        currLine:str = viList[n]
        term_and_def = currLine.split("|") #Split string at definied split point for each term. split() returns a list at split point
        term_and_def[1] = term_and_def[1].rstrip("\n") #Remove newline from the definition for easy formatting
        currTerm = Vocab(term_and_def[0], term_and_def[1], 100)
        wordBank.append(currTerm)
    return wordBank

#Do the same as createVocabBank but for grammr, which only has the term. May add definition/explanation in the future
def createGrammarBank(grList) -> list[str]:
    wordBank = [Vocab]
    for n in range(len(grList)):
        currLine = grList[n]
        term = currLine.rstrip("\n")
        wordBank.append(term)
    return wordBank

def numericalInput(text) -> int:
    inValidate = False
    while not inValidate: #TODO: Create function that receives input and autoconverts to int/handles sanitization.
        var = input(text) #TODO: Input sanitization. Case handling for non-numerical input.
        try:
            var = int(var)
            inValidate = True
        except:
            print("Input was not numerical, please try again.")
    return var

def calculatePriorirty(currTerm:Vocab, lvl:int)->int:
    k = 0.1 #This is a scaling factor for determining the magnitue of adjustment. 0.1 allows for a max adjustment of 50% of curr priority
    currPriority = int(currTerm.priority)
    newPriority = int(currPriority * (1 + k * (5 - lvl)))
    return newPriority

def vocabTest(n, vocabBank:list[Vocab]):
    #For numTerms times, select a random word from the word bank, after user input, print definition.
    for i in range (0, n):
        RNG_V = random.choice(vocabBank)
        print("ROUND: " + str(i + 1))
        print("Current Term: " + RNG_V.term)
        input("When ready to continue, press ENTER") #Jank use of input() to wait for userinput to continue execution. Find potential better way
        print("Definition: " + RNG_V.definition + "\n\n")

def vocabTestHeap(n, vocabBank:MaxHeap):
    #TODO: fix calculatePriority to drop priority when 4 or 5 is entered.
    for i in range (0, n):
        RNG_V:Vocab = vocabBank.getTop()
        print("ROUND: " + str(i + 1))
        print("Current Term: " + RNG_V.term)
        input("When ready to continue, press ENTER") #Jank use of input() to wait for userinput to continue execution. Find potential better way
        print("Definition: " + RNG_V.definition + "\n")
        knowledgeCheck = numericalInput("On a scale of 1 - 5, how well did you know the term?\n")
        updateVal = calculatePriorirty(RNG_V, knowledgeCheck)
        handlerWalter.updatePriority(RNG_V, updateVal) #Handle updating priority in the Heap file. This way, priorities are saved to the permanent storage before being updated in memory.
        RNG_V.priority = updateVal #Update priority as per user response
        vocabBank.popTop()
                
#TODO: Find a better way to incorporate grammar as a study method
def vocabAndGrammarTest(n, vocabBank:list[Vocab], grammBank):
    for i in range (0, n):
        RNG_V = random.choice(vocabBank)
        RNG_G = random.choice(grammBank)
        print("ROUND: " + str(i + 1))
        print("Current Term: " + RNG_V.term + " Vocab: " + RNG_G)
        input("When ready to continue, press ENTER") #Jank use of input() to wait for userinput to continue execution. Find potential better way
        print("Definition: " + RNG_V.definition + "\n\n")
        
#ENTRY POINT HERE!
#Open vocab list and read into array
vocabInput = open("vocab_list.txt", "r", encoding="utf8")
viList = vocabInput.readlines()
vocabInput.close()


grammarInput = open("grammar_list.txt", "r", encoding="utf8")
grList = grammarInput.readlines()
grammarInput.close()

vocabBank = createVocabBank(viList) #Creates vocab word bank

handlerWalter = FileHandler("VocabHeap.txt") #Declare File Handler for the Heap
HEAPFILEDATA = []
vocabHeap = MaxHeap()
if handlerWalter.exists(): 
    HEAPFILEDATA = handlerWalter.bufferContents()
    print("Heap file detected, reading data now.")
    for i in range(len(HEAPFILEDATA)):
        assembleBuffer = HEAPFILEDATA[i].split("|")
        currTerm = Vocab("NaN", "NaN", -1)
        currTerm.reassemble(assembleBuffer)
        vocabHeap.add(currTerm) 
    print("Heap file read complete.")
else: 
    handlerWalter.initialWrite(vocabBank) #Do an initial write of the Heap if the file DOES NOT EXIST.
    HEAPFILEDATA = handlerWalter.bufferContents()
    vocabHeap = MaxHeap()
    print("First time heap file creation successful. Populating session heap.")
    for i in range(len(HEAPFILEDATA)):
        vocabHeap.add(HEAPFILEDATA[i])
    print("Initial heap creation successful.")
grammBank = createGrammarBank(grList) #Creates grammar word bank

exit = 1
while exit == 1:
    #Take user input to create desired study environment.
    numTerms = numericalInput("How many terms would you like to study?\n")
    heapFlag = numericalInput("Would you like to enable Smart Study Mode? (Enable use of HeapSorted priority terms.)\n")
    grammFlag = numericalInput("Would you like to add grammar terms as well?\nNOTE: type 1 for yes, 0 for no\n")
    if grammFlag > 1: grammFlag = 1 #Catch case where user input unexpected input
    if grammFlag == 0 and heapFlag == 0:
        vocabTest(numTerms, vocabBank)
    elif grammFlag == 0 and heapFlag == 1:
        vocabTestHeap(numTerms, vocabHeap)
    #TODO: Implement vocabTestHeap which works in tandem with grammar
    else:
        vocabAndGrammarTest(numTerms, vocabBank, grammBank)
    exit = numericalInput("Would you like to continue?\nNOTE: 1 for yes, 0 for no\n")
    print()