# Date project started: 08/11/18
# Current date: 11/11/18
# Estimated Hour Count: 11hrs

import random
import time

# Login system redone 19/11/18

user = ("user")
passw = ("pass")
    
userName = input("Please enter your username: ")
if userName == user:
    print("\n")
    print("Username correct!")

else:
    print("Username incorrect!")
    quit()

print("\n")

passWord = input("Now please enter your password: ")
if passWord == passw:
    print("\n")
    print("User access granted! Game will now begin")
    print("\n")

else:
    print("Invalid Credentials")
    quit()

# Bug Update 19/11/18: Rewrote Login System. Bug fixed.

# Dice game rules / To Do list
# - Dice total added to score. - DONE
# - if total = even + 10 to score - DONE
# - if total = odd - 5 to score - DONE
# - if roll = double roll + 1 die and add roll to score - Simple if statement. Check if dice1 == dice2 and if yes then roll a third dice - DONE
# - Score != < 0 - DONE
# - Score after 5 rolls wins. - Learn while loops. Ask Debbie - IN PROGRESS 
# - if p1score == p2score roll 1 die and see who wins - Same as doubles. Just check scores after 5 rounds, and roll a third if need be. Repeat until win.
# Save all scores at the end of every round and add to finalScorep1 & p2 variable. Compare these and whichever is higher, print winners name and highest roll. 

# Ask both players for their names and store them locally to a file


p1Name = input("Player 1. Please enter your name: ")
p2Name = input("Player 2. Please enter your name: ")

f=open("Player1_Data.txt" , "a")
f.write(p1Name + "\n")
f.close()

f=open("Player2_Data.txt" , "a")
f.write(p2Name + "\n")
f.close()
print("\n")




# Ask if player 1 would like to roll their dice, and if yes, then roll them.
player1Roll = input(p1Name + " would you like to roll your dice? Y/N: ")
print("\n")


# Credit to StackOveflow. (Finding User later)
if player1Roll ==("Y"):
    for x in range (1):
        print ("You rolled a:")
        Dice1 = int(random.randint(1,6))
        print(Dice1)

    for x in range (1):
        print ("You rolled a:")
        Dice2 = int(random.randint(1,6))
        print(Dice2)


diceTotalp1 = Dice1 + Dice2

score = diceTotalp1

oddScore = int(score) - 5 

scoreZero = int(0)

evenScore = int(score) + 10

if score == int(2):
        print("You rolled an even number + 10 points!")
        score + 10
        score = evenScore
    
elif score == int(4):
         print("You rolled an even number + 10 points!")
         score + 10
         score = evenScore

elif score == int(6):
         print("You rolled an even number + 10 points!")
         score + 10
         score = evenScore

elif score == int(8):
         print("You rolled an even number + 10 points!")
         score + 10
         score = evenScore
         
elif score == int(10):
         print("You rolled an even number + 10 points!")
         score + 10
         score = evenScore
elif score == int(12):
         print("You rolled an even number + 10 points!")
         score + 10
         score = evenScore

elif score == int(3):
    print("Aww. You rolled an odd number. - 5 points.")
    score - 5
    score = oddScore

elif score == int(5):
    print("Aww. You rolled an odd number. - 5 points.")
    score - 5
    score = oddScore


elif score == int(7):
    print("Aww. You rolled an odd number. - 5 points.")
    score - 5
    score = oddScore

elif score == int(9):
    print("Aww. You rolled an odd number. - 5 points.")
    score - 5
    score = oddScore

     
elif score == int(11):
    print("Aww. You rolled an odd number. - 5 points.")
    score - 5
    score = oddScore

elif score == int(0):
    print("Your score is already 0! It can't go any lower. That's just mean")
    score + 0


if score == int(0):
    print("Your score is already 0! It can't go any lower. That's just mean")
    score + 0

# If Player 1 rolls double, roll a third dice and add it to their score
if Dice1 == Dice2:
    print("\n")
    print("Congratulations! You rolled a double. Here's a bonus roll.")
    for x in range (1):
        print("You rolled a:")
        bonusDice = int(random.randint(1,6))
        print(bonusDice)

        bonusScore = score + bonusDice
        score = bonusScore


        

