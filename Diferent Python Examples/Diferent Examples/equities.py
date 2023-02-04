# Stocks

def expected_return(current_price, expected_p, div=0):
    return (div + expected_p - current_price) / current_price

def simple_expected_return(div, current_price, g):
    dividend_yield = div / current_price
    r = dividend_yield + (g/100)
    return (dividend_yield, r)

print(f'The expected return is {simple_expected_return(3, 57.14, 5)}')
print(f'The expected return is {simple_expected_return(3, 57.14, 6)}')

def present_value_g(div, r, g=0):
    return div / ((r/100) - (g/100))
print(f'present value of stock: {present_value_g(1.50, 13, 10)}')

def mkt_implied_g(r, pv, div):
    return ((r/100) * pv) - div
#print(f'market implied growth: {mkt_implied_g(9, 80, 5):.2%}')

def price_equity(expected_p, div, r):
    r = r / 100
    return (div + expected_p) / (1 + r)

def dividend_discount_model(cash_flows, r):
    pv = 0
    t = 0
    for i in cash_flows:
        period = i / (1 + (r/100))**t
        t += 1
        pv += period
    print(t)
    return pv


def price_with_dividend_g(rate_grow, r, initial_div):
    rate_grow = [x / 100 for x in rate_grow]
    all_divs = []
    div = initial_div * (1 + rate_grow[0])
    all_divs.append(div)
    
    for i in rate_grow[1:]:
        new_div = all_divs[-1] * (1 + (i))
        all_divs.append(new_div)

    discount_factor = (1 +(r/100))**(len(all_divs)-1)
    last_period = (all_divs[-1] / ((r/100) - rate_grow[-1])) / discount_factor

    return (sum(all_divs) / discount_factor) + last_period

print(f'price with div growth change: {price_with_dividend_g([10], 13, 1.50)}')




def dividend_yield(div, market_price, period):
    return (div * period) / market_price

print(f'dividend yield: {dividend_yield(0.17, 19.72, 4):.2%}')

print(f'pv of stock: {dividend_discount_model([20, 40, 35], 9)}')


#  Fledgling Electronics stock is selling for $100. 
# Investors expect  $5 cash dividend over the next year 
# They also expect the stock to sell for $110
print('Example #1')
print(f'expected return : {expected_return(60, 69.77, 1.75):.2%}')
print(f'expected return : {expected_return(105, 110, 5):.2f}')
print(f'price of equity: {price_equity(110, 5, 15):.2f}')

print('Example #2')
print(f'cost of equity capital: {simple_expected_return(1.18, 33.62, 6.6)}')
