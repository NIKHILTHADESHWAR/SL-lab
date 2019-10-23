import pandas as pd
data = pd.read_csv('employee.csv')
#print(data)

#Slice result for 1st 5 rows
#print(data[0:5]['salary'])

#print(data['salary'].head())
#Use multi axes indexing function
#print(data.loc[:,['salary','name']])

#Use multi axes indexing function
#print(data.loc[[1,3,5],['salary','name']])

#Use multi axes indexing function
#print(data.loc[2:6,['salary']])

#df1=pd.read_excel('employee.xls')
#print(df1)
