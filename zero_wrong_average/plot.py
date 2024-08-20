
from .imports import * 
from matplotlib import pyplot as plt


def subset_data(df, places):
    """Subset DataFrame based on hours and place descriptions

    This function filters the DataFrame to include only rows where the 
    'hour' column is between 5 and 22 and the 'place_description' 
    column matches any of the specified places.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame to subset, containing 'hour' and 
        'place_description' columns.
    places : list of str
        A list of place names to filter the DataFrame by.

    Returns
    -------
    pandas.DataFrame
        A subset (copy) of the original DataFrame matching the specified
        criteria.

    """
    m = (df['hour'] > 5) & (df['hour'] < 22)
    m &= df['place_description'].isin(places)
    sl = df[m].copy()
    return sl


def basic_scatter(sl, width=12, subtitle=''):
    """Create a basic scatterplot of speed percentage over time of day

    This function generates a scatterplot with observations of speed 
    percentage against the hour of the day. It also plots the mean and 
    the 25th percentile of speed percentage by hour; both of which are
    calculated in this function. 

    Parameters
    ----------
    sl : pandas.DataFrame
        DataFrame containing 'hour' and 'speed_percent' columns.
    width : int, optional
        Width of the plot in inches (default is 12).
    subtitle : str, optional
        Subtitle to add below the main title (default is no subtitle).

    Returns
    -------
    matplotlib.figure.Figure
        The generated scatterplot figure.
    """
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
