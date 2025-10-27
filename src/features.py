import pandas as pd
import ta

def add_technical_indicators(df):
    df = df.copy()
    df['MA20'] = df['Close'].rolling(20).mean()
    df['MA50'] = df['Close'].rolling(50).mean()
    df['BB_high'] = df['Close'].rolling(20).mean() + 2 * df['Close'].rolling(20).std()
    df['BB_low'] = df['Close'].rolling(20).mean() - 2 * df['Close'].rolling(20).std()
    df['rsi'] = ta.momentum.RSIIndicator(df['Close']).rsi()
    return df


