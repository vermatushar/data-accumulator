import pandas as pd

df = pd.read_csv('top-1m.csv', index_col = None)
print(df.head())

nonphishy_urls = df.iloc[600:750, 1].values.tolist()
print(nonphishy_urls[:5])


