import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
conn = sqlite3.connect('chinook.db')
sql='select * from company'
query = pd.read_sql_query(sql, conn)
df = pd.DataFrame(query)
print(df)
print('-----------------------')
df.plot(x = 'ADDRESS', y = 'SALARY')
plt.show()
df.plot(x = 'ADDRESS', y = 'SALARY', kind = 'bar')
plt.show()
print('-----------------------')
group_address = df.groupby('ADDRESS')['SALARY'].sum()
group_address.plot(kind = 'bar')
plt.show()
