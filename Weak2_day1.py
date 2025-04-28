import numpy as np
arr=np.array([1,2,3,4,5,6])
print(arr)


#Daimension/manipulating

reshaped=arr.reshape((2,3))
print(reshaped)


#so instead of a  unit nedd one single dimensions,it's going to have two by thrice matix for me
expended=arr[:,np.newaxis]
print(expended)
# print the 3,2, matrix of zeroes
zeroes=np.zeros([3,2])
print(zeroes)
#ones of matrix 5,3
ones=np.ones([5,3])
print(ones)