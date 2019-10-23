import pandas as pd
#import numpy as np
#import matplot.pylot as plt
#import seaborn as sbn

titanic_data = pd.read_csv('titanic.csv',sep='\t')
#print(titanic_data.head())

#Info
#print(titanic_data.info())

#Describe
#print(titanic_data.describe())

#Drop unwanted columns and store in new dataframe
#new_df = titanic_data.drop(['Parch'], axis=1, inplace=False)

print(new_df.info())

#Remove unwanted values from embarked
#new_df['Embarked'] = new_df['Embarked'].fillna('S')

#print(new_df['Embarked'])

#Print max and min ages
#print(new_df['Age'].max())
#print(new_df.Age.min())
