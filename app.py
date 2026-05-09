import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
st.title("Stock Market Analysis System")

symbol = st.text_input("Enter Stock Symbol (Example: AAPL)")

if symbol:
    try:
        stock = yf.Ticker(symbol)

        info = stock.info
        history = stock.history(period="1mo")

        if history.empty:
            st.error("Invalid stock symbol or no data found.")
        else:
            st.subheader("Stock Information")
            st.write("Company Name:", info.get("longName", "Not Available"))
            st.write("Current Price:", info.get("currentPrice", "Not Available"))

            st.subheader("Historical Data")
            st.dataframe(history)

            st.subheader("Stock Price Trend")

            fig, ax = plt.subplots()
            ax.plot(history.index, history["Close"])
            ax.set_xlabel("Date")
            ax.set_ylabel("Closing Price")
            ax.set_title(f"{symbol} Stock Trend")

            st.pyplot(fig)

    except Exception as e:
        st.error(f"Error: {e}")
