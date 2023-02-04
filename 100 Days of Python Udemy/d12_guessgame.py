import random
print('welcome to the number Guessing game!')
print("I'm thinking of a number between 1 and 100")

number = random.randint(1, 100)
print(number)

def number_guess(number_lives):
    lives = number_lives
    while lives > 0:
        print(f'You have {lives} attempts remaining to guess the number')
        guess = int(input('Make a Guess: '))
        if guess > number:
            print('Too high')
            lives -= 1
        elif guess < number:
            print('Too low')
            lives -= 1
        elif guess == number:
            print('You win!')
            break
    if lives == 0:
        print('You have run out of guesses, you lose')        

player_choice = input("Choose a difficulty. Type 'easy or 'hard: ")

if player_choice == 'easy':
    number_guess(10)
    
if player_choice == 'hard':
    number_guess(5)
                
# you hace 5 attempts remaining to guess the number
# Make a guess: 
