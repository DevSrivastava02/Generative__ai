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

# a disease affects 1% of the population
# a test is 95% accurate for disease individual and 90% accurate for non-disease individual
# find the probability of having the disease given a positive test result

# def basyes_theorm(prior,sensitivity,specification):
#     evidence=(sensitivity*prior)+((1-specification)*(1-prior))
#     posterior=(sensitivity*prior)/evidence
#     return posterior

# prior=0.01
# sensitivity=0.95
# specification=0.90

# posterior=basyes_theorm(prior,sensitivity,specification)
# print("porobility of disesas given is:",posterior)

# plot and explore differnent probability Distribution
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm,binom,poisson

# Gaussian distribution
# x=np.linspace(-4,4,100)
# y=norm.pdf(x,loc=0,scale=1)
# plt.plot(x,y,label="Gaussian")
# plt.title("Gaussian distribution")
# plt.show()

# binomial distribution
# n,p=10,0.5
# x=np.arange(0,n+1)
# y=binom.pmf(x,n,p)
# plt.bar(x,y, label="bonomial")
# plt.title("Binomal distribution")
# plt.show()

# poisson distribution

lam=3
x=np.arange(0,10)
y=poisson.pmf(x,lam)
plt.bar(x,y,label="Poisson")
plt.title("Poisson distribution")
plt.show()






