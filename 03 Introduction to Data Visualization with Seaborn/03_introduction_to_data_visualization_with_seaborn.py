# Course 3
# Introduction to Data Visualization with Seaborn

# Chapter 1
# Introduction to Seaborn

#Making a scatter plot with lists
#Import Matplotlib and Seaborn using the standard naming convention.
# Import Matplotlib and Seaborn
import seaborn as sns
import matplotlib.pyplot as plt

#Create a scatter plot of GDP (gdp) vs. number of phones per 1000 people (phones).
# Create scatter plot with GDP on the x-axis and number of phones on the y-axis
sns.scatterplot(x=gdp, y=phones)

#Display the plot.
# Show plot
plt.show()

#Change the scatter plot so it displays the percent of the population that can read and write (percent_literate) on the y-axis.
# Change this scatter plot to have percent literate on the y-axis
sns.scatterplot(x=gdp, y=percent_literate)

# Show plot
plt.show()

#Making a count plot with a list
''''
Import Matplotlib and Seaborn using the standard naming conventions.
Use Seaborn to create a count plot with region on the y-axis.
Display the plot.
'''
# Import Matplotlib and Seaborn
import seaborn as sns
import matplotlib.pyplot as plt

# Create count plot with region on the y-axis
sns.countplot(y=region)

# Show plot
plt.show()

#"Tidy" vs. "untidy" data
''''
Read the csv file located at csv_filepath into a DataFrame named df.
Print the head of df to show the first five rows.
'''
# Import Pandas
import pandas as pd

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Print the head of df
print(df.head())

#Making a count plot with a DataFrame
''''
Import Matplotlib, Pandas, and Seaborn using the standard names.
Create a DataFrame named df from the csv file located at csv_filepath.
Use the countplot() function with the x= and data= arguments to create a count plot with the "Spiders" column values on the x-axis.
Display the plot.
'''
# Import Matplotlib, Pandas, and Seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Create a count plot with "Spiders" on the x-axis
sns.countplot(x="Spiders",data=df)

# Display the plot
plt.show()

#Hue and scatter plots
#Create a scatter plot with "absences" on the x-axis and final grade ("G3") on the y-axis using the DataFrame student_data. Color the plot points based on "location" (urban vs. rural).

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot of absences vs. final grade
sns.scatterplot(x="absences",y="G3",data=student_data,hue="location")

# Show plot
plt.show()

#Make "Rural" appear before "Urban" in the plot legend.
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Change the legend order in the scatter plot
sns.scatterplot(x="absences", y="G3", 
                data=student_data, 
                hue="location",
                hue_order=["Rural","Urban"])

# Show plot
plt.show()

#Hue and count plots
''''
Fill in the palette_colors dictionary to map the "Rural" location value to the color "green" and the "Urban" location value to the color "blue".
Create a count plot with "school" on the x-axis using the student_data DataFrame.
Add subgroups to the plot using "location" variable and use the palette_colors dictionary to make the location subgroups green and blue.
'''
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a dictionary mapping subgroup values to colors
palette_colors = {"Rural": "green", "Urban": "blue"}

# Create a count plot of school with location subgroups
sns.countplot(x="school", data=student_data,hue="location",palette=palette_colors)

# Display plot
plt.show()

# Chapter 2
# Introduction to Seaborn

#Creating subplots with col and row
#Modify the code to use relplot() instead of scatterplot().
# Change to use relplot() instead of scatterplot()
sns.relplot(x="absences", y="G3", 
                data=student_data)

# Show plot
plt.show()

#Modify the code to create one scatter plot for each level of the variable "study_time", arranged in columns.
# Change to make subplots based on study time
sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter",
            col="study_time")

# Show plot
plt.show()

#Adapt your code to create one scatter plot for each level of a student's weekly study time, this time arranged in rows.
# Change this scatter plot to arrange the plots in rows instead of columns
sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter", 
            row="study_time")

# Show plot
plt.show()

#Creating two-factor subplots
#Use relplot() to create a scatter plot with "G1" on the x-axis and "G3" on the y-axis, using the student_data DataFrame.
# Create a scatter plot of G1 vs. G3
sns.relplot(x="G1",y="G3",data=student_data,kind="scatter")

# Show plot
plt.show()

# Adjust to add subplots based on school support
sns.relplot(x="G1", y="G3", 
            data=student_data,
            kind="scatter",
            col="schoolsup",
            col_order=["yes","no"])

# Show plot
plt.show()

