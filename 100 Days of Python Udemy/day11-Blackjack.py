import random

from scipy import rand

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def first_hand(cards):
    hand = list(random.sample(cards, 2))
    return hand

#current_sum = hand[0] + hand[1]

def dealers(cards):
    dealer_hand = list(random.sample(cards, 2))
    return dealer_hand

def hit(cards):
    hit_card = random.sample(cards, 1)
    return hit_card

def game(x, y):
    if sum(x) > 21:
        print('You bust')
    pass
    

# player = [i for i in first_hand(cards)]
# print(player)
# dealer = [i for i in dealers(cards)]
# print(dealer)

print('welcome to 21')
my_hands = first_hand(cards)  
dealer_hands = dealers(cards)

print(f'Your cards are: {my_hands}, sum {sum(my_hands)}')
print(f'Dealers first card: {dealer_hands[0]}')
    
game_on = True
while game_on == True:   
    # player.append([i for i in first_hand(cards)])
    # dealer.append([i for i in dealer(cards)])
  
    player = input('Hit or Pass press: "h" or "p" ')

    if player == 'h':
        add_card1 = hit(cards)[0]
        add_card2 = hit(cards)[0]
        my_hands.append(add_card1)
        # print(my_hands)
        dealer_hands.append(add_card2)
        # print(dealer_hands)
        print(f'Your cards are {my_hands}, sum is {sum(my_hands)}')
        if sum(my_hands) > 21:
            print('You bust')
            game_on = False
        # elif sum(dealer_hands) > 21:
        #     print('You win, the dealer bust')
        #     game_on = False

    elif player == 'p':
        if sum(my_hands) > sum(dealer_hands):
            print(f'You win you had {sum(my_hands)}')
            game_on = False
        else:
            print(f'You lose dealer had {sum(dealer_hands)}')
            game_on = False




