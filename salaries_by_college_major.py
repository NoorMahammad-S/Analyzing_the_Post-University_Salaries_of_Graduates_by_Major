# -*- coding: utf-8 -*-

# import pandas into your notebook and read the .csv file.
import pandas as pd
df = pd.read_csv('data/salaries_by_college_major.csv')

# the Pandas dataframe we've just created with .head(). This will show us the first 5 rows of our dataframe.
df.head()

# To see the number of rows and columns we can use the shape attribute: df.shape
df.shape

# We can access the column names directly with the columns attribute.
df.columns

# Missing Values and Junk we're going to look for NaN (Not A Number) values in our dataframe.
# NAN values are blank cells or cells that contain strings instead of numbers. Use the .isna() method and see if you can spot if there's a problem somewhere.
df.isna

# #Check the last couple of rows in the dataframe:
# We have a row that contains some information regarding the source of the data with blank values for all the other other columns.
df.tail()

# Delete the Last Row
# We don't want this row in our dataframe. There's two ways you can go about removing this row.
# The first way is to manually remove the row at index 44. The second way is to simply use the .dropna() method from pandas.
# Let's create a new dataframe without the last row and examine the last 5 rows to make sure we removed the last row:
clean_df = df.dropna()
clean_df.tail()

# To access a particular column from a data frame we can use the square bracket notation, like so:
clean_df['Starting Median Salary']

# To find the highest starting salary we can simply chain the .max() method.
clean_df.max()

#.idxmax() method will give us index for the row with the largest value.
clean_df['Starting Median Salary'].max()
clean_df['Starting Median Salary'].idxmax()

# we can use the .loc (location) property.
clean_df['Starting Median Salary'].loc[43]

# Here we are selecting both a column ('Undergraduate Major') and a row at index 43,
# so we are retrieving the value of a particular cell. You might see people using the double square brackets notation to achieve exactly the same thing:
clean_df['Undergraduate Major'].loc[43]
clean_df['Undergraduate Major'][43]

# If you don't specify a particular column you can use the .loc property to retrieve an entire row:
clean_df.loc[43]

clean_df['Mid-Career 10th Percentile Salary']

clean_df['Mid-Career 10th Percentile Salary'].idxmax()

clean_df['Undergraduate Major'].loc[8]

clean_df['Mid-Career 10th Percentile Salary'].loc[8]

clean_df.loc[8]

clean_df.min()

clean_df['Undergraduate Major'].min()

clean_df['Starting Median Salary'].min()

# The Highest Mid-Career Salary
print(clean_df['Mid-Career Median Salary'].max())
print(f"Index for the max mid career salary: {clean_df['Mid-Career Median Salary'].idxmax()}")
clean_df['Undergraduate Major'][8]

# The Lowest Starting and Mid-Career Salary
print(clean_df['Starting Median Salary'].min())
clean_df['Undergraduate Major'].loc[clean_df['Starting Median Salary'].idxmin()]

#We can also use the .loc property to access an entire row. Below I've accessed the row at the index of the smallest mid-career salary:
clean_df.loc[clean_df['Mid-Career Median Salary'].idxmin()]

# Lowest Risk Majors
# Pandas allows us to do simple arithmetic with entire columns, so all we need to do is take the difference between the two columns:
clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']

#Alternatively, you can also use the .subtract() method.
clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])

# The output of this computation will be another Pandas dataframe column. We can add this to our existing dataframe with the .insert() method:
# The first argument is the position of where the column should be inserted. In our case, it's at position 1, so the second column.
spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
clean_df.head()

#Sorting by the Lowest Spread*
# To see which degrees have the smallest spread, we can use the .sort_values() method.
# And since we are interested in only seeing the name of the degree and the major, we can pass a list of these two column names to look at the .head() of these two columns exclusively.
low_risk = clean_df.sort_values('Spread')
low_risk[['Undergraduate Major', 'Spread']].head()

# Majors with the Highest Potential
highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()

# Majors with the Greatest Spread in Salaries
highest_spread = clean_df.sort_values('Spread', ascending=False)
highest_spread[['Undergraduate Major', 'Spread']].head()

highest_potential = clean_df.sort_values('Mid-Career Median Salary', ascending=False)
highest_potential[['Undergraduate Major', 'Mid-Career Median Salary']].head()

#use the .groupby() method. This allows us to manipulate data similar to a Microsoft Excel Pivot Table.
clean_df.groupby('Group').count()

#.mean() method to find the average salary by group
clean_df.groupby('Group').mean()

#Number formats in the Output
pd.options.display.float_format = '{:,.2f}'.format 
clean_df.groupby('Group').mean()

