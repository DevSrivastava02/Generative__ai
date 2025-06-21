import numpy as np
v=np.array([1,2,3,4])
m=np.array([[1,2],[3, 4]])
n=np.array([[3,4],[5,6],[7,8],[9,8]])
# Addition

# print("Addtion\n",m+n)

# # subtraction
# print("Addtion\n",m-n)

# # vector
# print("Addtion\n",3*n)

# # Matrix_vector Multiplication
# v1=np.array([1,-1])
# multiplication=np.dot(m,v1)
# print(multiplication)

# Special matrix multiplication
i=np.eye(2)
z=np.zeros((3,3))
d=np.diag([2,3,4])
print("Spical matrix multiplication\n",np.dot(m,i))