# Note to self: Remind Debbie that 2 other methods were attempted before settling on if/elif.
# 1. Creating a variable that had all the even/odd numbers in them respectively, Outcome: Wouldn't work
# 2. On launch, writing a list of all the even/odd numbers to a local file. And then reading that local file where appropriate.
# Outcome: Could read and print the list, but could not read and apply them to an if statement.

# Shows the players what Player 1's final score for the round is     
print("\n")
print(p1Name + "'s score for round 1 is: " + str (score))
print("\n")

# Write Player 1's total for this round to a local file
f=open("Player1_Data.txt" , "a")
f.write(str (diceTotalp1) + ("\n"))
f.close()

# Write Player 1's final score for the round to a local file
f=open("Player1_Data.txt" , "a")
f.write(str (score) + ("\n")) 
f.close()

# Ask player 2 if they would like to roll, and if yes, then roll them.
player2Roll = input(p2Name + " would you like to roll your dice? Y/N: ")
print("\n")
if player2Roll ==("Y"):
    for x in range (1):
        print ("You rolled a:")
        dice1 = int(random.randint(1,6))
        print(dice1)

    for x in range (1):
        print ("You rolled a:")
        dice2 = int(random.randint(1,6))
        print(dice2)

diceTotalp2 = dice1 + dice2

scorep2 = diceTotalp2

oddScorep2 = int(scorep2) - 5 

scoreZerop2 = int(0)

evenScorep2 = int(scorep2) + 10

if scorep2 == int(2):
        print("You rolled an even number + 10 points!")
        scorep2 + 10
        scorep2 = evenScorep2
    
elif scorep2 == int(4):
         print("You rolled an even number + 10 points!")
         scorep2 + 10
         scorep2 = evenScorep2

elif scorep2 == int(6):
         print("You rolled an even number + 10 points!")
         scorep2 + 10
         scorep2 = evenScorep2

elif scorep2 == int(8):
         print("You rolled an even number + 10 points!")
         scorep2 + 10
         scorep2 = evenScorep2
         
elif scorep2 == int(10):
         print("You rolled an even number + 10 points!")
         scorep2 + 10
         scorep2 = evenScorep2
elif scorep2 == int(12):
         print("You rolled an even number + 10 points!")
         scorep2 + 10
         scorep2 = evenScorep2

elif scorep2 == int(3):
    print("Aww. You rolled an odd number. - 5 points.")
    scorep2 = oddScorep2

elif scorep2 == int(5):
    print("Aww. You rolled an odd number. - 5 points.")
    scorep2 = oddScorep2


elif scorep2 == int(7):
    print("Aww. You rolled an odd number. - 5 points.")
    scorep2 = oddScorep2

elif scorep2 == int(9):
    print("Aww. You rolled an odd number. - 5 points.")
    scorep2 = oddScorep2

     
elif scorep2 == int(11):
    print("Aww. You rolled an odd number. - 5 points.")
    scorep2 = oddScorep2

elif scorep2 == int(0):
    print("Your score is already 0! It can't go any lower. That's just mean")
    scorep2 + 0

# If Player 2 rolls a double, roll a bonus die and add it to their score.
if dice1 == dice2:
    print("\n")
    print("Congratulations! You rolled a double. Here's a bonus roll.")
    for x in range (1):
        print("You rolled a:")
        bonusDicep2 = int(random.randint(1,6))
        print(bonusDicep2)

        bonusScorep2 = scorep2 + bonusDicep2
        scorep2 = bonusScorep2

# Shows the players what Player 2's final score for the round is.
print("\n")
print(p2Name + "'s score for round 1 is: " + str (scorep2))

# Write Player 2's roll for this round to a local file
f=open("Player2_Data.txt" , "a")
f.write(str(diceTotalp2)+ ("\n"))
f.close()

f=open("Player2_Data.txt" , "a")
f.write(str(scorep2))
f.close()

print("\n")


# Ask if player 1 would like to roll their dice, and if yes, then roll them.
player1Roll = input(p1Name + " would you like to roll your dice? Y/N: ")
print("\n")


