#lets start!!!
import random
from os import system
from time import sleep
words=['apple','banana','fish']

def get_question():
    return (random.choice(words)).lower()

def display():
    print("\n\t\t")
    for i in range (len(secret)):
        print(secret[i],end=" ")
    print()

def hangman(n):
    order=[
        """
        |__________________________
        |                     |
        |                     |
        |
        |
        |
        |
        |
        |
        |
        |______________________________________""",
        """
        |__________________________
        |                     |
        |                     |
        |                     O
        |
        |
        |
        |
        |
        |
        |______________________________________""",
        """
        |__________________________
        |                     |
        |                     |
        |                     O
        |                     |
        |
        |
        |
        |
        |
        |______________________________________""",
        """
        |__________________________
        |                     |
        |                     |
        |                     O
        |                     |\\
        |
        |
        |
        |
        |
        |______________________________________""",
         """
        |__________________________
        |                     |
        |                     |
        |                     O
        |                    /|\\
        |
        |
        |
        |
        |
        |______________________________________""",
         """
        |__________________________
        |                     |
        |                     |
        |                     O
        |                    /|\\
        |                      \\
        |
        |
        |
        |
        |______________________________________""",
         """
        |__________________________
        |                     |
        |                     |
        |                     O
        |                    /|\\
        |                    / \\       
        |
        |
        |
        |
        |______________________________________"""
    ]
    print(order[n])

def ispresent(letter):
    for i in guessed:
        if i == letter:
            return False
    return True

def check(letter):
    flag= False
    for i in range(len(q_list)):
        if letter == q_list[i]:
            secret[i]=letter
            flag = True
    if flag:
        return True
    return False
   

def win():
    for i in range(len(q_list)):
        if secret[i] != q_list[i]:
            return False
    return True

            

def play():
    
    chance=0
    global guessed
    guessed=[]
    print("You have 6 chances to save")
    while True:
        sleep(1)
        system('cls')
        hangman(chance)
        display()
        method=input("\nWanna Enter a letter[any key] or A word To guess[0]\n>>>")
        if method=='0':
            guess=input("Guess a word\n>>>")
            if guess==question:
                print("Yea u win")
                return
            else:
                print("Wrong Guess!!!")
                chance += 1
                print("You have ",6-chance," chaces left")
        else:
            guess=input("Guess a letter \n>>>")
            if check(guess):
                if ispresent(guess):
                    guessed.append(guess)
                    print("OK")
                    if win():
                        print("YOu saved Your friend")
                        return
                else:
                    print("Letter already Guessed")
            else:
                print("Wrong Guess")
                chance += 1
                if chance >= 6:
                    print("You lost your friend sorry!!!")
                    return 
                print("You have ",6-chance," chances left")

def greet():
    print("Welcom to HANGMAN")
    sleep(1)
    print("This is a game where you would be given random words and u needa guess \n to save your friend")
    sleep(2)
    print("stakes are high \n BEST OF LUCK \n")    
    
                
def main():
    system("color 70")
    greet()
    system("cls")
    system("color 02")
    p='y'
    while p != 'n':
        global question
        question=get_question()
        global q_list
        q_list=list(question)
        global secret    
        secret=['_']*len(question)
        play()
        p=input("Wanna play again [y/n]??").lower()
main()