# Probability theory and random variable

# Basic probablity
# Import liberary
# *********************************************
# from itertools import product
# Sample_value=list(range(1,7))
# even=[2,4,6]

# Even_prob=len(even)/len(Sample_value)
# print("The probility of even outcome is:",Even_prob)

#******************************************************
# Random variable
import numpy as np

Outcome=np.array([1,2,3,4,5,6])
Probility=np.array([1/6]*6)

# Expection E[x]

Expection1=np.sum(Outcome*Probility)
print("Expextion(mean):",Expection1)

# Varienace V[x]
Variance=np.sum((Outcome-Expection1)**2 *Probility)
print("Varienace is:",Variance)

# Standard Derivation
Std=np.sqrt(Variance)
print("Standard derivation:",Std)