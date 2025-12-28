import json 
from pathlib import Path 
from src.prices import fetch_prices 
from src.metrics import daily_returns, annualised_volatility, sharpe_ratio

def load_config(): 
    return json.loads(Path("config.json").read_text())

def main(): 
    cfg = load_config()

    prices = fetch_prices(
        ticker=cfg["ticker"],
        start=cfg["start_date"],
        end=cfg.get("end_date") 
    )

    returns = daily_returns(prices)

    vol = annualised_volatility(returns)
    sr = sharpe_ratio(returns)

    print(f"Annualised Volatility for {cfg['ticker']}: {vol:.2%}")
    print(f"Annualised Sharpe Ratio for {cfg['ticker']}: {sr:.2f}")
    # print(type(sr))

if __name__ == "__main__":
    main()