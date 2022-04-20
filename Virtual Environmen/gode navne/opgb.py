from statistics import mean
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame(
        {
            "jan": [
                23,
                14,
                55,
                23,
            ],
            "feb": [
                55,
                22,
                25,
                45,
            ],
            "mar": [
                10,
                60,
                30,
                40,
            ],
        }
        ,   index=['A1','B1','C1','D1'],
    )
#Opg 1 og 2
print(df)

#Opg3
print(df["feb"])

#Opg 4
print(sum(df["jan"]))
print(max(df["jan"]))
print(mean(df["jan"]))

#Opg5
#navne på rækker er ændret
df.plot.bar()
df.plot.bar('jan',' ')
plt.show(block=True)
