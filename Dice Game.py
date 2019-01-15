# Dicegame

import random
import time


# Display program info.

print("Hello! Thank you for playing my dice game.")
print("Here's some useful info you'll need before starting.")
print("The default username and password are 'user' and 'pass'")
print("When given a Y/N prompt, please use uppercase letters.")
print("That should be everything, the program will begin in 5 seconds.")
time.sleep(5)

print("\n")

# Create Login System.
username = ("user")
password = ("pass")


def userLogin():
    askUser = input("Please enter your username: ")
    if askUser == username:
        print("\n")
        print("Username correct.")
        print("\n")

    else:
        print("\n")
        print("Username incorrect. Please try again")
        time.sleep(0.25)
        userLogin()

def passLogin():
    askPass = input("Please enter your password: ")
    if askPass == password:
        print("\n")
        print("Password correct. The game will now begin.")
        time.sleep(1)

    else:
        print("Password incorrect. Please try again")
        time.sleep(0.25)
        passLogin()

print("\n")

userLogin()
passLogin()

askNamep1 = input("Player 1, what is your name? ")
askNamep2 = input("Player 2, what is your name? ")

f=open("Player1_Data.txt", "a")
f.write(askNamep1 + "\n")
f.close()

f=open("Player2_Data.txt", "a")
f.write(askNamep2 + "\n")
f.close()





def rollDicep2():
        Dice1 = int(random.randint(1,6))
        Dice2 = int(random.randint(1,6))
        score = Dice1 + Dice2

        evenScore = score + 10
        oddScore = score - 5
        
        print(askNamep2 + " you rolled a: " + str(Dice1))
        print(askNamep2 + " you rolled a: " + str(Dice2))
        print(askNamep2 + " your score for this round is: " + str(score))

        if Dice1 == Dice2: 
                    print("You rolled a double! Rolling bonus dice.")
                    time.sleep(0.25)

                    Bonusdice = int(random.randint(1,6))

                    print(askNamep2 + " your bonus roll is: " + str(Bonusdice))
                    bonusScore = Dice1 + Dice2 + Bonusdice
                    print(askNamep2 + " your score for this round is: " + str(bonusScore))
                
        if score == int(2):
                    print("You rolled an even number. +10 points")
                    score = evenScore
                    print(askNamep2 + " your score for this round is: " + str(score))
                    
        elif score == int(4):
                    print("You rolled an even number. +10 points")
                    score = evenScore
                    print(askNamep2 + " your score for this round is: " + str(score))
                    
        elif score == int(6):
                    print("You rolled an even number. +10 points")
                    score = evenScore
                    print(askNamep2 + " your score for this round is: " + str(score))
                    
        elif score == int(8):
                    print("You rolled an even number. +10 points")
                    score = evenScore
                    print(askNamep2 + " your score for this round is: " + str(score))
                    
        elif score == int(10):
                    print("You rolled an even number. +10 points")
                    score = evenScore
                    print(askNamep2 + " your score for this round is: " + str(score))
                    
        elif score == int(12):
                    print("You rolled an even number. +10 points")
                    score = evenScore
                    print(askNamep2 + " your score for this round is: " + str(score))

        else:
            print("Aww, too bad, you rolled an odd number -5 points")
            score = oddScore
            print(askNamep2 + " your score for this round is: " + str(score))

        if score == 0:
                    print(askNamep2 + " your score is already 0, it can't get any lower.")
                    score = 0

        f=open("Player2_Data.txt", "a")
        f.write(str(score) + "\n")
        f.close()






def rollDicep1():
        dice1 = int(random.randint(1,6))
        dice2 = int(random.randint(1,6))
        score = dice1 + dice2

        evenScore = score + 10
        oddScore = score - 5

        
        print(askNamep1 + " you rolled a: " + str(dice1))
        print(askNamep1 + " you rolled a: " + str(dice2))
        print(askNamep1 + " your score for this round is: " + str(score))

        if dice1 == dice2: 
                    print("You rolled a double! Rolling bonus dice.")
                    time.sleep(0.25)

                    bonusDice = int(random.randint(1,6))

                    print(askNamep1 + " your bonus roll is: " + str(bonusDice))
                    Bonusscore = dice1 + dice2 + bonusDice
                    print(askNamep1 + " your score for this round is: " + str(Bonusscore))
                
        if score == int(2):
                    print("You rolled an even number. +10 points")
                    score = evenScore
                    print(askNamep1 + " your score for this round is: " + str(score))
                    
        elif score == int(4):
                    print("You rolled an even number. +10 points")
                    score = evenScore
                    print(askNamep1 + " your score for this round is: " + str(score))
                    
        elif score == int(6):
                    print("You rolled an even number. +10 points")
                    score = evenScore
                    print(askNamep1 + " your score for this round is: " + str(score))
                    
        elif score == int(8):
                    print("You rolled an even number. +10 points")
                    score = evenScore
                    print(askNamep1 + " your score for this round is: " + str(score))
                    
        elif score == int(10):
                    print("You rolled an even number. +10 points")
                    score = evenScore
                    print(askNamep1 + " your score for this round is: " + str(score))
                    
        elif score == int(12):
                    print("You rolled an even number. +10 points")
                    score = evenScore
                    print(askNamep1 + " your score for this round is: " + str(score))

        else:
            print("Aww, too bad, you rolled an odd number -5 points")
            score = oddScore
            print(askNamep1 + " your score for this round is: " + str(score))

        if score == 0:
                    print(askNamep1 + " your score is already 0, it can't get any lower.")
                    score = 0

        f=open("Player1_Data.txt", "a")
        f.write(str(score) + "\n")
        f.close()


startRoll = input(askNamep1 + " would you like to roll your dice? Y/N: ")
if startRoll ==("Y"):
    rollDicep1()

startRollp2 = input(askNamep2 + " would you like to roll your dice? Y/N: ")
if startRollp2 ==("Y"):
    rollDicep2()

startRollr2 = input(askNamep1 + " would you like to roll your dice? Y/N: ")
if startRollr2 ==("Y"):
    rollDicep1()

startRollp2r2 = input(askNamep2 + " would you like to roll your dice? Y/N: ")
if startRollp2r2 ==("Y"):
    rollDicep2()


startRollr3 = input(askNamep1 + " would you like to roll your dice? Y/N: ")
if startRollr3 ==("Y"):
    rollDicep1()

startRollp2r3 = input(askNamep2 + " would you like to roll your dice? Y/N: ")
if startRollp2r3 ==("Y"):
    rollDicep2()

startRollr4 = input(askNamep1 + " would you like to roll your dice? Y/N: ")
if startRollr4 ==("Y"):
    rollDicep1()

startRollp2r4 = input(askNamep2 + " would you like to roll your dice? Y/N: ")
if startRollp2r4 ==("Y"):
    rollDicep2()

startRollr5 = input(askNamep1 + " would you like to roll your dice? Y/N: ")
if startRollr5 ==("Y"):
    rollDicep1()

startRollp2r5 = input(askNamep2 + " would you like to roll your dice? Y/N: ")
if startRollp2r5 ==("Y"):
    rollDicep2()


f=open("Player1_Data.txt", "r")
printScore = f.readline()
print(printScore)
f.close()



