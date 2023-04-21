# Create a line plot showing the number of marriages and divorces per capita in the
# U.S. between 1867 and 2014. Label both lines and show the legend.
# Don't forget to label your axes!

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('us-marriages-divorces-1867-2014.csv')
print(df.columns)
for i in range(len(df.index)):
    df.at[i, 'Marriages_per_capita'] = float(df.at[i, 'Marriages'])/float(df.at[i, 'Population'])
for i in range(len(df.index)):
    df.at[i, 'Divorces_per_capita'] = float(df.at[i, 'Divorces'])/float(df.at[i, 'Population'])

plt.plot(df['Year'], df['Marriages_per_capita'], color='green', marker='.', label='Marriages_per_capita')
plt.plot(df['Year'], df['Divorces_per_capita'], color='red', marker='.', label='Divorces_per_capita')
plt.title('number of marriages and divorces per capita in the U.S. between 1867 and 2014', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.ylabel('number of marriages and divorces per capita', fontsize=14)
plt.grid = True
plt.legend()
plt.show()