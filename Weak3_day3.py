import numpy as np
# define the gradient descent function
def Optimal_Descent(X,Y,theta,learning_rate,iteration):
    m=len(Y)
    for _ in range(iteration):
        prediction=np.dot(X,theta)
        errors=prediction-Y
        gradient=(1/m)*np.dot(X.T,errors)
        theta-=learning_rate*gradient
    return theta   
X=np.array([[1,1],[1,2],[3,4]])
Y=np.array([1,0,1])
theta=np.array([0.1,0.1])
learning_rate=0.1
iteration=1000
Optimal_theta=Optimal_Descent(X,Y,theta,learning_rate,iteration)
print("Optimal descent\n",Optimal_theta)

import sympy as sp
X=sp.Symbol('x')
f=X**2+2*X**3
derivation=sp.diff(f,X)
print(derivation) 