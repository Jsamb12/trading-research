import pandas as pd
import numpy as np 

TRADING_DAYS = 252

def daily_returns(prices: pd.DataFrame) -> pd.Series: 
    """Calculate daily returns from price data."""

    if "Adj Close" in prices.columns: 
        series = prices["Adj Close"]
    elif "Close" in prices.columns: 
        series = prices["Close"]
    else:
        raise KeyError(f"Expected 'Adj Close' or 'Close' column in prices DataFrame, found: {prices.columns.tolist()}")
    returns = series.pct_change().dropna()
    return returns

def annualised_volatility(returns: pd.Series) -> float: 
    """
    Annualised volatility from daily returns.
    """
    return float(returns.std() * np.sqrt(TRADING_DAYS))

def sharpe_ratio(returns: pd.Series, risk_free_rate: float = 0.0) -> float:
    """
    Annualised Sharpe ratio (assuming daily returns).
    Risk-free rate is annualised.
    """
    excess_returns = returns - (risk_free_rate / TRADING_DAYS)
    return float((excess_returns.mean() / excess_returns.std()) * np.sqrt(TRADING_DAYS))