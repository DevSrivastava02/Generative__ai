# introduction of pandas..
# series and DataFrame..

import pandas as pd
s=pd.Series([10,20,30],index=["a","b","c"])
print(s)

data={"name":["dev","ayush","lala","jai"],
      "Age":[12,3,45,6]}
df=pd.DataFrame(data)
print(df)


# Loading data from csv,excel,and other

# import pandas as pd
# df=pd.read_csv("data.csv")
# df=pd.read_excel("data.text")
# df=pd.DataFrame(data)


# #to save the Data
# df.to_csv("data.csv")
# df.to_excel("data.text" ,index=False)

