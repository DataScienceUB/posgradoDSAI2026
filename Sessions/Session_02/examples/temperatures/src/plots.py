"""Plot of the cleaned readings."""
import matplotlib.pyplot as plt
import pandas as pd


def plot_stations(df: pd.DataFrame):
    """One line per station: temperature (°C) against date. Returns the matplotlib Figure."""
    fig, ax = plt.subplots(figsize=(10, 4))
    for station, d in df.groupby("station"):
        ax.plot(d["date"], d["temperature_c"], label=station)
    ax.set(ylabel="temperature (°C)", title="Daily temperature per station")
    ax.grid(alpha=0.3)
    ax.legend()
    fig.autofmt_xdate()
    return fig
