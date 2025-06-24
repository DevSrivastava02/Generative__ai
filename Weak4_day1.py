# Create and Analyze Random variable
import numpy as np
import matplotlib.pyplot as mlt
from scipy.stats import uniform
# Descrite Random Variable
Rice_rool=[1,2,3,4,5,6]
Probility=np.sum([1/6]*6)

mlt.bar(Rice_rool,Probility,color="green",alpha=0.5)
mlt.title("Descrite Random Variable")
mlt.show()

# Contineus Random Variable

Rice_rool1=np.linspace(0,1,100)
Probility1=uniform.pdf(Rice_rool1,loc=0,scale=1)
mlt.plot(Rice_rool1,Probility1,color="red")
mlt.title("Contineus Random Variable")
mlt.show()