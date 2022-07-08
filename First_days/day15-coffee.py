
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    'money': 0,
}


def report(resources):
    for i, j in resources.items():
        if i == 'coffee':
            print(f'{i}: {j}g')
        elif i == 'money':
            print(f'{i}: ${j}')
        else:
            print(f'{i}: {j}ml')
        


espresso = MENU["espresso"]['ingredients']
latte = MENU["latte"]['ingredients']
cappuccino = MENU["cappuccino"]['ingredients']

cost_espresso = MENU["espresso"]['cost']
cost_latte = MENU["latte"]['cost']
cost_cappuccino = MENU['cappuccino']['cost']


def check_ingredients(resources, coffee_type):
    A = list(resources.keys())
    B = list(coffee_type.keys())
    commonKeys = set(A) - (set(A) - set(B))

    
    for key in commonKeys:
        if(resources[key] < coffee_type[key]):
            print(f"Can't make {costumer} missing {key}")
            return False
    
        
def update_ingredients(resources, coffee_type):
    A = list(resources.keys())
    B = list(coffee_type.keys())
    commonKeys = set(A) - (set(A) - set(B))

    for key in commonKeys:
        resources[key] -= coffee_type[key]

    return resources

def money_calculation():
    money_value = {'q': 0.25, 'd': 0.10, 'n': 0.05, 'p': 0.01}
    print('Insert Coins!')

    quarter = int(input('How many quarters: '))
    dimes = int(input('How many dimes: '))
    nickles = int(input('How many nickles: '))
    pennies = int(input('How many pennies: '))

    total = (money_value["q"] * quarter)+(money_value["d"] * dimes)+ (money_value["n"] * nickles)+ (money_value["p"] * pennies)
    return total
    


coffee_on = True
while coffee_on == True:
    costumer = input('What would you like? (espresso/latte/cappuccino): ')

    if costumer == 'espresso':
        if check_ingredients(resources, espresso) == False:
            continue
            

        finance = money_calculation()
        if finance < cost_espresso:
            print('Sorry not enough money')

        elif finance > cost_espresso and check_ingredients != False:
            resources["money"] += cost_espresso
            change = finance - cost_espresso
            update_ingredients(resources, espresso)
            print(f'Here is your change ${round(change, 5)}')
            print(f'Here is your {costumer}. Enjoy!')
            

    elif costumer == 'latte':
        if check_ingredients(resources, latte) == False:
            continue
            
        
        finance = money_calculation()
        if finance < cost_latte:
            print('Sorry not enough money')

        elif finance > cost_latte and check_ingredients != False:
            resources["money"] += cost_latte
            change = finance - cost_latte
            update_ingredients(resources, latte)
            print(f'Here is your change ${round(change, 5)}')
            print(f'Here is your {costumer}. Enjoy!')
            

    elif costumer == 'cappuccino':
        if check_ingredients(resources, cappuccino) == False:
            continue
            

        finance = money_calculation()
        if finance < cost_cappuccino:
            print('Sorry not enough money')

        elif finance > cost_cappuccino and check_ingredients != False:
            resources["money"] += cost_cappuccino
            change = finance - cost_cappuccino
            update_ingredients(resources, cappuccino)
            print(f'Here is your change ${round(change, 5)}')
            print(f'Here is your {costumer}. Enjoy!')
            
    
    elif costumer == 'report':
        report(resources)

    elif costumer == 'off':
        coffee_on = False