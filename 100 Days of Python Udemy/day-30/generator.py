import random

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
          'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
          'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

number_letters = random.randint(8, 10)
number_symbols = random.randint(2, 4)
number_numbers = random.randint(2, 4)

def password():
    password = []
    for i in range(0, number_letters):
        password.append(random.choice(letter))
    for i in range(0, number_symbols):
        password.append(random.choice(symbols))
    for i in range(0, number_numbers):
        password.append(random.choice(numbers))
    random.shuffle(password)
    password = ''.join(password)
    return password

