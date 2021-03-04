import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], c='b', s=8)

    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    slope, intercept, r, p, std_err = linregress(x, y)
    x1 = range(1880, 2050)

    def myfunc(x1):
      return slope * x1 + intercept

    model = list(map(myfunc, x1))

    plt.plot(x1, model, 'r', label="best fit line 1")

    # Create second line of best fit
    xnew = df[df['Year'] >= 2000]['Year']
    ynew = df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level']

    fit2 = linregress(xnew, ynew)

    slope2 = fit2.slope
    intercept2 = fit2.intercept

    x2 = range(2000,2050)
    y2 = slope2 * x2 + intercept2

    plt.plot(x2, y2,'g', label="best fit line 2")
    #plt.legend()

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()