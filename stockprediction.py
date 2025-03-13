import pandas as pd
import requests
import yfinance as yf

def stockModel(): 
    tickerInput = input("Enter the Ticker: ")
    ticker = yf.Ticker(tickerInput)
    chart = ticker.history(period ="max")
    chart.plot.line(y="Close", use_index=True)
    del chart["Dividends"]
    del chart["Stock Splits"]
    print(chart)
    chart["Next Day"] = chart["Close"].shift(-1)
    chart["Target"] = 0
    for index, row in chart.iterrows():
        if row["Next Day"] > row["Close"]:
            chart.at[index, "Target"] = 1
        else:
            chart.at[index, "Target"] = 0


    print(chart)
    

stockModel()