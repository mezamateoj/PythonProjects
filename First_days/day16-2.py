from prettytable import PrettyTable
table = PrettyTable()
table2 = PrettyTable()
# one option
table.add_column("City name",["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"]) 
table.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386]) 
table.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092, 1554769]) 
table.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9, 869.4])

# second option 
table2.field_names = ['City name', 'Area', 'Population', 'Annual Rainfall']
table2.add_rows(
    [
        ["Adelaide", 1295, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Darwin", 112, 120900, 1714.7],
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4],
    ]

)



print(table)
print()
print(table2)