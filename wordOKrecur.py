def wordOK(word, hand):
    if word == "": #an empty word can be made with any hand
        return True
    elif word[0] not in hand:
        return False
    #elif hand.values() == 0: #that's what I figured, check for both 0 values and {}
      #  return False               #but this must be not it because condition 2 covers this
    else:
        hand[word[0]] = hand.get(word[0], 0) - 1 # minus one letter in hand
        word = word[1:] # minus first letter
        return wordOK(word, hand)
        
        
        ####    
#test
wordList = ['tree', 'swamp', 'apples', 'apple', 'pizzaz']
hand = {'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}
hand3 = {'a': 0, 'p': 0, 's': 0, 'e': 0, 'l': 0}
hand1 = {}
word = 'apples'
print wordOK(word, hand)