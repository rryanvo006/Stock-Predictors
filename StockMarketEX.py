import pandas as pd 
import yfinance as yf
import matplotlib.pyplot as plt

# Load Data
# stock = yf.download("AAPL", start="2020-01-01", end="2024-01-01")

# # Plot Closing Prices
#     plt.figure(figsize=(10,5))
#     plt.plot(stock['Close'], label='Apple Stock Price')
#     plt.legend()
#     plt.show()

sp500 = yf.Ticker("^GSPC")
sp500 = sp500.history(period = "max")
print(sp500)

print(sp500.index)




