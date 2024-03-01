# Course 8
# Analyzing Police Activity with pandas

# Chapter 1
# Preparing the data for analysis

#Examining the dataset
''''
Import pandas using the alias pd.
Read the file police.csv into a DataFrame named ri.
Examine the first 5 rows of the DataFrame (known as the "head").
Count the number of missing values in each column: Use .isnull() to check which DataFrame elements are missing, and then take the .sum() to count the number of True values in each column.
'''
# Import the pandas library as pd
import pandas as pd

# Read 'police.csv' into a DataFrame named ri
ri = pd.read_csv('police.csv')

# Examine the head of the DataFrame
print(ri.head())

# Count the number of missing values in each column
print(ri.isnull().sum())

#Dropping columns
''''
Examine the DataFrame's .shape to find out the number of rows and columns.
Drop both the county_name and state columns by passing the column names to the .drop() method as a list of strings.
Examine the .shape again to verify that there are now two fewer columns.
'''
# Examine the shape of the DataFrame
print(ri.shape)

# Drop the 'county_name' and 'state' columns
ri.drop(['county_name', 'state'], axis='columns', inplace=True)

# Examine the shape of the DataFrame (again)
print(ri.shape)

#Dropping rows
''''
Count the number of missing values in each column.
Drop all rows that are missing driver_gender by passing the column name to the subset parameter of .dropna().
Count the number of missing values in each column again, to verify that none of the remaining rows are missing driver_gender.
Examine the DataFrame's .shape to see how many rows and columns remain.
'''
# Count the number of missing values in each column
print(ri.isnull().sum())

# Drop all rows that are missing 'driver_gender'
ri.dropna(subset=['driver_gender'], inplace=True)

# Count the number of missing values in each column (again)
print(ri.isnull().sum())

# Examine the shape of the DataFrame
print(ri.shape)

#Fixing a data type
''''
Examine the head of the is_arrested column to verify that it contains True and False values and to check the column's data type.
Use the .astype() method to convert is_arrested to a bool column.
Check the new data type of is_arrested to confirm that it is now a bool column.
'''
# Examine the head of the 'is_arrested' column
print(ri.is_arrested.head())

# Change the data type of 'is_arrested' to 'bool'
ri['is_arrested'] = ri.is_arrested.astype('bool')

# Check the data type of 'is_arrested' 
print(ri.is_arrested.dtype)

#Combining object columns
''''
Use a string method to concatenate stop_date and stop_time (separated by a space), and store the result in combined.
Convert combined to datetime format, and store the result in a new column named stop_datetime.
Examine the DataFrame .dtypes to confirm that stop_datetime is a datetime column.
'''
# Concatenate 'stop_date' and 'stop_time' (separated by a space)
combined = ri.stop_date.str.cat(ri.stop_time, sep = ' ')

# Convert 'combined' to datetime format
ri['stop_datetime'] = pd.to_datetime(combined)

# Examine the data types of the DataFrame
print(ri.dtypes)

#Setting the index
''''
Set stop_datetime as the DataFrame index.
Examine the index to verify that it is a DatetimeIndex.
Examine the DataFrame columns to confirm that stop_datetime is no longer one of the columns.
'''
# Set 'stop_datetime' as the index
ri.set_index('stop_datetime', inplace=True)

# Examine the index
print(ri.index)

# Examine the columns
print(ri.columns)

#Examining traffic violations
''''
Count the unique values in the violation column of the ri DataFrame, to see what violations are being committed by all drivers.
Express the violation counts as proportions of the total.
'''
# Count the unique values in 'violation'
print(ri.violation.value_counts())

# Express the counts as proportions
print(ri.violation.value_counts(normalize=True))

#Comparing violations by gender
''''
Create a DataFrame, female, that only contains rows in which driver_gender is 'F'.
Create a DataFrame, male, that only contains rows in which driver_gender is 'M'.
Count the violations committed by female drivers and express them as proportions.
Count the violations committed by male drivers and express them as proportions.
'''
# Create a DataFrame of female drivers
female = ri[ri.driver_gender=='F']

