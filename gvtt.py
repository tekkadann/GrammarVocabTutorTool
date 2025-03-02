import random

def createVocabBank(viList) -> list[str]:
    #Split each term into two parts, term and definition, and then add those parts to an array to represent our "dictionary"
    wordBank = [] #Declare array for storing words
    for n in range(len(viList)):
        currLine = viList[n]
        term_and_def = currLine.split("|") #Split string at definied split point for each term. split() returns a list at split point
        term_and_def[1] = term_and_def[1].rstrip("\n") #Remove newline from the definition for easy formatting
        wordBank.append(term_and_def)
    return wordBank

#Open vocab list and read into array
vocabInput = open("vocab_list.txt", "r", encoding="utf8")
viList = vocabInput.readlines()
vocabInput.close()

"""
grammarInput = open("grammar_list.txt", "r", encoding="utf8")
grList = grammarInput.readlines()
grammarInput.close()
"""
vocabBank = createVocabBank(viList) #Creates vocab word bank

numTerms = input("How many terms would you like?\n") #TODO: Input sanitization. Case handling for non-numerical input.
numTerms = int(numTerms)

#For numTerms times, select a random word from the word bank, after user input, print definition.
for i in range (0, numTerms):
    RNG = random.choice(vocabBank)
    print("ROUND: " + str(i + 1))
    print("Current Term: " + RNG[0])
    input("When ready to continue, press ENTER") #Jank use of input() to wait for userinput to continue execution. Find potential better way
    print("Definition: " + RNG[1] + "\n\n")
    
