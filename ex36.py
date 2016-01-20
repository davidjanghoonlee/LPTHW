# coding: utf-8

import time
import string
from random import randint
from sys import exit


def startGame():
    print "Welcome to the Maze of Sphinx.\n"
    print "You are locked in a room now."
    print "To Escape: answer Sphinx's riddle correctly and open the door to start.\n"
    print "Here comes the riddle...\n"
    print "_______________________________________________________________"
    riddleOne()


def tryAgain():
    wantRetry = raw_input("Do you want to try again?\n[no]\n[yes]\n>")

    if wantRetry == "no" :
        exit()
    elif wantRetry=="yes":
        print "_______________________________________________________________"
        startGame()
    else:
        print "I didn't understand you. Please type [yes] or [no] again.\n>"
        print "_______________________________________________________________"
        tryAgain()


def riddleOne():
    print "_______________________________________________________________"
    print "\t Riddle # 1\n"
    print "Mary's father has 5 daughters: Nana, Nene, Nini, Nono. What is the fifth daughters name?"

    mary = raw_input("> ")

    if mary == "Mary":
        print "Correct....Moving on to the next stage...\n"
        time.sleep(0.5)
        print "_______________________________________________________________"
        print "\nWhen you went out the gate, there were four paths."
        choiceOne()
    elif mary == "mary":
        print "Correct....Moving on to the next stage...\n"
        time.sleep(0.5)
        print "_______________________________________________________________"
        print "\nWhen you went out the gate, there were four paths."
        choiceOne()
    else:
        print "Wrong!"
        print "_______________________________________________________________"
        dead()


def dead():
    print "You didn't answer the riddle correctly..."
    time.sleep(0.2)
    print "You starved to death in the maze..."
    time.sleep(0.2)
    print "_______________________________________________________________"
    tryAgain()


def choiceOne():
    print "[   ]    [     ]   [   ]"
    print "[   ]    [     ]   [   ]"
    print "[ 1 ]    [  2  ]   [ 3 ]"
    print "[   ]____[     ]___[   ]"
    print "[________ (YOU) _______]"
    print "         |     |        "
    print "         |  4  |        "
    print "\nYou are at section #A"

    choice = int(input("Which path do you take?[1/2/3/4]\n> "))

    if choice ==  1:
        print "_______________________________________________________________"
        gotoB()
    elif choice == 2:
        print "_______________________________________________________________"
        gotoD()
    elif choice == 3:
        print "_______________________________________________________________"
        gotoC()
    elif choice == 4:
        print "_______________________________________________________________"
        print "That's where you first started from."
        time.sleep(0.5)
        print "Let's try again!\n"
        time.sleep(0.5)
        print "_______________________________________________________________"
        choiceOne()
    else:
        print "Invalid choice: Try Again.\n"
        print "_______________________________________________________________"
        choiceOne()

def gotoB():
    print "         [  2  ]            "
    print "         [     ]            "
    print "_________[     ]___________ "
    print "                           "
    print "  1       (YOU)        3   "
    print "_________       ___________"
    print "         [     ]            "
    print "         [     ]            "
    print "         [  4  ]            "
    print "\nYou are at Section #B"
    time.sleep(0.2)
    print "\nThere are four paths."

    choice = int(input("Which path do you take?[1/2/3/4]\n> "))

    if choice == 1:
        print "_______________________________________________________________"
        goToBeginningTrap()
    elif choice == 2:
        print "Oh man! You were caught in a swirling flame and died!"
        time.sleep(0.4)
        print "_______________________________________________________________"
        tryAgain()
    elif choice ==3:
        print "_______________________________________________________________"
        gotoD()
    elif choice ==4:
        print "_______________________________________________________________"
        choiceOne()
    else:
        print "Invalid choice. Try again."
        time.sleep(0.1)
        print "_______________________________________________________________"
        gotoB()

def goToBeginningTrap():
    print "Woops! You were caught in a go-to-beginning trap!"
    print "Sorry! Starting from the beginning!"
    time.sleep(0.1)
    print "."
    time.sleep(0.1)
    print "."
    time.sleep(0.1)
    print "."
    print "Starting Again from the First Gate!"
    time.sleep(0.4)
    print "_______________________________________________________________"
    riddleOne()

def gotoC():
    print "         [  2  ]            "
    print "         [     ]            "
    print "_________[     ]___________ "
    print "                           "
    print "  1       (YOU)        3   "
    print "_________       ___________"
    print "         [     ]            "
    print "         [     ]            "
    print "         [  4  ]            "
    print "\nYou are at section #C"
    time.sleep(0.1)
    print "\nThere are four paths."

    choice = int(input("Which path do you take?[1/2/3/4]\n> "))

    if choice == 1:
        time.sleep(0.1)
        print "_______________________________________________________________"
        gotoD()
    elif choice == 2:
        time.sleep(0.1)
        print "_______________________________________________________________"
        gotoE()
    elif choice ==3:
        time.sleep(0.1)
        print "_______________________________________________________________"
        thornTrap()
    elif choice ==4:
        time.sleep(0.1)
        print "_______________________________________________________________"
        choiceOne()
    else:
        print "Invalid choice. Try again."
        time.sleep(0.1)
        print "_______________________________________________________________"
        gotoC()

