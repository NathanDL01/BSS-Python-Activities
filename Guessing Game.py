from random import randint

num=randint(1,20)

print("This program is a guessing game! There are only 3 chances to play this game")
print(num)

for i in range(3):
    guess=eval(input("Type your guess number between 1 and 20: "))
    
    if guess == num:
        print("CONGRATULATIONS, You got it! ")
        exit()
    elif guess!=num and lives!=1:
        print("Oops wrong! Please try again.")
        lives=lives-1
    else:
        print("You used up all your lives, GAME OVER!")
        print (num)
        
        
        
        
        
        
        