# Credit to StackOveflow. (Finding User later)
if player1Roll ==("Y"):
    for x in range (1):
        print ("You rolled a:")
        Dice1 = int(random.randint(1,6))
        print(Dice1)

    for x in range (1):
        print ("You rolled a:")
        Dice2 = int(random.randint(1,6))
        print(Dice2)


diceTotalp1 = Dice1 + Dice2

score = diceTotalp1

oddScore = int(score) - 5 

scoreZero = int(0)

evenScore = int(score) + 10

if score == int(2):
        print("You rolled an even number + 10 points!")
        score + 10
        score = evenScore
    
elif score == int(4):
         print("You rolled an even number + 10 points!")
         score + 10
         score = evenScore

elif score == int(6):
         print("You rolled an even number + 10 points!")
         score + 10
         score = evenScore

elif score == int(8):
         print("You rolled an even number + 10 points!")
         score + 10
         score = evenScore
         
elif score == int(10):
         print("You rolled an even number + 10 points!")
         score + 10
         score = evenScore
elif score == int(12):
         print("You rolled an even number + 10 points!")
         score + 10
         score = evenScore

elif score == int(3):
    print("Aww. You rolled an odd number. - 5 points.")
    score - 5
    score = oddScore

elif score == int(5):
    print("Aww. You rolled an odd number. - 5 points.")
    score - 5
    score = oddScore


elif score == int(7):
    print("Aww. You rolled an odd number. - 5 points.")
    score - 5
    score = oddScore

elif score == int(9):
    print("Aww. You rolled an odd number. - 5 points.")
    score - 5
    score = oddScore

     
elif score == int(11):
    print("Aww. You rolled an odd number. - 5 points.")
    score - 5
    score = oddScore

elif score == int(0):
    print("Your score is already 0! It can't go any lower. That's just mean")
    score + 0


if score == int(0):
    print("Your score is already 0! It can't go any lower. That's just mean")
    score + 0

# If Player 1 rolls double, roll a third dice and add it to their score
if Dice1 == Dice2:
    print("\n")
    print("Congratulations! You rolled a double. Here's a bonus roll.")
    for x in range (1):
        print("You rolled a:")
        bonusDice = int(random.randint(1,6))
        print(bonusDice)

        bonusScore = score + bonusDice
        score = bonusScore


        

# Note to self: Remind Debbie that 2 other methods were attempted before settling on if/elif.
# 1. Creating a variable that had all the even/odd numbers in them respectively, Outcome: Wouldn't work
# 2. On launch, writing a list of all the even/odd numbers to a local file. And then reading that local file where appropriate.
# Outcome: Could read and print the list, but could not read and apply them to an if statement.

# Shows the players what Player 1's final score for the round is     
print("\n")
print(p1Name + "'s score for round 2 is: " + str (score))
print("\n")

# Write Player 1's total for this round to a local file
f=open("Player1_Data.txt" , "a")
f.write(str (diceTotalp1) + ("\n"))
f.close()

# Write Player 1's final score for the round to a local file
f=open("Player1_Data.txt" , "a")
f.write(str (score) + ("\n")) 
f.close()

# Ask player 2 if they would like to roll, and if yes, then roll them.
player2Roll = input(p2Name + " would you like to roll your dice? Y/N: ")
print("\n")
if player2Roll ==("Y"):
    for x in range (1):
        print ("You rolled a:")
        dice1 = int(random.randint(1,6))
        print(dice1)

    for x in range (1):
        print ("You rolled a:")
        dice2 = int(random.randint(1,6))
        print(dice2)

diceTotalp2 = dice1 + dice2

scorep2 = diceTotalp2

oddScorep2 = int(scorep2) - 5 

scoreZerop2 = int(0)

evenScorep2 = int(scorep2) + 10

if scorep2 == int(2):
        print("You rolled an even number + 10 points!")
        scorep2 + 10
        scorep2 = evenScorep2
    
elif scorep2 == int(4):
         print("You rolled an even number + 10 points!")
         scorep2 + 10
         scorep2 = evenScorep2

