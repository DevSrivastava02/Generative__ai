import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8]])
print("Sum",np.sum(arr))
print("max",np.max(arr))
print("mean",np.mean(arr))
print("Standerd derivation",np.std(arr))
#for axis the row is axis=1
print("Sum along row",np.sum((arr),axis=1))
#for axis the coloum is axis=0
print("Sum along coloum",np.sum((arr),axis=0))


#filture the array
even=arr[arr%2==0]
print("Even:",even)
arr[arr>3]=0
print(arr)

# Random Number Generation and Setting seeds


random_array=np.random.randint(0,10 ,size=(2,3))
print(random_array)

#Random.seeds thet is hold the value as it no value change

np.random.seed(42)
random_seeds=np.random.randint(0,10 ,size=(2,3))
print(random_seeds)
