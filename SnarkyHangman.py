'''
Created on Nov 21, 2557 BE

@author: Nisakorn Valyasevi
'''

import random
import string

def load_lines(filename):
    """
    read words from specified file and return a list of
    strings, each string is one line of the file
    """
    lines = []
    f = open(filename)
    for line in f.readlines():
        line = line.strip()
        lines.append(line)
    return lines
def get_words(filename, wordlength = 5):
    """
    returns a list of words having a specified length from
    the file whose name is filename.
    default length is 5 (if parameter not specified)
    """
    lines = load_lines(filename)
    wlist = [w for w in lines if len(w) == wordlength]
    return wlist


def process_letter(guessed,secret,letter):  #this function  processed the letter the user chooses and checks if it is in the "secret" word or not
    for num in range(len(secret)):
        if letter == secret.lower()[num]:
            guessed[num] = secret[num]
        if letter not in secret.lower():
            return False
    return guessed

def snarkydict(letter, secret, words):  #this function creates a dictionary where all the keys are all the possible locations of the letter that 
    dict= {}                                    #was chosen and the values of those corresponding keys are 
    lis = [word for word in words if len(word) == len(secret)] #all the possible words with the chosen letters in the corresponding position(s) to the key
    for x in lis:
            guessed = ["_"] * len(secret)
            for no in range(len(secret)):
                if x[no] not in string.ascii_letters:
                    guessed[no] = x[no]
            y = process_letter(guessed, x, letter)
            a = ",".join(guessed)
            if process_letter(guessed, x, letter) == False:
                    if a not in dict:
                        dict[a] = []
                        dict[a] += [x]
                    else:
                        dict[a] += [x]
            else:
                    y = process_letter(guessed, x, letter)
                    b = ",".join(y)
                    if b not in dict:
                        dict[b] = []
                        dict[b] += [x]
                    else:
                        dict[b] += [x]
    return dict

def chooseSnarky(letter, secret, words, guessed): #function changes the secret word by randomly choosing a word from 
    templateDict = snarkydict(letter, secret, words)   #the longest dictionary value from the dictionary given by the snarkydict function
    for k in templateDict.keys():                      
        if len(templateDict[k]) == max([len(v) for v in templateDict.values()]):
                secret = random.choice(templateDict[k])
                words = templateDict[k]
    return secret

def updateGuessed(guessed, secret):
        for no in range(len(secret)):
            if secret[no] not in string.ascii_letters:
                guessed[no] = secret[no]
        return guessed


def printInfo(guessed, numguess, start, guesses, letter):
    print guessed
    print "misses left:", numguess - start
    print "guesses so far:", guesses
    print "guess letter:", letter

    
def user(): #this is the function that is the main program that runs the game
    print "which theme (movies, famouspeople, worldcountries, or lowerwords)?",
    theme = raw_input()
    print "what's the word length?>",
    wordlen = int(raw_input())
    words = get_words(theme,wordlen)
    one = random.choice(words)
    secret = one
    guessed = ["_"] * len(secret)
    guesses = ""
    print "How many guesses to hanging?>",
    numguess = int(raw_input())
    start = 0                       # it will check to see if all the letters in the word have been guessed yet and also how many guesses are left
    while start <= numguess:
        if "".join(guessed) == secret:
                print "CONGRATULATIONS! YOU WON! YAY~ XD"
                return
        else:
            
            if start == numguess:
                print "you are hung :'(, secret word is", secret
                return
            print "guess letter",
            letter = raw_input()
            secret = chooseSnarky(letter, secret, words, guessed)
            guessed = updateGuessed(guessed, secret)
            if process_letter(guessed, secret, letter) == False:
                print "(secret word:", secret, ")", "# possible words:", len(words)
                guesses += str(letter) + " "
                guesses.strip()
                start += 1
                printInfo(guessed, numguess, start, guesses, letter)
                print "no", letter
            if process_letter(guessed, secret, letter) != False:
                print "(secret word:", secret, ")", "# possible words:", len(words)
                guessed = process_letter(guessed, secret,letter)
                printInfo(guessed, numguess, start, guesses, letter)


if __name__ == "__main__":
    user()