elif scorep2 == int(6):
         print("You rolled an even number + 10 points!")
         scorep2 + 10
         scorep2 = evenScorep2

elif scorep2 == int(8):
         print("You rolled an even number + 10 points!")
         scorep2 + 10
         scorep2 = evenScorep2
         
elif scorep2 == int(10):
         print("You rolled an even number + 10 points!")
         scorep2 + 10
         scorep2 = evenScorep2
elif scorep2 == int(12):
         print("You rolled an even number + 10 points!")
         scorep2 + 10
         scorep2 = evenScorep2

elif scorep2 == int(3):
    print("Aww. You rolled an odd number. - 5 points.")
    scorep2 = oddScorep2

elif scorep2 == int(5):
    print("Aww. You rolled an odd number. - 5 points.")
    scorep2 = oddScorep2


elif scorep2 == int(7):
    print("Aww. You rolled an odd number. - 5 points.")
    scorep2 = oddScorep2

elif scorep2 == int(9):
    print("Aww. You rolled an odd number. - 5 points.")
    scorep2 = oddScorep2

     
elif scorep2 == int(11):
    print("Aww. You rolled an odd number. - 5 points.")
    scorep2 = oddScorep2

elif scorep2 == int(0):
    print("Your score is already 0! It can't go any lower. That's just mean")
    scorep2 + 0

# If Player 2 rolls a double, roll a bonus die and add it to their score.
if dice1 == dice2:
    print("\n")
    print("Congratulations! You rolled a double. Here's a bonus roll.")
    for x in range (1):
        print("You rolled a:")
        bonusDicep2 = int(random.randint(1,6))
        print(bonusDicep2)

        bonusScorep2 = scorep2 + bonusDicep2
        scorep2 = bonusScorep2

# Shows the players what Player 2's final score for the round is.
print("\n")
print(p2Name + "'s score for round 2 is: " + str (scorep2))

# Write Player 2's roll for this round to a local file
f=open("Player2_Data.txt" , "a")
f.write(str(diceTotalp2)+ ("\n"))
f.close()

f=open("Player2_Data.txt" , "a")
f.write(str(scorep2))
f.close()


# Ask if player 1 would like to roll their dice, and if yes, then roll them.
player1Roll = input(p1Name + " would you like to roll your dice? Y/N: ")
print("\n")


# Credit to StackOveflow. (Finding User later)
if player1Roll ==("Y"):
    for x in range (1):
        print ("You rolled a:")
        Dice1 = int(random.randint(1,6))
        print(Dice1)

    for x in range (1):
        print ("You rolled a:")
        Dice2 = int(random.randint(1,6))
        print(Dice2)


diceTotalp1 = Dice1 + Dice2

score = diceTotalp1

oddScore = int(score) - 5 

scoreZero = int(0)

evenScore = int(score) + 10

if score == int(2):
        print("You rolled an even number + 10 points!")
        score + 10
        score = evenScore
    
elif score == int(4):
         print("You rolled an even number + 10 points!")
         score + 10
         score = evenScore

elif score == int(6):
         print("You rolled an even number + 10 points!")
         score + 10
         score = evenScore

elif score == int(8):
         print("You rolled an even number + 10 points!")
         score + 10
         score = evenScore
         
elif score == int(10):
         print("You rolled an even number + 10 points!")
         score + 10
         score = evenScore
elif score == int(12):
         print("You rolled an even number + 10 points!")
         score + 10
         score = evenScore

elif score == int(3):
    print("Aww. You rolled an odd number. - 5 points.")
    score - 5
    score = oddScore

elif score == int(5):
    print("Aww. You rolled an odd number. - 5 points.")
    score - 5
    score = oddScore


elif score == int(7):
    print("Aww. You rolled an odd number. - 5 points.")
    score - 5
    score = oddScore

elif score == int(9):
    print("Aww. You rolled an odd number. - 5 points.")
    score - 5
    score = oddScore

     
elif score == int(11):
    print("Aww. You rolled an odd number. - 5 points.")
    score - 5
    score = oddScore

elif score == int(0):
    print("Your score is already 0! It can't go any lower. That's just mean")
    score + 0


