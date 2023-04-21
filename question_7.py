# Create a vertical bar chart comparing the number of marriages and divorces per
# capita in the U.S. between 1900, 1950, and 2000.
# Don't forget to label your axes!

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('us-marriages-divorces-1867-2014.csv')

print(df.columns)
df = df.set_index('Year')
print(df.index)
df = df.filter(items=[1900, 1950, 2000], axis=0)
df = df.reset_index()

for i in range(len(df.index)):
    df.at[i, 'Marriages_per_capita'] = float(df.at[i, 'Marriages'])/float(df.at[i, 'Population'])
for i in range(len(df.index)):
    df.at[i, 'Divorces_per_capita'] = float(df.at[i, 'Divorces'])/float(df.at[i, 'Population'])

plt.plot(df['Year'], df['Marriages_per_capita'], color='green', marker='.', label='Marriages_per_capita')
plt.plot(df['Year'], df['Divorces_per_capita'], color='red', marker='.', label='Divorces_per_capita')
plt.title('number of marriages and divorces per capita in the U.S. between 1900, 1950 and 2000', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.ylabel('number of marriages and divorces per capita', fontsize=14)
plt.grid = True
plt.legend()
plt.show()