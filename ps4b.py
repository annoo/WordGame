from ps4a_max import *
import time
#
#
# Problem #6: Computer chooses a word
#
#


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
        if isValidWord(word, hand, wordList):
                # Find out how much making that word is worth
                newScore = getWordScore(word, n)
            
                # If the score for that word is higher than your best score
                maxScore = max(newScore, maxScore)
                
                    # Update your best score, and best word accordingly
                if getWordScore(word, n) == maxScore:
                    bestWord = word

    # return the best word you found.
    return bestWord

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    totalScore = 0

    # Display the hand
    print "Computer's current hand: ", 
    displayHand(hand)
        
    # Computer chooses a word
    word = compChooseWord(hand, wordList, n)
    
    #as long as the computer can play
    while compChooseWord(hand, wordList, n) != None:
   
        # Tell the computer how many points the word earned
        score = getWordScore(word, n)
        totalScore += score
        print("'%s' earned %i points.") % (word, score)
        # Update the hand 
        hand = updateHand(hand, word)
        # Display the hand
        print "Computer's current hand: ", 
        displayHand(hand)
    
    # Game is over. Tell the total score
    print("No more possibilities. Total score: %i points") % totalScore

#
# Problem #8: Playing a game
#
#
#create helpfuntion: computer or user
def playUserOrComp():
    """
    Determines who gets to play: computer or user
    returns: True for user
    returns: False for computer
    """    
    answer = raw_input("Press 'u' if you want to play. Press 'c' for the computer. ")
    answer = answer.lower()
    
    if answer == 'u':
        return True
    elif answer == 'c':
        return False
    else:
        print("Input unclear")
        playUserOrComp() 
    
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    while True:
        #ask the user to input 'n' 'r' or 'e'
        newReplayExit = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        newReplayExit = newReplayExit.lower()
        
        #if 'n' deal a new hand
        if newReplayExit == 'n':
            hand = dealHand(n)
            user = playUserOrComp()
            if user == True: 
                playHand(hand, wordList, n)
            else: 
                compPlayHand(hand, wordList, n)
        
        #if 'r' replay last hand
        elif newReplayExit == 'r':
            try:
                user = playUserOrComp()
                if user == True:
                    playHand(hand, wordList, n)
                else:
                    compPlayHand(hand, wordList, n)
            except UnboundLocalError:
                print "You cannot replay a game on your first try."
                ##?? how can this be more correct? it comes at wrong time!n
            else:
                break 
        
        #if 'e' exit the game
        elif newReplayExit == 'e':
            break

        #all other inputs
        else:
            print("Input unclear.")
##?? what's the better solution put the def at the end again or while function?c
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


