import random

#Split each term into two parts, term and definition, and then add those parts to an array to represent our "dictionary"
def createVocabBank(viList) -> list[str]: 
    wordBank = [] #Declare array for storing words
    for n in range(len(viList)):
        currLine = viList[n]
        term_and_def = currLine.split("|") #Split string at definied split point for each term. split() returns a list at split point
        term_and_def[1] = term_and_def[1].rstrip("\n") #Remove newline from the definition for easy formatting
        wordBank.append(term_and_def)
    return wordBank

#Do the same as createVocabBank but for grammr, which only has the term. May add definition/explanation in the future
def createGrammarBank(grList) -> list[str]:
    wordBank = []
    for n in range(len(grList)):
        currLine = grList[n]
        term = currLine.rstrip("\n")
        wordBank.append(term)
    return wordBank

def vocabTest(n, vocabBank):
    #For numTerms times, select a random word from the word bank, after user input, print definition.
    for i in range (0, n):
        RNG_V = random.choice(vocabBank)
        print("ROUND: " + str(i + 1))
        print("Current Term: " + RNG_V[0])
        input("When ready to continue, press ENTER") #Jank use of input() to wait for userinput to continue execution. Find potential better way
        print("Definition: " + RNG_V[1] + "\n\n")
        
#TODO: Find a better way to incorporate grammar as a study method
def vocabAndGrammarTest(n, vocabBank, grammBank):
    for i in range (0, n):
        RNG_V = random.choice(vocabBank)
        RNG_G = random.choice(grammBank)
        print("ROUND: " + str(i + 1))
        print("Current Term: " + RNG_V[0] + " Vocab: " + RNG_G)
        input("When ready to continue, press ENTER") #Jank use of input() to wait for userinput to continue execution. Find potential better way
        print("Definition: " + RNG_V[1] + "\n\n")
        
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
#ENTRY POINT HERE!
#Open vocab list and read into array
vocabInput = open("vocab_list.txt", "r", encoding="utf8")
viList = vocabInput.readlines()
vocabInput.close()


grammarInput = open("grammar_list.txt", "r", encoding="utf8")
grList = grammarInput.readlines()
grammarInput.close()

vocabBank = createVocabBank(viList) #Creates vocab word bank
grammBank = createGrammarBank(grList) #Creates grammar word bank

exit = 1
while exit == 1:
    #Take user input to create desired study environment.
    numTerms = numericalInput("How many terms would you like to study?\n")
    
    grammFlag = numericalInput("Would you like to add grammar terms as well?\nNOTE: type 1 for yes, 0 for no\n")
    if grammFlag > 1: grammFlag = 1 #Catch case where user input unexpected input
    if grammFlag == 0:
        vocabTest(numTerms, vocabBank)
    else:
        vocabAndGrammarTest(numTerms, vocabBank, grammBank)
    exit = numericalInput("Would you like to continue?\nNOTE: 1 for yes, 0 for no\n")
    print()