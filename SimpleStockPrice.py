import pandas as pd
import yfinance as yf
import streamlit as st

# streamlit run SimpleStockPrice.py - to run the app in browser
st.write(""" 
# Simple Stock Price App

Shown are the stock closing price and volume of Google!

""")

# define the ticker symbol
tickerSymbol = 'GOOGL'
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2022-5-31')
# open    High    Low   Close    Volume   dividends   Stock Splits


st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
