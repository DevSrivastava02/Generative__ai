# Bayes therom
def Bayes_therom(prior,likelihood,evidence):
    return (prior*likelihood)/evidence

import numpy as np
import matplotlib.pyplot as plt

# mu,sigma=0,1
# x=np.linspace(-4,4,100)
# print(x)
# y = (1 / (np.sqrt(2 * np.pi * sigma**2))) * np.exp(-((x - mu)**2) / (2 * sigma**2))
# print(y)

# plt.plot(x,y)
# plt.title("Guassien Distribution")
# plt.show()

def basyes_theorm(prior,sensitivity,specification):
    evidence=(sensitivity*prior)+((1-specification)*(1-prior))
    posterior=(sensitivity*prior)/evidence
    return posterior

prior=0.01
sensitivity=0.95
specification=0.90

posterior=basyes_theorm(prior,sensitivity,specification)
print("porobility of disesas given is:",posterior)



