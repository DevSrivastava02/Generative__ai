# Simulate Dice Roll and Calculate Probility

# Simulate 10000 rice roll together
import numpy as np

Rool_dice=np.random.randint(1,7,size=10000)

Even_prob=np.sum(Rool_dice%2==0)/len(Rool_dice)
Pro_of_Greaterthen4=np.sum(Rool_dice>4)/len(Rool_dice)

print("Even probility is:",Even_prob)
print("The probility which greater then 4 is:",Pro_of_Greaterthen4)