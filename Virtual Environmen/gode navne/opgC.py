import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

A = np.random.rand(100,3)

#Opg1
print(A)

#Opg2
df = pd.DataFrame(
    {'Uge 1': A[:,0],
     'Uge 2': A[:,1], 
     'Uge 3': A[:,2] } 
     )
print(df)

#Opg3
df.plot.line()
(df).plpt
plt.show()