# Create a DataFrame of male drivers
male = ri[ri.driver_gender=='M']

# Compute the violations by female drivers (as proportions)
print(female.violation.value_counts(normalize = True))

# Compute the violations by male drivers (as proportions)
print(male.violation.value_counts(normalize = True))

#Comparing speeding outcomes by gender
''''
Create a DataFrame, female_and_speeding, that only includes female drivers who were stopped for speeding.
Create a DataFrame, male_and_speeding, that only includes male drivers who were stopped for speeding.
Count the stop outcomes for the female drivers and express them as proportions.
Count the stop outcomes for the male drivers and express them as proportions.
'''
# Create a DataFrame of female drivers stopped for speeding
female_and_speeding = ri[(ri.driver_gender == 'F') & (ri.violation == 'Speeding')]

# Create a DataFrame of male drivers stopped for speeding
male_and_speeding = ri[(ri.driver_gender == 'M') & (ri.violation == 'Speeding')]

# Compute the stop outcomes for female drivers (as proportions)
print(female_and_speeding.stop_outcome.value_counts(normalize=True))

# Compute the stop outcomes for male drivers (as proportions)
print(male_and_speeding.stop_outcome.value_counts(normalize=True))

#Calculating the search rate
''''
Check the data type of search_conducted to confirm that it's a Boolean Series.
Calculate the search rate by counting the Series values and expressing them as proportions.
Calculate the search rate by taking the mean of the Series. (It should match the proportion of True values calculated above.)
'''
# Check the data type of 'search_conducted'
print(ri.search_conducted.dtype)

# Calculate the search rate by counting the values
print(ri.search_conducted.value_counts(normalize=True))

# Calculate the search rate by taking the mean
print(ri.search_conducted.mean())

#Comparing search rates by gender
#Filter the DataFrame to only include female drivers, and then calculate the search rate by taking the mean of search_conducted.
# Calculate the search rate for female drivers
print(ri[ri.driver_gender == 'F'].search_conducted.mean())

#Filter the DataFrame to only include male drivers, and then repeat the search rate calculation.
# Calculate the search rate for male drivers
print(ri[ri.driver_gender == 'M'].search_conducted.mean())

#Group by driver gender to calculate the search rate for both groups simultaneously. (It should match the previous results.)
# Calculate the search rate for both groups simultaneously
print(ri.groupby('driver_gender').search_conducted.mean())

#Adding a second factor to the analysis
#Use a .groupby() to calculate the search rate for each combination of gender and violation. Are males and females searched at about the same rate for each violation?
# Calculate the search rate for each combination of gender and violation
print(ri.groupby(['driver_gender', 'violation']).search_conducted.mean())

#Reverse the ordering to group by violation before gender. The results may be easier to compare when presented this way.
# Reverse the ordering to group by violation before gender
print(ri.groupby(['violation', 'driver_gender']).search_conducted.mean())

#Counting protective frisks
''''
Count the search_type values in the ri DataFrame to see how many times "Protective Frisk" was the only search type.
Create a new column, frisk, that is True if search_type contains the string "Protective Frisk" and False otherwise.
Check the data type of frisk to confirm that it's a Boolean Series.
Take the sum of frisk to count the total number of frisks.
'''
# Count the 'search_type' values
print(ri.search_type.value_counts())

# Check if 'search_type' contains the string 'Protective Frisk'
ri['frisk'] = ri.search_type.str.contains('Protective Frisk', na=False)

# Check the data type of 'frisk'
print(ri.frisk.dtype)

# Take the sum of 'frisk'
print(ri.frisk.sum())

#Comparing frisk rates by gender
''''
Create a DataFrame, searched, that only contains rows in which search_conducted is True.
Take the mean of the frisk column to find out what percentage of searches included a frisk.
Calculate the frisk rate for each gender using a .groupby().
'''
# Create a DataFrame of stops in which a search was conducted
searched = ri[ri.search_conducted == True]

# Calculate the overall frisk rate by taking the mean of 'frisk'
print(searched.frisk.mean())

