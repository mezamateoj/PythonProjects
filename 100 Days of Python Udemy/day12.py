enemies = 1

def increase_enemies():
    enemies = 2
    print(f'enemies inside function: {enemies}')

increase_enemies()
print(f'enemies outside function: {enemies}')

# Local Scope 
# inside a function
def drink_potion():
    # potion strenght has local scope
    potion_strenght = 2
    print(potion_strenght)

drink_potion()

# Global scope 
player_health = 10  # this variable has a global scope, can be use inside a function
def game():
    def drink_potion():  # now has local scope inside game
        # potion strenght has local scope
        potion_strenght = 2
        print(player_health)
    drink_potion()
#drink_potion()

# ther is no Bloclk Scope
game_level = 3
def create_enemy():    
    enemies = ['skeleton', 'zombie', 'alien']
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)

# modifying Global Scope / Avoid doing it it's not okay
enemy = 'Skeleton'
def change_enemy():
    global enemy  # this is not something wwe consider to do 
    enemy = 'Zombie'
    print(f'enemy inside function: {enemy}')

change_enemy()
print(f'enemy outside function: {enemy}')

# Gloabal constants
pi = 3.14

# variables that you are never going to change
# use upper case when naming thwe variable

URL = 'http:...'
TWITTER_HANDLE = '@mezamateoj'
