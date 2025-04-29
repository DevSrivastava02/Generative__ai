import pandas as pd
import numpy as np

#upload the raw data
data=pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
df=pd.DataFrame(data)
#read the first 5 line
print(df.head())
#read the last  5 line
print(df.tail())
#read the info of the data
print(df.info())
# read the mean max min etc
print(df.describe())
#read the element by selecting the indexing
print(df["sepal_width"])
#read the multiple indexing
print(df[["sepal_width","petal_length"]])
#filtue the raw data
print(df[df["petal_length"]>3])
#selcting by position
print(df.iloc[0]) # for row [0]
print(df.iloc[:,0]) # for coloum[:,0]
#selecing by label
print(df.loc[0])  # it will give u the first row by indexing
print(df.loc[:"petal_length"])