# Calculate the frisk rate for each gender
print(searched.groupby('driver_gender').frisk.mean())

# Chapter 3
# Visual exploratory data analysis

#Calculating the hourly arrest rate
''''
Take the mean of the is_arrested column to calculate the overall arrest rate.
Group by the hour attribute of the DataFrame index to calculate the hourly arrest rate.
Save the hourly arrest rate Series as a new object, hourly_arrest_rate.
'''
# Calculate the overall arrest rate
print(ri.is_arrested.mean())

# Calculate the hourly arrest rate
print(ri.groupby(ri.index.hour).is_arrested.mean())

# Save the hourly arrest rate
hourly_arrest_rate = ri.groupby(ri.index.hour).is_arrested.mean()

#Plotting the hourly arrest rate
''''
Import matplotlib.pyplot using the alias plt.
Create a line plot of hourly_arrest_rate using the .plot() method.
Label the x-axis as 'Hour', label the y-axis as 'Arrest Rate', and title the plot 'Arrest Rate by Time of Day'.
Display the plot using the .show() function.
'''
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Create a line plot of 'hourly_arrest_rate'
hourly_arrest_rate.plot()

# Add the xlabel, ylabel, and title
plt.xlabel('Hour')
plt.ylabel('Arrest Rate')
plt.title('Arrest Rate by Time of Day')

# Display the plot
plt.show()

#Plotting drug-related stops
''''
Calculate the annual rate of drug-related stops by resampling the drugs_related_stop column (on the 'A' frequency) and taking the mean.
Save the annual drug rate Series as a new object, annual_drug_rate.
Create a line plot of annual_drug_rate using the .plot() method.
Display the plot using the .show() function.
'''
# Calculate the annual rate of drug-related stops
print(ri.drugs_related_stop.resample('A').mean())

# Save the annual rate of drug-related stops
annual_drug_rate = ri.drugs_related_stop.resample('A').mean()

# Create a line plot of 'annual_drug_rate'
annual_drug_rate.plot()

# Display the plot
plt.show()

#Comparing drug and search rates
''''
Calculate the annual search rate by resampling the search_conducted column, and save the result as annual_search_rate.
Concatenate annual_drug_rate and annual_search_rate along the columns axis, and save the result as annual.
Create subplots of the drug and search rates from the annual DataFrame.
Display the subplots.
'''
# Calculate and save the annual search rate
annual_search_rate = ri.search_conducted.resample('A').mean()

# Concatenate 'annual_drug_rate' and 'annual_search_rate'
annual = pd.concat([annual_drug_rate,annual_search_rate], axis='columns')

# Create subplots from 'annual'
annual.plot(subplots = True)

# Display the subplots
plt.show()

#Tallying violations by district
''''
Create a frequency table from the ri DataFrame's district and violation columns using the pd.crosstab() function.
Save the frequency table as a new object, all_zones.
Select rows 'Zone K1' through 'Zone K3' from all_zones using the .loc[] accessor.
Save the smaller table as a new object, k_zones.
'''
# Create a frequency table of districts and violations
print(pd.crosstab(ri.district,ri.violation))

# Save the frequency table as 'all_zones'
all_zones = pd.crosstab(ri.district,ri.violation)

# Select rows 'Zone K1' through 'Zone K3'
print(all_zones.loc['Zone K1':'Zone K3'])

# Save the smaller table as 'k_zones'
k_zones = all_zones.loc['Zone K1':'Zone K3']

#Plotting violations by district
#Create a bar plot of k_zones.
#Display the plot and examine it. What do you notice about each of the zones?

# Create a bar plot of 'k_zones'
k_zones.plot(kind='bar')

# Display the plot
plt.show()

#Create a stacked bar plot of k_zones.
#Display the plot and examine it. Do you notice anything different about the data than you did previously?
# Create a stacked bar plot of 'k_zones'
k_zones.plot(kind = 'bar', stacked=True)

# Display the plot
plt.show()

