__package__ = "Finance"

from Scrappers.DollarGoogleScraperBS import getValue, getDate
from SQL.CrudDollar import insertDollar
from Analysis.DollarAnalysis import plotGraph, getAverage

def main():
    insertDollar(getValue(), getDate())
    print('Average: ' + str(getAverage()))
    plotGraph()
    

if __name__ == '__main__':
   main()
 