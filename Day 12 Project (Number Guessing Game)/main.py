import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking a number between 1 and 100")

random_number = random.randint(1,100)


def play_easy():
    global random_number
    attempts = 10
    finished = False
    a = "Guess Again."
    
    
    while attempts != 0 and finished != True:
        print(f"You have only {attempts} remaining to guess the number.")
        guess = int(input("Make a guess: "))
        
        if guess == random_number:
            print(f"You got it! The answer was {random_number}")
            finished = True
        elif guess > random_number:
            print("Too High")
            attempts -= 1
            if attempts == 0:
                a = "Game Over"
            print(a)
            
        elif guess < random_number:
            print("Too Low")
            attempts -= 1
            if attempts == 0:
                a = "Game Over"            
            print(a)
            
    
def play_hard():
    global random_number
    attempts = 5
    finished = False
    a = "Guess Again."
    
    
    while attempts != 0 and finished != True:
        print(f"You have only {attempts} remaining to guess the number.")
        guess = int(input("Make a guess: "))
        
        if guess == random_number:
            print(f"You got it! The answer was {random_number}")
            finished = True
        elif guess > random_number:
            print("Too High")
            attempts -= 1
            if attempts == 0:
                a = "Game Over"
            print(a)
            attempts -= 1
        elif guess < random_number:
            print("Too Low")
            attempts -= 1
            if attempts == 0:
                a = "Game Over"
            print(a)
        
        
        
  
def game():        
    
    difficulty = input("\nChoose a difficulty. Type 'easy' or 'hard': ").lower()        
            
    if difficulty == 'easy' or difficulty == 'e':
        play_easy()
    elif difficulty == 'hard' or difficulty == 'h':
        play_hard()
    else:
        print("Please enter a valid input.")
        game()
    
game()