#Add row subplots based on whether the student received support from the family ("famsup"), ordered so that "yes" comes before "no". This will result in subplots based on two factors.
# Adjust further to add subplots based on family support
sns.relplot(x="G1", y="G3", 
            data=student_data,
            kind="scatter", 
            col="schoolsup",
            col_order=["yes", "no"],
            row="famsup",
            row_order=["yes","no"])

# Show plot
plt.show()

#Changing the size of scatter plot points
#Use relplot() and the mpg DataFrame to create a scatter plot with "horsepower" on the x-axis and "mpg" on the y-axis. Vary the size of the points by the number of cylinders in the car ("cylinders").
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot of horsepower vs. mpg

sns.relplot(x="horsepower",y="mpg",data=mpg,size="cylinders",kind="scatter")


# Show plot
plt.show()

#To make this plot easier to read, use hue to vary the color of the points by the number of cylinders in the car ("cylinders").
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot of horsepower vs. mpg
sns.relplot(x="horsepower", y="mpg", 
            data=mpg, kind="scatter", 
            size="cylinders",hue="cylinders")

# Show plot
plt.show()

#Changing the style of scatter plot points
''''
Use relplot() and the mpg DataFrame to create a scatter plot with "acceleration" on the x-axis and "mpg" on the y-axis. Vary the style and color of the plot points by country of origin ("origin").
'''
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot of acceleration vs. mpg
sns.relplot(x="acceleration", y="mpg", 
            data=mpg, kind="scatter", 
            style="origin",hue="origin")



# Show plot
plt.show()

#Interpreting line plots
#Use relplot() and the mpg DataFrame to create a line plot with "model_year" on the x-axis and "mpg" on the y-axis.
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create line plot
sns.relplot(x="model_year",y="mpg",data=mpg,kind="line")

# Show plot
plt.show()

#Visualizing standard deviation with line plots
''''
Change the plot so the shaded area shows the standard deviation instead of the confidence interval for the mean.
'''
# Make the shaded area show the standard deviation
sns.relplot(x="model_year", y="mpg",
            data=mpg, kind="line",ci="sd")

# Show plot
plt.show()

#Plotting subgroups in line plots
''''
Use relplot() and the mpg DataFrame to create a line plot with "model_year" on the x-axis and "horsepower" on the y-axis. Turn off the confidence intervals on the plot.
'''
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create line plot of model year vs. horsepower
sns.relplot(x="model_year", y="horsepower",
            data=mpg, kind="line",ci=None)

# Show plot
plt.show()

''''
Create different lines for each country of origin ("origin") that vary in both line style and color.
'''
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Change to create subgroups for country of origin
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", 
            ci=None,hue="origin")

# Show plot
plt.show()

''''
Add markers for each data point to the lines.
Use the dashes parameter to use solid lines for all countries, while still allowing for different marker styles for each line.
'''
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Add markers and make each line have the same style
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", 
            ci=None, style="origin", 
            hue="origin",markers=True,dashes=False)

# Show plot
plt.show()

# Chapter 3
# Visualizing a Categorical and a Quantitative Variable

#Count plots
#Use sns.catplot() to create a count plot using the survey_data DataFrame with "Internet usage" on the x-axis.
# Create count plot of internet usage
sns.catplot(x="Internet usage",data=survey_data,kind="count")

# Show plot
plt.show()

#Make the bars horizontal instead of vertical.
# Change the orientation of the plot
sns.catplot(y="Internet usage", data=survey_data,
            kind="count")

# Show plot
plt.show()

#Create column subplots based on "Age Category", which separates respondents into those that are younger than 21 vs. 21 and older.
# Create column subplots based on age category
sns.catplot(y="Internet usage", data=survey_data,
            kind="count", col="Age Category")

# Show plot
plt.show()

#Bar plots with percentages
#Use the survey_data DataFrame and sns.catplot() to create a bar plot with "Gender" on the x-axis and "Interested in Math" on the y-axis.
# Create a bar plot of interest in math, separated by gender
sns.catplot(x="Gender",y="Interested in Math",data=survey_data,kind="bar")


# Show plot
plt.show()

#Customizing bar plots
#Use sns.catplot() to create a bar plot with "study_time" on the x-axis and final grade ("G3") on the y-axis, using the student_data DataFrame.

# Create bar plot of average final grade in each study category
sns.catplot(x="study_time",y="G3",data=student_data,kind="bar")

# Show plot
plt.show()

#Using the order parameter, rearrange the categories so that they are in order from lowest study time to highest.
# Rearrange the categories
study_time=["<2 hours", "2 to 5 hours", "5 to 10 hours", ">10 hours"]

sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="bar",
            order=study_time)

# Show plot
plt.show()

#Update the plot so that it no longer displays confidence intervals.
# Turn off the confidence intervals
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="bar",
            order=["<2 hours", 
                   "2 to 5 hours", 
                   "5 to 10 hours", 
                   ">10 hours"],
                   ci=None)

# Show plot
plt.show()

#Create and interpret a box plot
#Use sns.catplot() and the student_data DataFrame to create a box plot with "study_time" on the x-axis and "G3" on the y-axis. Set the ordering of the categories to study_time_order.

# Specify the category ordering
study_time_order = ["<2 hours", "2 to 5 hours", 
                    "5 to 10 hours", ">10 hours"]

# Create a box plot and set the order of the categories
sns.catplot(x="study_time",y="G3",data=student_data,kind="box",order=study_time_order)

# Show plot
plt.show()

#Omitting outliers
''''
Use sns.catplot() to create a box plot with the student_data DataFrame, putting "internet" on the x-axis and "G3" on the y-axis.
Add subgroups so each box plot is colored based on "location".
Do not display the outliers.
'''
# Create a box plot with subgroups and omit the outliers
sns.catplot(x="internet", y="G3",
            data=student_data,
            kind="box",
            hue="location",
            sym="")

# Show plot
plt.show()

#Adjusting the whiskers
#Adjust the code to make the box plot whiskers to extend to 0.5 * IQR. Recall: the IQR is the interquartile range.
# Set the whiskers to 0.5 * IQR
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=0.5)

# Show plot
plt.show()

#Change the code to set the whiskers to extend to the 5th and 95th percentiles.
# Extend the whiskers to the 5th and 95th percentile
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[5,95])

# Show plot
plt.show()

#Change the code to set the whiskers to extend to the min and max values.
# Set the whiskers at the min and max values
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[0,100])

# Show plot
plt.show()

#Customizing point plots
#Use sns.catplot() and the student_data DataFrame to create a point plot with "famrel" on the x-axis and number of absences ("absences") on the y-axis.
# Create a point plot of family relationship vs. absences
sns.catplot(x="famrel",y="absences",data=student_data,kind="point")

# Show plot
plt.show()

#Add "caps" to the end of the confidence intervals with size 0.2.
# Add caps to the confidence interval
sns.catplot(x="famrel", y="absences",
			data=student_data,
            kind="point",
            capsize=0.2)
        
# Show plot
plt.show()

#Remove the lines joining the points in each category.
# Remove the lines joining the points
sns.catplot(x="famrel", y="absences",
			data=student_data,
            kind="point",
            capsize=0.2,
            join=False)
            
# Show plot
plt.show()

#Point plots with subgroups
#Use sns.catplot() and the student_data DataFrame to create a point plot with relationship status ("romantic") on the x-axis and number of absences ("absences") on the y-axis. Create subgroups based on the school that they attend ("school")
# Create a point plot with subgroups
sns.catplot(x="romantic",y="absences",data=student_data,hue="school",kind="point")

# Show plot
plt.show()

#Turn off the confidence intervals for the plot.
# Turn off the confidence intervals for this plot
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school",
            ci=None)

# Show plot
plt.show()

#Since there may be outliers of students with many absences, import the median function from numpy and display the median number of absences instead of the average.
# Import median function from numpy
from numpy import median

# Plot the median number of absences instead of the mean
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school",
            ci=None)

# Show plot
plt.show()

# Chapter 4
# Customizing Seaborn Plots

#Changing style and palette

#Set the style to "whitegrid" to help the audience determine the number of responses in each category.
# Set the style to "whitegrid"
sns.set_style("whitegrid")

# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes", 
                  "Often", "Always"]

sns.catplot(x="Parents Advice", 
            data=survey_data, 
            kind="count", 
            order=category_order)

# Show plot
plt.show()

#Set the color palette to the sequential palette named "Purples".
# Set the color palette to "Purples"
sns.set_style("whitegrid")
sns.set_palette("Purples")


# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes", 
                  "Often", "Always"]

sns.catplot(x="Parents Advice", 
            data=survey_data, 
            kind="count", 
            order=category_order)

# Show plot
plt.show()

# Change the color palette to "RdBu"
sns.set_style("whitegrid")
sns.set_palette("RdBu")

# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes", 
                  "Often", "Always"]

sns.catplot(x="Parents Advice", 
            data=survey_data, 
            kind="count", 
            order=category_order)

# Show plot
plt.show()

