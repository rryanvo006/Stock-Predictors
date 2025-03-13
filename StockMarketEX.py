import pandas as pd 
import yfinance as yf
import matplotlib.pyplot as plt

# Load Data
stock = yf.download("AAPL", start="2020-01-01", end="2024-01-01")

# Plot Closing Prices
plt.figure(figsize=(10,5))
plt.plot(stock['Close'], label='Apple Stock Price')
plt.legend()
plt.show()


