from wsgiref import headers
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

""" 
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
"""
#df = pd.read_csv('Virtual Environmen/nye tal 2017-2020.csv')


#print(df)




df = pd.DataFrame({
            "DK": [
                11345,
                22704,
                38698,
                44856
           
            ],

            "NO":[
                -593337,
                -554773,
                -567105,
                -623059

            ],
            "SE":[
                26658,
                29059,
                30044,
                33511
            
            ],
            "GER":[
                63959,
                63478,
                67055,
                63711
            ],
        
        }
    )
    

 ,          index=["A1", "B1", "C1", "D1"],

df = pd.DataFrame({
            "DK": [
                11345,
                22704,
                38698,
                44856
                ]})


df.plot.bar()
df.plot.bar('DK', 'SE')
plt.show(block = True)