if score == int(0):
    print("Your score is already 0! It can't go any lower. That's just mean")
    score + 0

# If Player 1 rolls double, roll a third dice and add it to their score
if Dice1 == Dice2:
    print("\n")
    print("Congratulations! You rolled a double. Here's a bonus roll.")
    for x in range (1):
        print("You rolled a:")
        bonusDice = int(random.randint(1,6))
        print(bonusDice)

        bonusScore = score + bonusDice
        score = bonusScore


        

# Note to self: Remind Debbie that 2 other methods were attempted before settling on if/elif.
# 1. Creating a variable that had all the even/odd numbers in them respectively, Outcome: Wouldn't work
# 2. On launch, writing a list of all the even/odd numbers to a local file. And then reading that local file where appropriate.
# Outcome: Could read and print the list, but could not read and apply them to an if statement.

# Shows the players what Player 1's final score for the round is     
print("\n")
print(p1Name + "'s score for round 3 is: " + str (score))
print("\n")

# Write Player 1's total for this round to a local file
f=open("Player1_Data.txt" , "a")
f.write(str(diceTotalp1) + ("\n"))
f.close()

# Write Player 1's final score for the round to a local file
f=open("Player1_Data.txt" , "a")
f.write(str (score) + ("\n")) 
f.close()

# Ask player 2 if they would like to roll, and if yes, then roll them.
player2Roll = input(p2Name + " would you like to roll your dice? Y/N: ")
print("\n")
if player2Roll ==("Y"):
    for x in range (1):
        print ("You rolled a:")
        dice1 = int(random.randint(1,6))
        print(dice1)

    for x in range (1):
        print ("You rolled a:")
        dice2 = int(random.randint(1,6))
        print(dice2)

diceTotalp2 = dice1 + dice2

scorep2 = diceTotalp2

oddScorep2 = int(scorep2) - 5 

scoreZerop2 = int(0)

evenScorep2 = int(scorep2) + 10

if scorep2 == int(2):
        print("You rolled an even number + 10 points!")
        scorep2 + 10
        scorep2 = evenScorep2
    
elif scorep2 == int(4):
         print("You rolled an even number + 10 points!")
         scorep2 + 10
         scorep2 = evenScorep2

elif scorep2 == int(6):
         print("You rolled an even number + 10 points!")
         scorep2 + 10
         scorep2 = evenScorep2

elif scorep2 == int(8):
         print("You rolled an even number + 10 points!")
         scorep2 + 10
         scorep2 = evenScorep2
         
elif scorep2 == int(10):
         print("You rolled an even number + 10 points!")
         scorep2 + 10
         scorep2 = evenScorep2
elif scorep2 == int(12):
         print("You rolled an even number + 10 points!")
         scorep2 + 10
         scorep2 = evenScorep2

elif scorep2 == int(3):
    print("Aww. You rolled an odd number. - 5 points.")
    scorep2 = oddScorep2

elif scorep2 == int(5):
    print("Aww. You rolled an odd number. - 5 points.")
    scorep2 = oddScorep2


elif scorep2 == int(7):
    print("Aww. You rolled an odd number. - 5 points.")
    scorep2 = oddScorep2

elif scorep2 == int(9):
    print("Aww. You rolled an odd number. - 5 points.")
    scorep2 = oddScorep2

     
elif scorep2 == int(11):
    print("Aww. You rolled an odd number. - 5 points.")
    scorep2 = oddScorep2

elif scorep2 == int(0):
    print("Your score is already 0! It can't go any lower. That's just mean")
    scorep2 + 0

# If Player 2 rolls a double, roll a bonus die and add it to their score.
if dice1 == dice2:
    print("\n")
    print("Congratulations! You rolled a double. Here's a bonus roll.")
    for x in range (1):
        print("You rolled a:")
        bonusDicep2 = int(random.randint(1,6))
        print(bonusDicep2)

        bonusScorep2 = scorep2 + bonusDicep2
        scorep2 = bonusScorep2

# Shows the players what Player 2's final score for the round is.
print("\n")
print(p2Name + "'s score for round 3 is: " + str (scorep2))

