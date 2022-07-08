
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
class Coffee:
    water = 300
    milk = 200
    coffee = 100
    money = 0
    costumer = ''
    cost = 0
    total = 0
    coffee_types = ['espresso', 'latte', 'cappuccino']
    espresso = MENU["espresso"]['ingredients']
    latte = MENU["latte"]['ingredients']
    cappuccino = MENU["cappuccino"]['ingredients']
        
        
    def ingredients(self):
        if Coffee.costumer == 'espresso':
            self.check = Coffee.espresso
            Coffee.cost = 1.5
            
        elif Coffee.costumer == 'latte':
            self.check = Coffee.latte
            Coffee.cost = 2.5
            
        elif Coffee.costumer == 'cappuccino':
            self.check = Coffee.cappuccino
            Coffee.cost = 3.0
                     
    
    def check_ingredients(self):
        if Coffee.water < self.check['water']:
            print(f"Can't make {Coffee.costumer} missing water")
            return False
                      
        elif Coffee.milk < self.check['milk']:
            print(f"Can't make {Coffee.costumer} missing milk")
            return False         
            
        elif Coffee.coffee < self.check['coffee']:
            print(f"Can't make {Coffee.costumer} missing coffee")
            return False
     
            
    def update(self):
        Coffee.water -= self.check['water']
        Coffee.milk -= self.check['milk']
        Coffee.coffee -= self.check['coffee']
        Coffee.money += Coffee.cost
        print(f'Here is your change ${round((Coffee.total-Coffee.cost), 5)}')
        print(f'Here is your {Coffee.costumer}. Enjoy!')
    

    def report(self):
        print(f'water: {Coffee.water}ml')
        print(f'milk: {Coffee.milk}ml')
        print(f'coffee: {Coffee.coffee}g')
        print(f'money: ${Coffee.money}')


    def money_calculation(self):
        money_value = {'q': 0.25, 'd': 0.10, 'n': 0.05, 'p': 0.01}
        print('Insert Coins!')

        quarter = int(input('How many quarters: '))
        dimes = int(input('How many dimes: '))
        nickles = int(input('How many nickles: '))
        pennies = int(input('How many pennies: '))

        self.total = (money_value["q"] * quarter)+(money_value["d"] * dimes)+ (money_value["n"] * nickles)+ (money_value["p"] * pennies)
        Coffee.total = self.total



client = Coffee()
coffee_on = True
while coffee_on == True:
    what = input('What would you like? (espresso/latte/cappuccino): ')
    Coffee.costumer = what
    client.ingredients()

    if Coffee.costumer in Coffee.coffee_types:
        if client.check_ingredients() == False:
            continue

        client.money_calculation()
        if Coffee.total < Coffee.cost:
            print('Sorry not enough money')
        elif Coffee.total > Coffee.cost:
                client.update()

    elif Coffee.costumer == 'report':
        client.report()

    elif Coffee.costumer == 'off':
        coffee_on = False

    elif Coffee.costumer not in Coffee.coffee_types:
        print('We dont have that coffee, try again')