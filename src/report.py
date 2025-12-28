from datetime import datetime 

def build_report(
        ticker: str,
        start_date: str, 
        volatility: float, 
        sharpe: float, 
        max_drawdown: float,
) -> str: 
    today = datetime.now().strftime("%d %B %Y")

    report = (
        f"# Trading Research Report\n\n"
        f"**Ticker:** {ticker}\n\n"
        f"**Start date:** {start_date}\n\n"
        f"**Report generated:** {today}\n\n"
        f"## Risk and Return Metrics\n\n"
        f"- **Annualised volatility:** {volatility:.2%}\n"
        f"- **Sharpe ratio:** {sharpe:.2f}\n"
        f"- **Maximum drawdown:** {max_drawdown:.2%}\n\n"
        f"## Interpretation\n\n"
        f"- Volatility measures the typical annual fluctuation in returns.\n"
        f"- The Sharpe ratio captures return per unit of risk.\n"
        f"- Maximum drawdown reflects the worst historical peak-to-trough loss.\n"
    )
    return report