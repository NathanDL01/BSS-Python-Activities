from random import randint
import sys

num=randint(1,20)

print("This program is a guessing game! There are only 3 chances to play this game")

lives=3

for i in range(lives):
    guess=eval(input("Type your guess number between 1 and 20: "))
    if guess == num:
        print("CONGRATULATIONS, You got it! ")
        sys.exit()
    elif lives!=0:
        print("Oops wrong! Please try again.")
        lives=lives-1
        print("Lives: ", lives)
    elif lives == 0:
        print("You used up all your lives, GAME OVER!")
        print (num)
        
        
        
        
        
        
        