# Write Player 2's roll for this round to a local file
f=open("Player2_Data.txt" , "a")
f.write(str(diceTotalp2)+ ("\n"))
f.close()

f=open("Player2_Data.txt" , "a")
f.write(str(scorep2))
f.close()


# Note to self: Remind Debbie that 2 other methods were attempted before settling on if/elif.
# 1. Creating a variable that had all the even/odd numbers in them respectively, Outcome: Wouldn't work
# 2. On launch, writing a list of all the even/odd numbers to a local file. And then reading that local file where appropriate.
# Outcome: Could read and print the list, but could not read and apply them to an if statement.

# Shows the players what Player 1's final score for the round is     
print("\n")
print(p1Name + "'s score for round 3 is: " + str (score))
print("\n")

# Write Player 1's total for this round to a local file
f=open("Player1_Data.txt" , "a")
f.write(str (diceTotalp1) + ("\n"))
f.close()

# Write Player 1's final score for the round to a local file
f=open("Player1_Data.txt" , "a")
f.write(str (score) + ("\n")) 
f.close()

# Ask player 2 if they would like to roll, and if yes, then roll them.
player2Roll = input(p2Name + " would you like to roll your dice? Y/N: ")
print("\n")
if player2Roll ==("Y"):
    for x in range (1):
        print ("You rolled a:")
        dice1 = int(random.randint(1,6))
        print(dice1)

    for x in range (1):
        print ("You rolled a:")
        dice2 = int(random.randint(1,6))
        print(dice2)

diceTotalp2 = dice1 + dice2

scorep2 = diceTotalp2

oddScorep2 = int(scorep2) - 5 

scoreZerop2 = int(0)

evenScorep2 = int(scorep2) + 10

if scorep2 == int(2):
        print("You rolled an even number + 10 points!")
        scorep2 + 10
        scorep2 = evenScorep2
    
elif scorep2 == int(4):
         print("You rolled an even number + 10 points!")
         scorep2 + 10
         scorep2 = evenScorep2

elif scorep2 == int(6):
         print("You rolled an even number + 10 points!")
         scorep2 + 10
         scorep2 = evenScorep2

elif scorep2 == int(8):
         print("You rolled an even number + 10 points!")
         scorep2 + 10
         scorep2 = evenScorep2
         
elif scorep2 == int(10):
         print("You rolled an even number + 10 points!")
         scorep2 + 10
         scorep2 = evenScorep2
elif scorep2 == int(12):
         print("You rolled an even number + 10 points!")
         scorep2 + 10
         scorep2 = evenScorep2

elif scorep2 == int(3):
    print("Aww. You rolled an odd number. - 5 points.")
    scorep2 = oddScorep2

elif scorep2 == int(5):
    print("Aww. You rolled an odd number. - 5 points.")
    scorep2 = oddScorep2


elif scorep2 == int(7):
    print("Aww. You rolled an odd number. - 5 points.")
    scorep2 = oddScorep2

elif scorep2 == int(9):
    print("Aww. You rolled an odd number. - 5 points.")
    scorep2 = oddScorep2

     
elif scorep2 == int(11):
    print("Aww. You rolled an odd number. - 5 points.")
    scorep2 = oddScorep2

elif scorep2 == int(0):
    print("Your score is already 0! It can't go any lower. That's just mean")
    scorep2 + 0

# If Player 2 rolls a double, roll a bonus die and add it to their score.
if dice1 == dice2:
    print("\n")
    print("Congratulations! You rolled a double. Here's a bonus roll.")
    for x in range (1):
        print("You rolled a:")
        bonusDicep2 = int(random.randint(1,6))
        print(bonusDicep2)

        bonusScorep2 = scorep2 + bonusDicep2
        scorep2 = bonusScorep2

# Shows the players what Player 2's final score for the round is.
print("\n")
print(p2Name + "'s score for round 3 is: " + str (scorep2))

# Write Player 2's roll for this round to a local file
f=open("Player2_Data.txt" , "a")
f.write(str(diceTotalp2)+ ("\n"))
f.close()

f=open("Player2_Data.txt" , "a")
f.write(str(scorep2))
f.close()


