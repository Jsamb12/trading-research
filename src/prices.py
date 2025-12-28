import yfinance as yf 
import pandas as pd

def fetch_prices(ticker: str, start: str, end: str | None = None) -> pd.DataFrame:
    data = yf.download(
        ticker,
        start=start,
        end=end,
        progress=False
    )

    if data.empty: 
        raise ValueError(f"No data found for ticker {ticker} between {start} and {end}")
    
    return data 