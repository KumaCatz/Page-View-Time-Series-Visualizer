import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(
    'fcc-forum-pageviews.csv',
    index_col='date',
    parse_dates=['date']
    )

# Clean data
df = df[~(
    (df['value'] >= df['value'].quantile(0.975)) |
    (df['value'] <= df['value'].quantile(0.025))
    )]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(17, 5))
    ax.plot(
        df.index,
        df['value'],
        color=(0.8, 0, 0)
        )
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df.index = df.index.to_period('M')
    df_bar = df.groupby(df.index)['value'].mean()

    # Draw bar plot
    fig, ax = plt.subplots(layout='constrained')
    df['year'] = df.index.year
    df['month'] = df.index.month

    for year, year_data in df.groupby('year'):
        for month in range(1, 13):
            print(df['month'])

    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig
draw_bar_plot()
def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
