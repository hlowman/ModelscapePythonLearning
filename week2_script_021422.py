# -*- coding: utf-8 -*-
"""
Spyder Editor

This is the Modelscape lesson script for February 14, 2022.
"""

# In the console, load the pandas environment.
# Run the following in the console: 
import pandas as pd

# Take a look at dataset for today.
# Can be downloaded at https://ndownloader.figshare.com/files/2292172
# Make sure the "files" pane is navigated to the appropriate directory.
pd.read_csv("surveys.csv")

# Save the dataset in as a variable.
surveys_df = pd.read_csv("surveys.csv")

# Print a preview of the data.
surveys_df

# Look at the beginning of the data
surveys_df.head()

# type() function shows what's being used to read in the data
type(surveys_df)

# data structure
surveys_df.dtypes
# object - text
# float - has decimal places

# display column names
surveys_df.columns

# dimensions
surveys_df.shape

# show first 15 lines
surveys_df.head(15)

# show the end of the dataset
surveys_df.tail

# If you type this into the console, and then hit "Tab", a
# list of possible functions should appear
# surveys_df.

# Display unique species.
pd.unique(surveys_df['species_id'])

#### Challenge - create a list of unique site ids ####
site_names = pd.unique(surveys_df['plot_id'])

# length of this new list
len(site_names)

# number of unique items in the new list
surveys_df['plot_id'].nunique()

# generate summary statistics for the weight column
surveys_df['weight'].describe()

# more specific summary statistics for the weight column
surveys_df['weight'].min()
surveys_df['weight'].max()
surveys_df['weight'].mean()
surveys_df['weight'].std()
surveys_df['weight'].count()

# group by the sex column and display the results
grouped_data = surveys_df.groupby('sex')
grouped_data
grouped_data.describe()
grouped_data.mean()

#### Challenge - how many records of males and females are there? ####
grouped_data.count()

# grouping by two groups
grouped_data2 = surveys_df.groupby(['plot_id', 'sex'])
# retains the grouping when passing to another function
grouped_data2.mean()

#### Challenge - summarize weight values for each site in your data ####
grouped_data3 = surveys_df.groupby(['plot_id'])
grouped_data3['weight'].describe()
# square brackets are the same as dollar signs in R

species_counts = surveys_df.groupby('species_id')['record_id'].count()
# first group the dataframe by species
# then counting the number of records for each species
species_counts
# groupby requires parentheses because it's a function
# and brackets precede the count because it's calling a particular column

# count a particular species
surveys_df.groupby('species_id')['record_id'].count()['DO']
# 3027 - and matches 'species_counts' above! yay!

#### Challenge - find another way to group by species and count records ####
surveys_df.groupby('species_id').count()['record_id']

# The following commands require the matplotlib package.

%matplotlib inline # check to make sure this works
# tells you whether or not matplotlib is loaded in your environment

# Quick bar chart
species_counts.plot(kind='bar');

# Create a new dataset of total counts by plot id
total_count = surveys_df.groupby('plot_id')['record_id'].nunique()
# and also plot as a bar chart
total_count.plot(kind='bar');

# Steps for making a stacked bar chart
# Make a new dataset
d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']), 'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
# Examine the new dataset
pd.DataFrame(d)
# Save in the dataset in a pandas structure
my_df = pd.DataFrame(d)
# Plot as a stacked bar chart
my_df.plot(kind = 'bar', stacked = True, title = "The title of my graph")

# End of script.
