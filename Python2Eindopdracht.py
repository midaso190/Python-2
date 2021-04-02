doorgaan = True
import random
guessedletters = ""
guessedl = ''
woordlijst = ["koelkast", "kamer", "laptop", "letter", "scherm", "driehoek", "geluid", "coderen", "mario", "slang", "gras", "hallo", "banaan", "appel", "brommer", "leraar", "stoel", "zwembad", "klok", "kaas", "stofzuiger", "auto",]
woord = ''
guess = "nothing yet"
wordlist = list("")
guesses = 0

def randomword():
    global woord
    global wordlist
    global guessedletters
    global guessedl
    
    wordlist = list("")
    woord = random.choice(woordlijst)
    guessedletters = ''
    guessedl = ''
    for letter in woord:
        wordlist.append("-")

def wordcheck():
    global wordstri
    global aantalkeergeraden
    global guessedletters
    global guesses
    
    print(wordlist)
    guess = input("Raad een letter ")
    letterpos = 0
    guesstr = list(guess)
    guesses = guesses + 1
    if guess == woord:
        print("Goed greaden! Het woord was "+woord+". En je hebt "+str(guesses)+" keer erover gedaan om het te raden!")
        if input("Wil je nog een keer proberen? ") == "nee":
            print("Tot ziens!")
            return
        else:
            start()
    for letter in woord:
        letterpos = letterpos + 1
        if letter == guess:
            guessedletters = guessedletters + guess
            wordlist[letterpos - 1] = letter
    print(guessedl)

def start():
    global guesses
    guesses = 0
    randomword()
    while True:
        wordcheck()
start()