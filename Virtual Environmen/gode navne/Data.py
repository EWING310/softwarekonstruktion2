from wsgiref import headers
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
 
file = open ('Virtual Environmen/t2020_rd320_page_linear.csv')
csvreader = csv.reader(file)
header = next(csvreader)
header

rows = []

for row in csvreader:
    rows.append(row)
rows

print(header)
print(rows)
file.close()

dg = pd.read_csv('Virtual Environmen/nye tal 2017-2020.csv')


print(dg)





df = pd.DataFrame(
        {
            "DK":  [
                11345,
                22704,
                38698,
                44856,
            ],
            "NO": [
                -593337,
                -554773,
                -567105,
                -623059,
            ],
            "GER": [
                63959,
                63478,
                67055,
                63711,
            ],
            "CYP": [
                95927,
                92491,
                92792,
                93077,
            ]
        }
        ,   index=['2017','2018','2019','2020'],
    )

df.plot.bar()
plt.title('Energiafhængighed i EU')
plt.show(block=True)
