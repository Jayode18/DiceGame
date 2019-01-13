import random
import time

def loginSys():

    username = ("user")

    beginLogin = input("Please enter your username: ")


    
    if beginLogin == username:
        print("\n")
        print("Username correct")
        print("\n")

    else:
        print("\n")
        print("Username incorrect")
        print("\n")
        loginSys()


loginSys()

def loginPass():

    password = ("password")
  
    Loginpass = input("Now please enter your password: ")
    print("\n")


    if Loginpass == password:
        print("Login successful. The game will begin in 5 seconds")
        print("\n")
        time.sleep(5)

    else:
        print("Password incorrect")
        loginPass()

loginPass()

numRound = 1


p1Name = input("Player 1, what is your name? ")

f=open("D:\\Player1_Info.txt" , "a")
f.write(p1Name + "\n")
f.close()

p2Name = input("Player 2, what is your name? ")

f=open("D:\\Player2_Info.txt" , "a")
f.write(p2Name + "\n")
f.close()

print("\n")



def rollDice():

   

   
            for x in range (1):
                Dice1 = int(random.randint(1,6))
                Dice2 = int(random.randint(1,6))
                
                print("Rolling...")
                time.sleep(0.5)

                print("You rolled a " + str(Dice1) + " and a " + str(Dice2))
                print("\n")
                time.sleep(0.25)
                print("\n")

                score = Dice1 + Dice2

                print(p1Name + " your final score for round " + str(numRound) + " is " + str(score))
                print("\n")




           

            def rollDiceP2():
                 for x in range (1):
                    Dice1 = int(random.randint(1,6))
                    Dice2 = int(random.randint(1,6))
                    
                    print("Rolling...")
                    time.sleep(0.5)

                    print("You rolled a " + str(Dice1) + " and a " + str(Dice2))
                    print("\n")
                    time.sleep(0.25)
                    print("\n")

                    score = Dice1 + Dice2

                    print(p2Name + " your final score for round " + str(numRound) + " is " + str(score))
                    print("\n")

                    int(numRound) + 1



rollDice()
rollDiceP2()

