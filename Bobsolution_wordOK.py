import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "C:\Users\Ann\Documents\GitHub\WordGame\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList


def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    assert word == word.lower()
    
    score= 0
    #lookup values in dictionary scrabble letters
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter]
    score *= len(word)
    
    #extra 50 points for using all letters
    if len(word) == n:     
        score += 50
    
    assert 0 <= score <= 442
    return score

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    
    if word not in wordList:
        return False
    for letter in word:
        if word.count(letter) > hand.get(letter, 0):
            return False
    else:
        return True

def wordOK(word, hand):
    if word == "": #an empty word can be made with any hand
        return True
    elif word[0] not in hand:
        return False
    elif hand 
    else:
        word = word[1:]
        wordOK(word, hand)

def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0
    newScore =0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None
    
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        for letter in word:
            if word == '':
                return True
            trueList.append(word.count(letter) > hand.get(letter, 0))
            if all(trueList):
                print trueList
                break
            
            else:
                print word
                # Find out how much making that word is worth
                newScore = getWordScore(word, n)
                print newScore
                # If the score for that word is higher than your best score
                maxScore = max(newScore, maxScore)
                
                # Update your best score, and best word accordingly
                if getWordScore(word, n) == maxScore:
                    bestWord = word

    # return the best word you found.
    return bestWord
    
####    
#test
wordList = ['tree', 'swamp', 'apples', 'apple', 'pizzaz']
hand = {'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}
print compChooseWord(hand, wordList, 6)
