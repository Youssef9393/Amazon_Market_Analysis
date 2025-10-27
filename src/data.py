import yfinance as yf
import pandas as pd

# This for Download dataset of amazon between 2020-2025
def download_amzn(start='2020-01-01', end='2025-10-24'):
    t = yf.Ticker('AMZN')
    df = t.history(start=start, end=end)
    df = df[['Open','High','Low','Close','Volume']]
    df.index = pd.to_datetime(df.index)
    return df

# Save
df = download_amzn()
df.to_csv('./data/raw/amzn.parquet')