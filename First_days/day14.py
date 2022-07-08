
# coding=utf-8
from game_data import data
import random


score = 0
game = True
while game == True:
    random_1 = random.randint(1, 49)
    random_2 = random.randint(1, 49)
    follower_1 = data[random_1]['follower_count']
    follower_2 = data[random_2]['follower_count']
    print(f'Compare A: {data[random_1]["name"]} a {data[random_1]["description"]} from {data[random_1]["country"]}')
    print('V/S')
    print(f'Compare B: {data[random_2]["name"]} a {data[random_2]["description"]} from {data[random_2]["country"]}')
    user = input('Who has more followers? type "A" or "B": ')
    if user == 'A' and follower_1 > follower_2:
        score += 1
        print(f'You are right, current score: {score}')
    elif user == 'B' and follower_2 > follower_1:
        score += 1
        print(f'You are right, current score: {score}')
    else:
        print(f'Sorry, that is worng, final score: {score}')
        game = False




