# Data clearing and prepartion with pandas
#Handling the missing data
# 1> Method to handle the missing data

#   1> Drop Missing Values
#   (df=df.dropna())
#   (df=df.dropna(axis=1))
#   df["coloum_name"]=df["coloum_name"].fillna(0)

#   2> Fill the missing value:
#       there ara two differnt method 1> Forword 2> Backword

#       df.fillna(method="ffill")
#       df.fillna(method=bfill)


#   3> Interpolation-(linear interpolation)==based on the data we have  can fill data which is on a similiar lines to that particluar data set
#       df["coloum_name"]=df["coloum_name"].interpolate()     



