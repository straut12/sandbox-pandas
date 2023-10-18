import pandas as pd

# create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# compute correlation between all pairs of columns in df
corr_matrix = df.corr()
print(corr_matrix)

# create another DataFrame
df2 = pd.DataFrame({'A': [2, 4, 6], 'B': [8, 10, 12], 'C': [14, 16, 18]})

# compute correlation between columns of df and df2
corr_series = df.corrwith(df2)
print(corr_series)

'''corr_matrix is a correlation matrix that contains the correlation between all pairs of columns in df, 
while corr_series is a Series object that contains the correlation between the columns of df and df2.'''

#testing