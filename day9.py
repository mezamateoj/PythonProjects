# nesting
capitals = {
    'France': 2,
    'Germany': 5,
}

# nesting a list in a Dictionary
travel_log = {
    'France': ['Paris', 'Lille', 'Dijon'],
    'Germany': ['Berlin', 'Hamburg', 'Stuttgart'],
}

# nesting dictionary in dictionary 

travel_log2 = {
    'France': {'cities_visited': ['Paris', 'Lille', 'Dijon'], 'total_visits': 10},
    'Germany': {'cities_visited': ['Berlin', 'Hamburg', 'Stuttgart'], 'total_visits': 5},
}

# nesting dictionaries inside a list
travel_log3 = [
    {
     'country': 'France', 
     'cities_visited': ['Paris', 'Lille', 'Dijon'], 
     'total_visits': 10
    },
    {
     'country': 'Germany', 
     'cities_visited': ['Berlin', 'Hamburg', 'Stuttgart'], 
     'total_visits': 5
    },
]

print(travel_log3[0])

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(max(capitals.keys()))