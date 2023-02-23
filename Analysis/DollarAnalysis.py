__package__ = "Finance.Analysis"

from numpy import *
from matplotlib.pyplot import *
from SQL.CrudDollar import getDollarValues

def plotDollarGraph():
    title('Dollar value evolution')
    xlabel('Search number')
    ylabel('Dollar value')
    values = getDollarValues()
    x = arange(0, len(values), 1)
    plot(x, values)
    grid(True)
    show()

def getDollarAverage():
    values = getDollarValues()
    average = sum(values) / len(values)
    print('Average: ' + str(average))
    return average

def getDollarMedian():
    values = getDollarValues()
    median = median(values)
    return median

def getDollarStandardDeviation():
    values = getDollarValues()
    standard_deviation = std(values)
    return standard_deviation

def getDollarVariance():
    values = getDollarValues()
    variance = var(values)
    return variance
