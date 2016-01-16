import time
import string
from random import randint
from sys import exit


def startGame():
    print "Welcome to the Maze of Sphinx.\n"
    print "You are locked in a Maze."
    print "The only way escape this maze is to answer Sphinx's riddles correctly.\n"
    print "Here comes the first riddle...\n"
    riddleOne()

def riddleOne():
    print "\t Riddle # 1\n"
    print "Mary’s father has 5 daughters – Nana, Nene, Nini, Nono. What is the fifth daughters name?"

    mary = raw_input("> ")

    if "mary" or "Mary" in mary:
        print "Correct....Moving on to riddle two...\n"
        riddleTwo()
    else:
        print "The answer is Mary!"
        dead()

def riddleTwo():
    print "\t Riddle # 2\n"

    noStair = raw_input("In a one-story pink house, there was a pink person, a pink cat, a pink fish, a pink computer, a pink chair, a pink table, a pink telephone, a pink shower– everything was pink!\nWhat color were the stairs?\n:")

    if "no" or "No" in noStair:
        print "Correct....Moving on to riddle three...\n"
        riddleThree()
    else:
        print "There are no stairs! It is a one-story house!"
        dead()

def riddleThree():
    print "\t Riddle # 3\n"

    man = raw_input("What is the creature that walks on four legs in the morning, two legs at noon and three in the evening?\n:")

    if "man" or "Man" or "men" or "Men" in man:
        print "Correct....\nYou are out of this maze...!"
        gateOne()
    else:
        print "It is 'Man...'"
        dead()

def dead():
    print "You didn't answer the riddle correctly..."
    time.sleep(0.2)
    print "You starved to death in the maze..."
    time.sleep(0.2)
    tryAgain()

def tryAgain():
    choice = raw_input("Do you want to try again?\n[no]\n[yes]\n:")

    if "no" or "No" or "NO" or "nO" in choice:
        sys.exit()
    elif "yes" or "Yes" or "YEs" or "yES" or "yEs" or "YeS" or "YES" in choice:
        startGame()
    else:
        print "I didn't understand you. Please type [yes] or [no] again.\n:"
        tryAgain()

while True:
    startGame()
