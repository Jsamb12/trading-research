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
    std = returns.std()
    if isinstance(std, pd.Series):
        std = std.iloc[0]
    return std * np.sqrt(TRADING_DAYS)

def sharpe_ratio(returns: pd.Series, risk_free_rate: float = 0.0) -> float:
    """
    Annualised Sharpe ratio (assuming daily returns).
    Risk-free rate is annualised.
    """
    excess_returns = returns - (risk_free_rate / TRADING_DAYS)

    mean = excess_returns.mean()
    std = excess_returns.std()

    if isinstance(mean, pd.Series):
        mean = mean.iloc[0]
    if isinstance(std, pd.Series):
        std = std.iloc[0]  
    return (mean / std) * np.sqrt(TRADING_DAYS)

def max_drawdown(returns: pd.Series) -> float: 
    """
    Maximum drawdown from daily returns.
    Returned as a negative number (e.g. -0.2 for a 20% drawdown).
    """
    cumulative = (1 + returns).cumprod()
    running_max = cumulative.cummax()
    drawdown = cumulative / running_max - 1
    
    mdd = drawdown.min()
    if isinstance(mdd, pd.Series):
        mdd = mdd.iloc[0]
    return mdd 