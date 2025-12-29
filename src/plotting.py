import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def plot_cum_returns(bh_returns: pd.Series, strat_returns: pd.Series, outpath: str = "output.cumulative_returns.png") -> None: 
    bh_curve = (1 + bh_returns).cumprod()
    start_currve = (1 + strat_returns).cumnprod()

    plt.figure()
    bh_curve.plot(label="Buy & Hold")
    strat_curve.plot(label="SMA Strategy")
    plt.title("Cumulative Returns")
    plt.xlabel("Date")
    plt.ylabel("Growth of £1")
    plt.legend()

    path = Path(outpath)
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(path)
    plt.close()