#Changing the scale
#Set the scale ("context") to "paper", which is the smallest of the scale options.
# Set the context to "paper"
sns.set_context("paper")

# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",
            data=survey_data, kind="bar")

# Show plot
plt.show()

#Change the context to "notebook" to increase the scale.
# Change the context to "notebook"
sns.set_context("notebook")

# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",
            data=survey_data, kind="bar")

# Show plot
plt.show()

#Change the context to "talk" to increase the scale.
# Change the context to "talk"
sns.set_context("talk")

# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",
            data=survey_data, kind="bar")

# Show plot
plt.show()

#Change the context to "poster", which is the largest scale available.
# Change the context to "poster"
sns.set_context("poster")

# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",
            data=survey_data, kind="bar")

# Show plot
plt.show()

#Using a custom palette
''''
Set the style to "darkgrid".
Set a custom color palette with the hex color codes "#39A7D0" and "#36ADA4".
'''
# Set the style to "darkgrid"
sns.set_style("darkgrid")

# Set a custom color palette
sns.set_palette(["#39A7D0","#36ADA4"])

# Create the box plot of age distribution by gender
sns.catplot(x="Gender", y="Age", 
            data=survey_data, kind="box")

# Show plot
plt.show()

#FacetGrids vs. AxesSubplots
#Identify what type of object plot g is and assign it to the variable type_of_g.
# Create scatter plot
g = sns.relplot(x="weight", 
                y="horsepower", 
                data=mpg,
                kind="scatter")

# Identify plot type
type_of_g = type(g)

# Print type
print(type_of_g)

#Adding a title to a FacetGrid object
#Add the following title to this plot: "Car Weight vs. Horsepower".
# Create scatter plot
g = sns.relplot(x="weight", 
                y="horsepower", 
                data=mpg,
                kind="scatter")

# Add a title "Car Weight vs. Horsepower"
g.fig.suptitle("Car Weight vs. Horsepower")

# Show plot
plt.show()

#Adding a title and axis labels
#Add the following title to the plot: "Average MPG Over Time".

# Create line plot
g = sns.lineplot(x="model_year", y="mpg_mean", 
                 data=mpg_mean,
                 hue="origin")

# Add a title "Average MPG Over Time"
g.set_title("Average MPG Over Time")

# Show plot
plt.show()

#Label the x-axis as "Car Model Year" and the y-axis as "Average MPG".
# Create line plot
g = sns.lineplot(x="model_year", y="mpg_mean", 
                 data=mpg_mean,
                 hue="origin")

# Add a title "Average MPG Over Time"
g.set_title("Average MPG Over Time")

# Add x-axis and y-axis labels

g.set(xlabel="Car Model Year",ylabel="Average MPG")

# Show plot
plt.show()

#Rotating x-tick labels
#Rotate the x-tick labels 90 degrees.
# Create point plot
sns.catplot(x="origin", 
            y="acceleration", 
            data=mpg, 
            kind="point", 
            join=False, 
            capsize=0.1)

# Rotate x-tick labels
plt.xticks(rotation = 90)

# Show plot
plt.show()

#Box plot with subgroups
''''
Set the color palette to "Blues".
Add subgroups to color the box plots based on "Interested in Pets".
Set the title of the FacetGrid object g to "Age of Those Interested in Pets vs. Not".
Make the plot display using a Matplotlib function.
'''
# Set palette to "Blues"
sns.set_palette("Blues")

# Adjust to add subgroups based on "Interested in Pets"
g = sns.catplot(x="Gender",
                y="Age", data=survey_data, 
                kind="box", hue="Interested in Pets")

# Set title to "Age of Those Interested in Pets vs. Not"
g.fig.suptitle("Age of Those Interested in Pets vs. Not")

# Show plot
plt.show()

#Bar plot with subgroups and subplots
''''
Set the figure style to "dark".
Adjust the bar plot code to add subplots based on "Gender", arranged in columns.
Add the title "Percentage of Young People Who Like Techno" to this FacetGrid plot.
Label the x-axis "Location of Residence" and y-axis "% Who Like Techno".
'''
# Set the figure style to "dark"
sns.set_style("dark")

# Adjust to add subplots per gender
g = sns.catplot(x="Village - town", y="Likes Techno", 
                data=survey_data, kind="bar",
                col="Gender")

# Add title and axis labels
g.fig.suptitle("Percentage of Young People Who Like Techno", y=1.02)
g.set(xlabel="Location of Residence", 
       ylabel="% Who Like Techno")

# Show plot
plt.show()
