import random
import string

VOWELS
CONSONANTS
HAND_SIZE

SCRABBLE_LETTERS_VALUES

WORDLIST_FILENAME

loadWords()
getFrequencyDict(sequence)
getWordScore(word,n)
displayHand(hand)
dealHand(n)
updateHand(hand, word)
isValidWord(word, hand, wordList)
calculateHandlen(hand)
playHand(hand, wordList, n)
playGame(wordList)

compChooseWord(hand, wordList, n) -> str or None
compPlayHand(hand, wordList, n) -> None

---------------------

main
    wordList = loadWords()
    n = HAND_SIZE
    playGame(wordList)
        dealHand(n) VOWELS, CONSONANTS -> List: hand
        playHand(hand, wordList, n) -> None
            calculateHandlen(hand) -> int (max n)
            displayHand(n) -> List: 'hand'
            isValidWord(word, hand, wordList) -> Boolean
            getWordScore(word, n) -> int: score
            updateHand(hand, word) -> List: 'hand'
              