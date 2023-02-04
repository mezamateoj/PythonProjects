def test(*args):
    print(args)

#test('hola', 102, 'sera')
tables = {
  1: {
    'name': 'Jiho',
    'vip_status': False,
    'order': 'Orange Juice, Apple Juice'
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}
#print(tables)

def assign_table(table_number, name, vip_status=False): 
    tables[table_number]['name'] = name
    tables[table_number]['vip_status'] = vip_status
    tables[table_number]['order'] = ''


def assign_order(table_number, *order):
    tables[table_number]['order'] = list(order)
    for i in order:
        print(i)

assign_table(2, 'Arwa', True)
#assign_order(2, 'Steak', 'Seabass', 'Wine Bottle')

#print(tables)

# However, the staff now wants to distinguish between food items and drinks.
tables2 = {
  1: {
    'name': 'Chioma',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes'
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}

def assign_table2(table_number, name, vip_status=False): 
    tables2[table_number]['name'] = name
    tables2[table_number]['vip_status'] = vip_status
    tables2[table_number]['order'] = {}

assign_table2(2, 'Douglas', True)

#print('--- tables with Douglas --- \n', tables2)

def assign_food(table_number, **kwargs):
    food = kwargs.get('food')
    drinks = kwargs.get('drinks')
    tables2[table_number]['order']['food_items'] = food
    tables2[table_number]['order']['drinks'] = drinks

assign_food(2, food='Pancakes, Poached Egg', drinks='Margarita, Water')
# Write your code below: 
# print()
# print(tables2)

# Example Call
# assign_food_items(food='Pancakes, Poached Egg', drinks='Water')


def single_prix_fixe_order(appetizer, *entrees, sides, **dessert_scoops):
    print(appetizer)
    print(entrees)
    print(sides)
    print(dessert_scoops)

#single_prix_fixe_order('Baby Beets', 'Salmon', 'Scallops', sides='Mashed Potatoes', dessert_scoops='Vanilla, Cookies and Cream')

def calculate_price_per_person(total, tip, split):
    total_tip = total * (tip/100)
    split_price = (total + total_tip) / split
    print(split_price)


table_7_total = [534.50, 20.0, 5]
# Using the unpacking operato to call the function
calculate_price_per_person(*table_7_total)



