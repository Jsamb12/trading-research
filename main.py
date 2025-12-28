import json 
from pathlib import Path 
from src.prices import fetch_prices 
from src.metrics import daily_returns, annualised_volatility, sharpe_ratio, max_drawdown
from src.report import build_report
from pathlib import Path

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

if __name__ == "__main__":
    main()