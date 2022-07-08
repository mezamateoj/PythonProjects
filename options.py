import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Options:
    
    def __init__(self, strike):
        self.strike = strike
        self.call_option_table()


    def call_option_table(self):
        self.df = pd.DataFrame(list(range(self.strike-40, self.strike+40, 5)), columns = ['Stock Price'])
        self.df[f'${self.strike} Call Payoff'] = self.df['Stock Price'].apply(lambda x: max(x-self.strike, 0))
        self.df[f'${self.strike} Call Profit'] = self.df[f'${self.strike} Call Payoff'] - 5
        self.df = self.df.set_index('Stock Price')
        return self.df



    def call_option(self, strike, premium, market_price):
        # payoff to call holder, its never negative, sometimems its positive
        # CFt(call) ) = max[0, St - K]
        self.payoff = max(market_price - strike, 0)
        self.profit = self.payoff - premium

    #Graph the payoff
    def plot_payoff(self):
        ax = self.df[f'${self.strike} Call Payoff'].plot(kind='line')
        ax.axhline(0, linestyle='--', color='grey')
        plt.xlabel('Stock Price')
        plt.ylabel('Payoff')
        plt.title(f"${self.strike} Call Option Payoff")
        plt.show()


    #The cost is just a linear shift downwards
    def plot_profit(self):
        ax = self.df[f'${self.strike} Call Profit'].plot(kind='line')
        ax.axhline(0, linestyle='--', color='grey')
        plt.xlabel('Stock Price')
        plt.ylabel('Profit')
        plt.title(f"${self.strike} Call Option Profit")
        plt.show()

sera = Options(24)
print(sera.call_option_table())
#sera.plot_payoff()
#sera.plot_profit()

sera2 = Options(30)
print(sera2.call_option_table())
# sera2.plot_payoff()