def thornTrap():
    print "WOOPS! You are caught in a thorn trap!\n"
    time.sleep(0.1)
    print "You bled to death..."
    time.sleep(0.1)
    print "_______________________________________________________________"
    tryAgain()


def gotoD():
    print "         [  2  ]            "
    print "         [     ]            "
    print "_________[     ]___________ "
    print "                           "
    print "  1       (YOU)        3   "
    print "_________       ___________"
    print "         [     ]            "
    print "         [  4  ]            "
    print "         [     ]            "
    print "\nYou are at section #D"
    time.sleep(0.1)
    print "\nThere are four paths."

    choice = int(input("Which path do you take?[1/2/3/4]\n> "))

    if choice == 1:
        time.sleep(0.1)
        print "_______________________________________________________________"
        gotoB()
    elif choice == 2:
        time.sleep(0.1)
        print "_______________________________________________________________"
        gotoF()
    elif choice ==3:
        time.sleep(0.1)
        print "_______________________________________________________________"
        gotoC()
    elif choice ==4:
        time.sleep(0.1)
        print "_______________________________________________________________"
        choiceOne()
    else:
        print "Invalid choice. Try again."
        time.sleep(0.1)
        print "_______________________________________________________________"
        gotoD()


def gotoE():
    print "         [  2   ]"
    print "         [      ]"
    print "_________[      ]"
    print "                ]"
    print "  1       (YOU) ]"
    print "_________       ]"
    print "         [      ]"
    print "         [      ]"
    print "         [  3   ]"
    print "\nYou are at section #E"
    time.sleep(1)
    print "\nThere are three paths."

    choice = int(input("Which path do you take?[1/2/3]\n> "))

    if choice == 1:
        time.sleep(0.1)
        print "_______________________________________________________________"
        gotoF()
    elif choice == 2:
        time.sleep(0.1)
        print "_______________________________________________________________"
        meetKerberos()
    elif choice ==3:
        time.sleep(0.1)
        print "_______________________________________________________________"
        gotoC()
    else:
        print "Invalid choice. Try again."
        time.sleep(0.1)
        print "_______________________________________________________________"
        gotoE()


def meetKerberos():
    print "On the way to section G, you met a three-headed dog Kerberos!"
    print "You can only one of the three things."
    print "1> Fight the dog."
    print "2> Run Away."
    print "3> Persuade the dog."

    choice = int(input("What would you do?[1/2/3]\n> "))
    if choice == 1:
        print "Since you were unarmed, you lost to the dog!"
        print "You were eaten by the dog and died."
        print "_______________________________________________________________"
        tryAgain()
    elif choice == 2:
        print "You were slower than the dog."
        print "You were caught and killed by the dog."
        print "_______________________________________________________________"
        tryAgain()
    elif choice == 3:
        print "You succeeded in persuading the dog."
        print "You passed him and reached section #G"
        print "_______________________________________________________________"
        gotoG()




def gotoG():
        print "[   ]              [   ]"
        print "[   ]              [   ]"
        print "[ 1 ]              [ 2 ]"
        print "[   ]______________[   ]"
        print "[________ (YOU) _______]"
        print "         |     |        "
        print "         |  3  |        "
        print "\nYou are at section #G"

        choice = int(input("Which path do you take?[1/2/3]\n> "))

        if choice == 1:
            print "_______________________________________________________________"
            print "Congratulations!!!!!!!!!\nYou escaped!"
            print "_______________________________________________________________"
            tryAgain()
        elif choice == 2:
            print "_______________________________________________________________"
            arrowTrap()
        elif choice == 3:
            print "_______________________________________________________________"
            gotoE()
        else:
            print "Invalid choice. Try again."
            print "_______________________________________________________________"
            gotoG()


def gotoF():
    print "         [  2  ]            "
    print "         [     ]            "
    print "_________[     ]___________ "
    print "                           "
    print "  1       (YOU)        3   "
    print "_________       ___________"
    print "         [     ]            "
    print "         [     ]            "
    print "         [  4  ]            "
    print "\nYou are at section #F"

    choice = int(input("Which path do you take?[1/2/3/4]\n> "))

    if choice ==  1:
        print "_______________________________________________________________"
        fireTrap()
    elif choice == 2:
        print "_______________________________________________________________"
        knifeTrap()
    elif choice == 3:
        print "_______________________________________________________________"
        gotoE()
    elif choice == 4:
        print "_______________________________________________________________"
        gotoD()
    else:
        print "Invalid choice: Try Again.\n"
        gotoF()


def knifeTrap():
    print "Oh no!!!!!!!!!!You were caught in a chop-your-head-off trap!!!!"
    print "\tYou died."
    print "_______________________________________________________________"
    tryAgain()


def fireTrap():
    print "Hot!!Hot!!You were caught in a flame!!"
    print "You burned to death."
    print "_______________________________________________________________"
    tryAgain()


def arrowTrap():
    print "Pshhhhhh!! You were caught in an arrow trap!!!"
    print "You were shot by an arrow in the head and died."
    print "_______________________________________________________________"
    tryAgain()

while True:
    print "_______________________________________________________________"
    startGame()
