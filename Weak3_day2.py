# advance liner algebra concept

# calculate Determinant and inverse of the matrix
import numpy as np
A=np.array([[1,2,3],[3,4,6],[7,8,9]])

Determinant=np.linalg.det(A)

Inverse=np.linalg.inv(A)

print("Determinant \n",Determinant)
print("Inverse\n",Inverse)


# Eigenvector and Eigenvalue

Eigenvalue,Eigenvector=np.linalg.eig(A)
print("Eigenvalue\n",Eigenvalue)
print("Eigenvector\n",Eigenvector)

# Perform the SVD single value Decompostion
u,s,vt=np.linalg.svd(A)
print("u\n",u)
print("Singular value:\n",s)
print("vt\n",vt)

# Reconstruct
Sigma=np.zeros((3,3))
np.fill_diagonal(Sigma,s)
reconstruct=u@Sigma@vt

print("Original martix are:\n",reconstruct)

