logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

auction = {}

def star():
    name = input('What is your name?: ')
    bid = input('What is your bid?: $')
    global auction
    auction[name] = bid

more_bid = 'yes'
while more_bid == 'yes':
    star()
    more_bid = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if more_bid == 'no':
        winners_name = [name for name, bid in auction.items() if bid == max(auction.values())]
        print(f'The winner is {winners_name[0]} with a bid of ${max(auction.values())}')

