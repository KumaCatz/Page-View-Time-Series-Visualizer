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
    df_bar = df.index.to_period('M')
    df_bar = df.groupby(df_bar)['value'].mean()

    # Draw bar plot
    years = tuple(df_bar.index.year.unique())

    month_names = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
    ]

    average_per_month_by_year = {month: [] for month in month_names}

    for year in years:
        for month in range(1, 13):
            month_data = df_bar[(df_bar.index.year == year) & (df_bar.index.month == month)]
            value = month_data.values[0] if not month_data.empty else 0
            average_per_month_by_year[month_names[month - 1]].append(value)

    x = list(range(len(years)))
    width = 0.03
    multiplier = 0

    fig, ax = plt.subplots(figsize=(8, 6))
    
    for month, average in average_per_month_by_year.items():
        offset = width * multiplier
        rects = ax.bar([i + offset for i in x], average, width, label=month)
        multiplier += 1

    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.set_xticks([i - 0.18 + offset for i in x], years)
    ax.legend(
        loc='upper left',
        ncols=1,
        title="Months",
        title_fontsize='small',
        fontsize='small'
        )

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

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
