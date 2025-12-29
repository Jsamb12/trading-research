import pandas as pd 

def sma_strategy(
        prices: pd.Series, 
        short_window: int = 20, 
        long_window: int = 50, 
) -> pd.Series: 
    """
    Simple moving average crossover strategy. 
    Long when short SMA > long SMA, otherwise out (0 exposure).
    Uses a 1-day lag to avoid lookahead bias.
    """
    short_sma = prices.rolling(short_window).mean()
    long_sma = prices.rolling(long_window).mean()

    signal = (short_sma > long_sma).astype(int)
    position = signal.shift(1).fillna(0)

    asset_returns = prices.pct_change().fillna(0)
    strategy_returns = position * asset_returns

    return strategy_returns