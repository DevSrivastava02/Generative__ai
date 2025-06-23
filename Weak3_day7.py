# Hand on exercise
# Implement the /mathmatical formula for linear regression


#  initalized


import numpy as np
np.random.seed(42)
X= 2*np.random.rand(100,1)
Y=4+3*X*np.random.randn(100,1)

# adding bais
X_b=np.c_[np.ones((100,1)),X]

theta=np.random.randn(2,1)
learning_rate=0.01
iteration=1000
def predict(X,theta):
    return np.dot(X,theta)

def gradient(X,Y,theta ,learning_rate,iteration):
    m=len(Y)
    for _ in range(iteration):
        gradient=(1/m)*np.dot(X.T,(np.dot(X,theta)-Y))
        theta-=learning_rate*gradient
        return theta

def mean_squred_error(y_true,y_pred):
    return np.mean((y_true-y_pred)**2)

def r_squred(y_true,y_pred):
    ss_res=np.sum((y_true-y_pred)**2)
    ss_tot=np.sum((y_true-np.mean(y_true))**2)
    return 1-(ss_res/ss_tot)

# Perform gradient decesent

prior_optimal=gradient(X_b,Y,theta,learning_rate,iteration)
print("Optimal theta :",prior_optimal)

# Evalution and predition

y_pred=predict(X_b,prior_optimal)

print("Y predition",y_pred)

msd=mean_squred_error(Y, y_pred)
print("mean squred error",msd)
rrs=r_squred(Y,y_pred)
print("RR squred",rrs)


