import random
import logger
import time

# main
def run_game():

    keep_playing = 'y'
    words = ["fizzy", "crane", "jerky", "heart", "teach", "blank", "fetch", "ghost", 
             "dress", "preen", "shine", "scare", "smear", "slack", "spear", "climb", 
             "pluck", "learn", "drown", "aimed", "guess", "words", "value", "cover",
              "range", "cliff", "beads", "drone" ]
    guess = []
    round_guess = ""
    counter = 0
    start_time = time.time()

    while(keep_playing == "y" ):
        
        word = list(words[random.randint(0,len(words))])
        #print("[Debug] word is " + displayGuess(word))
        guess = GenerateWord(5)

        guessed = False
        while(not guessed):
            print(displayGuess(guess))

            if(displayGuess(guess).lower() == displayGuess(word)):
                print("You win!")
                guessed = True
                end_time = time.time()
                logger.log("[Wordle] User guessed the word " + displayGuess(word).capitalize() + " in " + logger.time_format(end_time - start_time) 
                           + " in " + str(counter) + " guesses!")
                counter = 0
            elif(counter > 5):
                print("Out of guesses!")
                print("Word was " + displayGuess(word).capitalize() + "!")
                end_time = time.time()
                logger.log("[Wordle] User failed to guess the word " + displayGuess(word).capitalize() + " in " + logger.time_format(end_time - start_time) + "!")
                counter = 0
                break
            else:
                counter = counter + 1
                round_guess = input("Enter a 5-letter guess. (" + str(counter) + "/6) \n> ")
                while(not validate(round_guess)):
                    round_guess = input("Must be a 5-letter guess. \n> ")

                guess = check_guess(round_guess, word, guess)   

        keep_playing = input("Would you like to keep playing? (y/n)\n> ").lower()
        while(keep_playing != "y" and keep_playing != "n"):
            keep_playing = input("Please enter a valid response. \n> ").lower() 

# Generates a blank map with all values covered up    
# n = size of grid, n x n        
def GenerateWord(n):
    arr = ['_ ' for space in range(n)]
    return arr

# makes sure word is 5 letters long. not checking to make sure words are actually words.
def validate(input):
    try:
        if (len(input) > 0 and len(input) <= 5):
            return True
        else:
            raise Exception
        
    except:
        return False

# checks to see if guess is any close.
# lc letter: letter is in word, but wrong spot
# uc letter: right letter, right spot
# _ : letter is not in word
def check_guess(round_guess, word, guess):
    count = 0
    for letter in round_guess:
        if(word[count] == letter):
            guess[count] = letter.capitalize()
        elif(letter in word):
            guess[count] = letter
        count = count + 1
    return guess

# prints words from arrays in a neat, readable way
def displayGuess(word):
    string = ""
    for letter in word:
        string = string + letter
    return string