import json 
from pathlib import Path 
from src.prices import fetch_prices 
from src.metrics import daily_returns, annualised_volatility, sharpe_ratio, max_drawdown
from src.report import build_report
from src.strategy import sma_strategy
from src.plotting import plot_cum_returns
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

    bh = {
        "vol": annualised_volatility(bh_returns),
        "sharpe": sharpe_ratio(bh_returns),
        "mdd": max_drawdown(bh_returns),
    }

    sma = {
        "vol": annualised_volatility(strat_returns),
        "sharpe": sharpe_ratio(strat_returns),
        "mdd": max_drawdown(strat_returns),
    }

    report = build_report(
        ticker=cfg["ticker"],
        start_date=cfg["start_date"],
        buy_hold=bh, 
        sma=sma, 
        short_window=20,
        long_window=50,
    )
    
    output_path = Path(cfg.get("output_path", "output/report.md"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")

    print(f"Report saved to {output_path.resolve()}")

    plot_cum_returns(bh_returns, strat_returns, out_path="assets/cumulative_returns.png")

    print("Wrote assets/cumulative_returns.png")

if __name__ == "__main__":
    main()