#Converting stop durations to numbers
''''
Print the unique values in the stop_duration column. (This has been done for you.)
Create a dictionary called mapping that maps the stop_duration strings to the integers specified above.
Convert the stop_duration strings to integers using the mapping, and store the results in a new column called stop_minutes.
Print the unique values in the stop_minutes column, to verify that the durations were properly converted to integers.
'''
# Print the unique values in 'stop_duration'
print(ri.stop_duration.unique())

# Create a dictionary that maps strings to integers
mapping = {'0-15 Min':8,'16-30 Min':23,'30+ Min':45}

# Convert the 'stop_duration' strings to integers using the 'mapping'
ri['stop_minutes'] = ri.stop_duration.map(mapping)

# Print the unique values in 'stop_minutes'
print(ri.stop_minutes.unique())

#Plotting stop length
''''
For each value in the ri DataFrame's violation_raw column, calculate the mean number of stop_minutes that a driver is detained.
Save the resulting Series as a new object, stop_length.
Sort stop_length by its values, and then visualize it using a horizontal bar plot.
Display the plot.
'''
# Calculate the mean 'stop_minutes' for each value in 'violation_raw'
print(ri.groupby('violation_raw').stop_minutes.mean())

# Save the resulting Series as 'stop_length'
stop_length = ri.groupby('violation_raw').stop_minutes.mean()

# Sort 'stop_length' by its values and create a horizontal bar plot
stop_length.sort_values().plot(kind='barh')

# Display the plot
plt.show()

#Chapter 4
#Analyzing the effect of weather on policing

#Plotting the temperature
''''
Read weather.csv into a DataFrame named weather.
Select the temperature columns (TMIN, TAVG, TMAX) and print their summary statistics using the .describe() method.
Create a box plot to visualize the temperature columns.
Display the plot.
'''
# Read 'weather.csv' into a DataFrame named 'weather'
weather = pd.read_csv('weather.csv')

# Describe the temperature columns
print(weather[['TMIN','TAVG','TMAX']].describe())

# Create a box plot of the temperature columns
weather[['TMIN','TAVG','TMAX']].plot(kind='box')

# Display the plot
plt.show()

#Plotting the temperature difference
''''
Create a new column in the weather DataFrame named TDIFF that represents the difference between the maximum and minimum temperatures.
Print the summary statistics for TDIFF using the .describe() method.
Create a histogram with 20 bins to visualize TDIFF.
Display the plot.
'''
# Create a 'TDIFF' column that represents temperature difference
weather['TDIFF'] = weather.TMAX - weather.TMIN


# Describe the 'TDIFF' column
print(weather['TDIFF'].describe())

# Create a histogram with 20 bins to visualize 'TDIFF'
weather.TDIFF.plot(kind='hist',bins=20)

# Display the plot
plt.show()

#Counting bad weather conditions
''''
Copy the columns WT01 through WT22 from weather to a new DataFrame named WT.
Calculate the sum of each row in WT, and store the results in a new weather column named bad_conditions.
Replace any missing values in bad_conditions with a 0. (This has been done for you.)
Create a histogram to visualize bad_conditions, and then display the plot.
'''
# Copy 'WT01' through 'WT22' to a new DataFrame
WT = weather.loc[:,'WT01':'WT22']

# Calculate the sum of each row in 'WT'
weather['bad_conditions'] = WT.sum(axis='columns')

# Replace missing values in 'bad_conditions' with '0'
weather['bad_conditions'] = weather.bad_conditions.fillna(0).astype('int')

# Create a histogram to visualize 'bad_conditions'
weather.bad_conditions.plot(kind='hist',bins=20)

# Display the plot
plt.show()

#Rating the weather conditions
''''
Count the unique values in the bad_conditions column and sort the index. (This has been done for you.)
Create a dictionary called mapping that maps the bad_conditions integers to strings as specified above.
Convert the bad_conditions integers to strings using the mapping and store the results in a new column called rating.
Count the unique values in rating to verify that the integers were properly converted to strings.
'''
# Count the unique values in 'bad_conditions' and sort the index
print(weather.bad_conditions.value_counts().sort_index())

