import pandas as pd

data=[10,20,30]
series=pd.Series(data,index=['a','b','c'])
print(series)

data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pd.DataFrame(data)
print(df)

