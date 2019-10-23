import pandas as pd

iris_df = pd.read_csv('iris_dataset.csv')
#print(iris_df)

#iris_df.info()

#print(iris_df[['Class','Sepal_length']].groupby(['Class'], as_index=False).mean())

#print("The maximun length of sepal is",iris_df['Sepal_length'].min())
