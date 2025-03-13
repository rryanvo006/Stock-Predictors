import pandas as pd
import requests
import yfinance as yf

def stockModel(): 
    tickerInput = input("Enter the Ticker: ")
    ticker = yf.Ticker(tickerInput)
    chart = ticker.history(period ="max")
    print(chart)
    print("ryna and aiv)")

stockModel()

def diddytracker():
    return True