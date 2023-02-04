from pickle import encode_long
import random 

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]

# Todo-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
end_game = False
chosen_word = random.choice(word_list)
print(chosen_word)

lives = 6
display = []
guess = input('Choose a random word:').lower()

for i in chosen_word:
    if i == guess:
        display.append(i)       
    else:
        display.append('_')
        
print(' '.join(display))
print(stages[lives])

while end_game == False:
    guess = input('Choose a random word:').lower()

    if '_' not in display:
        end_game = True
        print('You Win')

    for position in range(len(chosen_word)):
        letter = chosen_word[position]

        if letter == guess:
            #replace = chosen_word.index(i)
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_game = True
            print('You lose')

    print(' '.join(display))
    print(stages[lives])




