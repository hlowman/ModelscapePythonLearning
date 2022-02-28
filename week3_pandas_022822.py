# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 12:19:40 2022

@author: Alice Carter
"""

import pandas as pd


# download csv here:  https://ndownloader.figshare.com/files/2292172
surveys_df = pd.read_csv('C:/Users/Alice Carter/git/python_sandbox/surveys.csv')

# subset a python object with []
survey_species = surveys_df['species_id']

# or use column name as an attribute:
surveys_df.species_id

# Select the species and plot columns from the DataFrame
surveys_df[['species_id', 'plot_id']]

# What happens when you flip the order?
surveys_df[['plot_id', 'species_id']]

# What happens if you ask for a column that doesn't exist?
surveys_df['speciess']


# remember: Python uses zero based indexing
# create a list:
a = [1, 2, 3, 4, 5]

a[0]
a[5]
a[len(a)]

### Slicing
surveys_df[0:3]
# the start index is included while the stop one is not

# if no start index is included it is assumed to be 0
surveys_df[:5] 

# similarly, if no end value is included it goes to the end of the list:
surveys_df[35540:]
# or you can count backwards to select the bottom rows:
surveys_df[-1:]


### copying vs referencing objects
# Using the 'copy() method'
true_copy_surveys_df = surveys_df.copy()

# Using the '=' operator
ref_surveys_df = surveys_df

# reassign values:
ref_surveys_df[0:3] = 0

ref_surveys_df.head()
surveys_df.head()


### subsetting rows and columns
surveys_df = pd.read_csv('C:/Users/Alice Carter/git/python_sandbox/surveys.csv')
# iloc[row slicing, column slicing]
surveys_df.iloc[0:3,1:4]

# Select all columns for rows of index values 0 and 10
surveys_df.loc[[0, 10], :]

# What does this do?
surveys_df.loc[0, ['species_id', 'plot_id', 'weight']]

# What happens when you type the code below?
surveys_df.loc[[0, 10, 35549], :]

# challenge
surveys_df[0:1]
surveys_df[:-1]
surveys_df.iloc[0:4, 1:4]
surveys_df.loc[0:4, 1:4]

# Subset with a criteria
surveys_df[surveys_df.year == 2002]
surveys_df[surveys_df.year != 2002]
surveys_df[(surveys_df.year == 1999) & (surveys_df.weight <= 8)]

surveys_df[surveys_df['species_id'].isin(['NL', 'DM'])]

surveys_df[surveys_df['species_id'].isin(['NL', 'DM'])].shape

surveys_df[surveys_df['weight']>=0]
surveys_df[~surveys_df['sex'].isin(['M', 'F'])]

# using masks
pd.isnull(surveys_df)
surveys_df[pd.isnull(surveys_df).any(axis = 1)]

# What does this do?
empty_weights = surveys_df[pd.isnull(surveys_df['weight'])]['weight']
print(empty_weights)

new_df = surveys_df[~surveys_df['sex'].isin(['M', 'F'])]
new_df.loc[:,'sex'] = 'X'

new_df[pd.isnull(new_df)].shape

# challenge 2
mf_df = surveys_df[surveys_df['sex'].isin(['M','F']) &\
                   surveys_df['weight']>= 0]

by_site_sex = mf_df.groupby(['plot_id', 'sex'])
site_sex_mean = by_site_sex['weight'].mean()
spc = site_sex_mean.unstack()
s_plot = spc.plot(kind = 'bar', stacked = True, title = "Average Weight by Site")
s_plot.set_ylabel('Weight')
s_plot.set_xlabel('Plot ID')
s_plot
