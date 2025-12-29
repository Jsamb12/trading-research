from datetime import datetime

def build_report(
    ticker: str,
    start_date: str,
    buy_hold: dict,
    sma: dict,
    short_window: int,
    long_window: int,
) -> str:
    today = datetime.now().strftime("%d %B %Y")

    report = (
        f"# Trading Research Report\n\n"
        f"**Ticker:** {ticker}\n\n"
        f"**Start date:** {start_date}\n\n"
        f"**Report generated:** {today}\n\n"
        f"## Strategy Comparison\n\n"
        f"| Strategy | Annualised Volatility | Sharpe | Max Drawdown |\n"
        f"|---|---:|---:|---:|\n"
        f"| Buy & Hold | {buy_hold['vol']:.2%} | {buy_hold['sharpe']:.2f} | {buy_hold['mdd']:.2%} |\n"
        f"| SMA({short_window}/{long_window}) | {sma['vol']:.2%} | {sma['sharpe']:.2f} | {sma['mdd']:.2%} |\n\n"
        f"## Notes\n\n"
        f"- This is a historical backtest for learning and comparison.\n"
        f"- The SMA strategy is long-only and switches between 0% and 100% exposure.\n"
        f"- Signals are shifted by 1 day to avoid look-ahead bias.\n"
    )

    return report