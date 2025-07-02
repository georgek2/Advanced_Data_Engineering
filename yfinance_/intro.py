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

def cleaned_stock_data() -> pd.DataFrame:
    """
    Parameters:
    stock_data (pandas.DataFrame): The stock data DataFrame.

    Returns:
    pandas.DataFrame: A DataFrame with additional cleanup columns

    """
    # Fetch stock data
    data = get_stock_data(tickers[0])
    df = pd.DataFrame(data)  # Drop the first row if needed
    df = df.loc[:, (('Open', 'High', 'Low', 'Close', 'Volume'), 'AAPL')]
    
    df.columns= df.columns.droplevel(1)  # Drop the second level of the MultiIndex
    df.reset_index(inplace=True)  # Reset index to have 'Date' as a column
    
    # lowercase column names
    df.columns = [col.lower() for col in df.columns]

    # print(analyzed_data.isnull().sum())  # Check for missing values    
    return df

# Perform analysis
def feature_analysis_engineering(data: pd.DataFrame) -> pd.DataFrame:
    """ 
    Feature engineering and analysis of stock data.
    """
    df = data.copy()
    
    # Daily percentage change
    df['daily_%_change'] = (df['close'] - df['open']) / df['open'] * 100
    
    return df


analyzed_data = cleaned_stock_data()
print(analyzed_data)

print('**'*100)

print(feature_analysis_engineering(analyzed_data))