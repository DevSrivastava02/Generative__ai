# calculate the integrals of the simple function
import sympy as sp
X=sp.Symbol('x')
f=sp.exp(-X)

definit_integral=sp.integrate(f,(X,0,sp.oo))
indefinit_intregal=sp.integrate(f,X)

print("definit_intregal\n",definit_integral)
print("indefinit_intregal\n",indefinit_intregal)

import numpy as np

# initialised

np.random.seed(42)
X=2*np.random.rand(100,1)
print("x:\n",X)
Y=4+3*X+np.random.randn(100,1)
print("Y:\n",Y)

# Add Baise Term in X
X_b=np.c_[np.ones((100,1)),X]
print("After the baise Term::::",X_b)




# initialised SGD function

def Stochastic_Gradient_Descent(X,Y,theta,learning_rate,iterative):
    m=len(Y)
    for _ in range(iterative):
        for i in range(m):
            random_index=np.random.randint(m)
            xi=X[ random_index:random_index+1]
            yi=Y[ random_index:random_index+1]
            gradinent=2*xi.T @ (xi@theta-yi)
            theta-=learning_rate*gradinent
    return theta

theta=np.random.randn(2,1)
learning_rate=0.01
iterative=50

Optimal_theta=Stochastic_Gradient_Descent(X_b,Y,theta,learning_rate,iterative)
print("Optimal_theta::",Optimal_theta)        
            

