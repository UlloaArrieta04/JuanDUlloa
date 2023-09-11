import random
def giveInstructions():
    print ('''\n Wordle is a word guessing game.
        you have 5 attempts 
        (C) means the letter is in the word and in the correct position
        (WP) means the letter is in the word but not in the correct position
        (NT) means the letter is not there in the word itself
        
            
        Best of Luck''')

words = ["this","five", "help", "lake", "pink", "cats"]


hiddenWord = random.choice(words)

attempt = 5

def checkWord(guess):
    
        if hiddenWord == guess:

            print("Congrats!! You did it.")
            return True
        else:
            result = ""
            for i, j in zip(guess, hiddenWord):  # zip allows to iterate between 2 arrays at the same time
            
                if i == j:
                    result = result + "(C)"
                elif i in hiddenWord:
                    result = result + "(WP)"
                else:
                    result = result + "(NT)"
            print(result)
            return False
        
def mainLoop ():
    attempt = 5
    while attempt > 0:
        guess = input("Guess a four lettered word: ")
        if checkWord(guess):
            break
        else:
            attempt -= 1
            print (f"You have {attempt} attempts left")
    else:
        print ("GAME OVER")
mainLoop()      
