import pandas as pd

def pull_2014totals():
  df = pd.read_csv('/Downloads/COTHist2014.csv')
  print df.tail()

pull_2014totals()
