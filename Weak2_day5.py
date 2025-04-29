# introduction of pandas..
# series and DataFrame..

import pandas as pd
s=pd.Series([10,20,30],index=["a","b","c"])
print(s)

data={"name":["dev","ayush","lala","jai"],
      "Age":[12,3,45,6]}
df=pd.DataFrame(data)
print(df)
