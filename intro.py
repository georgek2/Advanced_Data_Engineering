import pandas as pd
import yfinance as yf



tickers = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]

def get_stock_data(tickers):
    """
    Fetch historical stock data for a given ticker symbol between specified dates.

    Parameters:
    ticker (str): The stock ticker symbol.
    start_date (str): The start date in 'YYYY-MM-DD' format.
    end_date (str): The end date in 'YYYY-MM-DD' format.

    Returns:
    pandas.DataFrame: A DataFrame containing the stock data.
    """
    start_date = '2023-01-01'
    end_date = '2023-12-31'
    stock_data = yf.Tickers(tickers).history(period='1y')
    
    print(type(stock_data))
    
    return stock_data

def analyze_stock_data():
    """
    Analyze stock data to calculate daily returns and moving averages.

    Parameters:
    stock_data (pandas.DataFrame): The stock data DataFrame.

    Returns:
    pandas.DataFrame: A DataFrame with additional columns for daily returns and moving averages.

    """
    # Fetch stock data
    data = get_stock_data(tickers[0])
    df = pd.DataFrame(data)
    # stock_data['Daily Return'] = stock_data['Close'].pct_change()
    # stock_data['50 Day MA'] = stock_data['Close'].rolling(window=50).mean()
    # stock_data['200 Day MA'] = stock_data['Close'].rolling(window=200).mean()
    print(df.iloc[0:2])
    
    return df




# Perform analysis
analyzed_data = analyze_stock_data()
analyze_stock_data()
# print(analyzed_data.head(2))
