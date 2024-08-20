
from .imports import * 
from matplotlib import pyplot as plt


def subset_data(df, places):
    """Subset Dataframe for normal hours and places"""
    m = (df['hour'] > 5) & (df['hour'] < 22)
    m &= df['place_description'].isin(places)
    sl = df[m].copy()
    return sl


def basic_scatter(sl, width=12, subtitle=''):
    """Basic Scatterplot"""
    mean = sl.groupby('hour')['speed_percent'].mean()
    perc_25 = sl.groupby('hour')['speed_percent'].describe()['25%']

    fig, ax = plt.subplots(figsize=(width, width/1.618))
    plt.scatter(sl['hour'], sl['speed_percent'], marker='.',
                label='observation', color='#E6A067', s=125)
    plt.plot(mean.index, mean.values, ls='--', label='mean', color='#7A7A7A')
    plt.plot(perc_25.index, perc_25.values, ls='-.', label='25th Percentile',
             color='#CDBAAA')
    ax.set_xticks(range(5,23))
    ax.set_xlabel('Time of Day (Hour)')
    ax.set_ylabel('Current Speed, % of Free Flow Speed')
    title = f'Speed % over Time of Day'
    if subtitle:
        title += f"\n{subtitle}"
    ax.set_title(title)
    plt.legend()
    plt.grid()

    return fig