# Create a dictionary that maps integers to strings
mapping = {0:'good', 1:'bad', 2:'bad', 3:'bad', 4:'bad',5:'worse',6:'worse',7:'worse',8:'worse',9:'worse'}

# Convert the 'bad_conditions' integers to strings using the 'mapping'
weather['rating'] = weather.bad_conditions.map(mapping)

# Count the unique values in 'rating'
print(weather.rating.value_counts())

#Changing the data type to category
''''
Create a list object called cats that lists the weather ratings in a logical order: 'good', 'bad', 'worse'.
Change the data type of the rating column from object to category. Make sure to use the cats list to define the category ordering.
Examine the head of the rating column to confirm that the categories are logically ordered.
'''
# Create a list of weather ratings in logical order
cats = ['good','bad','worse']

# Change the data type of 'rating' to category
weather['rating'] = weather.rating.astype('category',ordered=True,categories=cats)

# Examine the head of 'rating'
print(weather.rating.head())

#Preparing the DataFrames
''''
Reset the index of the ri DataFrame.
Examine the head of ri to verify that stop_datetime is now a DataFrame column, and the index is now the default integer index.
Create a new DataFrame named weather_rating that contains only the DATE and rating columns from the weather DataFrame.
Examine the head of weather_rating to verify that it contains the proper columns.
'''
# Reset the index of 'ri'
ri.reset_index(inplace=True)

# Examine the head of 'ri'
print(ri.head())

# Create a DataFrame from the 'DATE' and 'rating' columns
weather_rating = weather[['DATE','rating']]

# Examine the head of 'weather_rating'
print(weather_rating.head())

#Merging the DataFrames
''''
Examine the shape of the ri DataFrame.
Merge the ri and weather_rating DataFrames using a left join.
Examine the shape of ri_weather to confirm that it has two more columns but the same number of rows as ri.
Replace the index of ri_weather with the stop_datetime column.
'''
# Examine the shape of 'ri'
print(ri.shape)

# Merge 'ri' and 'weather_rating' using a left join
ri_weather = pd.merge(left=ri, right=weather_rating, left_on='stop_date', right_on='DATE', how='left')

# Examine the shape of 'ri_weather'
print(ri_weather.shape)

# Set 'stop_datetime' as the index of 'ri_weather'
ri_weather.set_index('stop_datetime', inplace=True)

#Comparing arrest rates by weather rating
#Calculate the overall arrest rate by taking the mean of the is_arrested Series.

# Calculate the overall arrest rate
print(ri_weather.is_arrested.mean())

#Calculate the arrest rate for each weather rating using a .groupby().
# Calculate the arrest rate for each 'rating'
print(ri_weather.groupby('rating').is_arrested.mean())

#Calculate the arrest rate for each combination of violation and rating. How do the arrest rates differ by group?
# Calculate the arrest rate for each 'violation' and 'rating'
print(ri_weather.groupby(['violation','rating']).is_arrested.mean())

#Selecting from a multi-indexed Series
''''
Save the output of the .groupby() operation from the last exercise as a new object, arrest_rate. (This has been done for you.)
Print the arrest_rate Series and examine it.
Print the arrest rate for moving violations in bad weather.
Print the arrest rates for speeding violations in all three weather conditions.
'''
# Save the output of the groupby operation from the last exercise
arrest_rate = ri_weather.groupby(['violation', 'rating']).is_arrested.mean()

# Print the 'arrest_rate' Series
print(arrest_rate)

# Print the arrest rate for moving violations in bad weather
print(arrest_rate.loc['Moving violation','bad'])

# Print the arrest rates for speeding violations in all three weather conditions
print(arrest_rate.loc['Speeding'])

#Reshaping the arrest rate data
''''
Unstack the arrest_rate Series to reshape it into a DataFrame.
Create the exact same DataFrame using a pivot table! Each of the three .pivot_table() parameters should be specified as one of the ri_weather columns.
'''
# Unstack the 'arrest_rate' Series into a DataFrame
print(arrest_rate.unstack())

# Create the same DataFrame using a pivot table
print(ri_weather.pivot_table(index='violation', columns='rating', values='is_arrested'))
