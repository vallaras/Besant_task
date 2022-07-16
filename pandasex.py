import pandas as pd
table = {'name': ['Kane', 'John', 'Mike', 'Suresh', 'Tracy'],
         'Age': [35, 25, 32, 30, 26],
         'Profession': ['Manager', 'HR', 'Analyst', 'Manager', 'HR'],
         'Sale':[422.19, 22.55, 12.66, 119.470, 200.190],
         'Salary':[12000, 10000, 8000, 14000, 11000]
	    }
data = pd.DataFrame(table)
print(data)
# load DataFrame to text file
data.to_csv('user_info.txt')
# load DataFrame to csv file with comma separator
data.to_csv('user_info.csv')
# load data from DataFrame to csv file with Tab separator
data.to_csv('user_info_new.csv', sep = '\t')
