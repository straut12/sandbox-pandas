import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

# create a DataFrame
df = pd.read_csv('CD-ALL-synthetic-data').assign(date=lambda data: pd.to_datetime(data["Date"], format="%Y-%m-%d")) # was not uploading with csv extension

# compute correlation between all pairs of columns in df
#corr_matrix = df.corr()

# compute correlation between columns of df and df2
#corr_series = df.corrwith(df2)

'''corr_matrix is a correlation matrix that contains the correlation between all pairs of columns in df, 
while corr_series is a Series object that contains the correlation between the columns of df and df2.'''

# visualize the correlation matrix using a heatmap
#sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')

'''The df.corr() method in pandas computes the pairwise correlation between columns of a DataFrame using the 
Pearson correlation coefficient by default. The Pearson correlation coefficient is a measure of the linear 
correlation between two variables, and it assumes that the variables are normally distributed and have a 
linear relationship.

You can also specify a different correlation method using the method parameter of the corr() method. 
For example, you can use the Spearman rank correlation coefficient by setting method='spearman', 
or the Kendall rank correlation coefficient by setting method='kendall'. These rank correlation 
coefficients are non-parametric measures of the correlation between two variables, and they do not 
assume that the variables are normally distributed or have a linear relationship.'''