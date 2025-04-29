#Introduction tp Matplotlib for plotting===>>>> it's a foundational Python Library for creating static, interactive,and animated plots.
# it allow for detailed customerization of ploats

import matplotlib.pyplot as plt
# x=[1,2,3,4,5]
# y=[7,8,9,0,7]
# plt.plot(x,y)
# plt.show()

# Line Ploats

# x=[1,2,3,4,5]
# y=[6,7,8,9,0]
# plt.plot(x,y ,label="trend")
# plt.title("Line Plot")
# plt.xlabel("X_label")
# plt.ylabel("Y_label")
# plt.legend()
# plt.show()

#Bar chart
# Categories=["A","B","C","D"]
# values=[12,34,56,23]
# plt.bar(Categories,values,color="skyblue")
# plt.title("Bar chart")
# plt.xlabel("X_label")
# plt.ylabel("Y_label")
# plt.show()


#Histrogram chart
Data=[1,2,2,3,3,3,4,4,4,4]
plt.hist(Data,bins=4,color="skyblue",edgecolor="black",label="trends")
plt.title("Histrogram chart")
plt.xlabel("X_label")
plt.ylabel("Y_label")
plt.legend()
plt.show()