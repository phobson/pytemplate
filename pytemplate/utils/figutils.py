import numpy as np
import matplotlib.pyplot as plt
import pandas


def _check_ax(ax):
    if ax is None:
        fig, ax = plt.subplots()
    elif isinstance(ax, plt.Axes):
        fig = ax.figure
    else:
        raise ValueError("`ax` is not an Axes object")

    return fig, ax

def hydrograph(data, ax=None, precipcol=None, flowcol=None):
    fig, ax = _check_ax(ax)
    data[precipcol].plot()
    return fig
