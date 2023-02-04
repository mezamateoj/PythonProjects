import matplotlib.pyplot as plt
import numpy as np

def future_value(r, t, p):
    return p * (1 + r / 100) ** t



def present_value(r, t, fv):
    return fv / ((1 + r / 100) ** t)

def acf(r, n):
    """Annuity Compound Factor
        r: interest rate,
        n: number of periods"""
    r = r / 100
    return (((1 + r)**n - 1) / r)


def adc(r, n):
    """Annuity Discount Factor,
        r: interest rate,
        n: number of periods"""
    return ((1 - 1 / (1 + r/100)**n) / (r/100))

def ear(r,period, t):
    """Effective annual rate
        r: APR
        period: annualy, quarterly, etc
        t: time"""
    r = r / 100
    factor = r / period  # APR / m
    effective = (1 + factor) ** t - 1
    return effective

#print(ear(8, 12, 20))

def continous_ear(r, t):
    r = r / 100
    return np.exp(r * t) - 1

# Using grow rates in annuities and perpetuities

def perpetuities(c, r, g=0):
    """Present Value of perpetuities
        c: cash flow
        r: interest rate
        g: constant growth"""
    r = r / 100
    g = g / 100
    pv = c / (r - g)
    return pv

def acf_g(r, n, g=0):
    """Annuity Compound Factor
        r: interest rate,
        n: number of periods
        g: growth rate"""
    r = r / 100
    g = g / 100
    return (((1 + r)**n - (1 + g)**n) / (r - g))


def adc_g(r, n, g=0):
    """Annuity Discount Factor,
        r: interest rate,
        n: number of periods
        g: growth rate"""
    r = r / 100
    g = g / 100
    return ((1 - ((1 + g)**n / (1 + r)**n)) / (r - g))

def vpn(investment, fcf, r, n):
    r = r / 100
    vp = fcf / (1 + r)**n
    return -investment + vp

# value of a company no debt 
def value_unlevered(fcf, r, n):
    r = r / 100
    return fcf / (1+r)**n



print(f'vpn is: {vpn(1000, 3500, 5, 5)}')
#print(f'Pv of my salary if it growths 5% at 8% interest rate for 5 years and starts at 90000 is: {90000 * adc_g(8, 5, 5)}')

# answer question boat 1
print(f'answer q1: {25000 / acf(8, 5)}')

# question 4. 1000 apr 8% semi annualy fv ?
print(f'q4: {future_value(4, 6, 1000)}')

# question 5 1000 fv compund montly
print(future_value(8/12, 36, 1000))

# question savings at 65
savings_fv = future_value(9, 35, 20000)
target = 1000000

c = target - savings_fv
print(c)
print(c / (acf(9, 35)))

# answer question golf
print(4000 / (1 + adc(1, 23)))
                
    
#print(f'ear: {ear(2, 4, 4) * 100}%')
# flows = [3000, 2000, 4000, 1000]
# futures = []

# years = 4
# for i in flows:
#     value = future_value(5, years - 1, i)
#     futures.append(value)
#     print(f'the fv is {value}')
#     years = -1

# Plot Compound Interest
# invest 100, guarantee 5& annual retrun in 30 years
def compound_plot(p, r, t):
    years = list(range(t + 1))
    values = [future_value(r, t, p) for t in years]

    plt.plot(years, values, color='salmon')
    plt.xlabel('Years')
    plt.ylabel('Value')
    plt.title('Compound Interest')
    plt.show()

