import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def plot_cum_returns(bh_returns, strat_returns, out_path="output/cumulative_returns.png"):
    bh_curve = (1 + bh_returns).cumprod()
    strat_curve = (1 + strat_returns).cumprod()

    plt.figure()
    plt.plot(bh_curve, label="Buy & Hold")
    plt.plot(strat_curve, label="SMA Strategy")
    plt.title("Cumulative Returns")
    plt.xlabel("Date")
    plt.ylabel("Growth of £1")
    plt.legend()

    path = Path(out_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(path, dpi=200, bbox_inches="tight")
    plt.close()