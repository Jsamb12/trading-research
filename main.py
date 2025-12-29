import json 
from pathlib import Path 
from src.prices import fetch_prices 
from src.metrics import daily_returns, annualised_volatility, sharpe_ratio, max_drawdown
from src.report import build_report
from src.strategy import sma_strategy
from pathlib import Path

def load_config(): 
    return json.loads(Path("config.json").read_text())

def print_metrics(name, rets):
    vol = annualised_volatility(rets)
    sr = sharpe_ratio(rets)
    mdd = max_drawdown(rets)

    print(f"Metrics for {name}:")
    print(f"  Annualised Volatility: {vol:.2%}")
    print(f"  Sharpe Ratio: {sr:.2f}")
    print(f"  Maximum Drawdown: {mdd:.2%}")
    print("")

def main(): 
    cfg = load_config()

    prices = fetch_prices(
        ticker=cfg["ticker"],
        start=cfg["start_date"],
        end=cfg.get("end_date") 
    )

    close = prices["Close"]

    # Buy & Hold returns (daily)
    bh_returns = close.pct_change().dropna()

    #  Strategy returns (same date index as close)
    strat_returns = sma_strategy(close)

    #  Align them (strategy returns starts with 0 because of fillna(0)
    strat_returns = strat_returns.loc[bh_returns.index]

    returns = daily_returns(prices)

    print_metrics("Buy & Hold", bh_returns)
    print_metrics("SMA (20/50)", strat_returns)

    vol = annualised_volatility(returns)
    sr = sharpe_ratio(returns)
    mdd = max_drawdown(returns)

    report = build_report(
        ticker=cfg["ticker"],
        start_date=cfg["start_date"],
        volatility=vol, 
        sharpe=sr,  
        max_drawdown=mdd,
    )
    
    output_path = Path(cfg.get("output_path", "output/report.md"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")

    print(f"Report saved to {output_path.resolve()}")

    # TEMP sanity checks
    tmp = sma_strategy(close)
    print("\n Strategy returns head:")
    print(tmp.head(10))
    print("Any positive/negative returns?", (tmp != 0).any())

if __name__ == "__main__":
    main()