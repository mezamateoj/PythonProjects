import pandas as pd
from pycoingecko import CoinGeckoAPI
import matplotlib.pyplot as plt
import plotly.graph_objects as go

cg = CoinGeckoAPI()

#print(cg.get_price(ids='bitcoin, solana, ethereum', vs_currencies='usd'))
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)
df = pd.DataFrame(bitcoin_data['prices'], columns=['Timestamp', 'Price'])
df['Date'] = pd.to_datetime(df['Timestamp'], unit='ms') 
#print(df.head())

candle_stick = df.groupby(df.Date.dt.date).agg({'Price': ['min', 'max', 'first', 'last']})
#print(candle_stick)

# plotting candlestick using plotly 
fig = go.Figure(data=[go.Candlestick(x = candle_stick.index,
                open = candle_stick['Price']['first'],
                high = candle_stick['Price']['max'],
                low = candle_stick['Price']['min'],
                close = candle_stick['Price']['last'])
            ])

fig.update_layout(xaxis_title='Date', yaxis_title='Price (USD $)',
                    title = 'Bitcoin Candlestick Cahrt past 30 days')

#plot(fig, filename='bitcoin_candle.html')
#fig.show()

