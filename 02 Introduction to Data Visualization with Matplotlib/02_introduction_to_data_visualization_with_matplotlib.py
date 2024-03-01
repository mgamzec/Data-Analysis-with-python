# Course 2
# Introduction to Data Visualization with Matplotlib

# Chapter 1
# Introduction to Matplotlib

#Using the matplotlib.pyplot interface
''''
Import the matplotlib.pyplot API, using the conventional name plt.
Create Figure and Axes objects using the plt.subplots function.
Show the results, an empty set of axes, using the plt.show function.
'''
# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt

# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

# Call the show function to show the result
plt.show()

#Adding data to an Axes object
''''
Import the matplotlib.pyplot submodule as plt.
Create a Figure and an Axes object by calling plt.subplots.
Add data from the seattle_weather DataFrame by calling the Axes plot method.
Add data from the austin_weather DataFrame in a similar manner and call plt.show to show the results.
'''
# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt

# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

# Plot MLY-PRCP-NORMAL from seattle_weather against the MONTH
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])

# Plot MLY-PRCP-NORMAL from austin_weather against MONTH
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

# Call the show function
plt.show()

#Customizing data appearance
''''
Call plt.plot to plot "MLY-PRCP-NORMAL" against "MONTHS" in both DataFrames.
Pass the color key-word arguments to these commands to set the color of the Seattle data to blue ('b') and the Austin data to red ('r').
Pass the marker key-word arguments to these commands to set the Seattle data to circle markers ('o') and the Austin markers to triangles pointing downwards ('v').
Pass the linestyle key-word argument to use dashed lines for the data from both cities ('--').
'''
# Plot Seattle data, setting data appearance
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], color="b",marker="o",linestyle="--")

# Plot Austin data, setting data appearance
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"], color="r",marker="v",linestyle="--")

# Call show to display the resulting plot
plt.show()

#Customizing axis labels and adding titles
''''
Use the set_xlabel method to add the label: "Time (months)".
Use the set_ylabel method to add the label: "Precipitation (inches)".
Use the set_title method to add the title: "Weather patterns in Austin and Seattle".
'''
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

# Customize the x-axis label
ax.set_xlabel("Time (months)")

# Customize the y-axis label
ax.set_ylabel("Precipitation (inches)")

# Add the title
ax.set_title("Weather patterns in Austin and Seattle")

# Display the figure
plt.show()

#Creating small multiples with plt.subplots
''''
Create a Figure and an array of subplots with 2 rows and 2 columns.
Addressing the top left Axes as index 0, 0, plot the Seattle precipitation.
In the top right (index 0,1), plot Seattle temperatures.
In the bottom left (1, 0) and bottom right (1, 1) plot Austin precipitations and temperatures.
'''

# Create a Figure and an array of subplots with 2 rows and 2 columns
fig, ax = plt.subplots(2, 2)

# Addressing the top left Axes as index 0, 0, plot month and Seattle precipitation
ax[0, 0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])

# In the top right (index 0,1), plot month and Seattle temperatures
ax[0, 1].plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])

# In the bottom left (1, 0) plot month and Austin precipitations
ax[1, 0].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

# In the bottom right (1, 1) plot month and Austin temperatures
ax[1, 1].plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
plt.show()

#Small multiples with shared y axis
''''
Create a Figure with an array of two Axes objects that share their y-axis range.
Plot Seattle's "MLY-PRCP-NORMAL" in a solid blue line in the top Axes.
Add Seattle's "MLY-PRCP-25PCTL" and "MLY-PRCP-75PCTL" in dashed blue lines to the top Axes.
Plot Austin's "MLY-PRCP-NORMAL" in a solid red line in the top Axes and the "MLY-PRCP-25PCTL" and "MLY-PRCP-75PCTL" in dashed red lines.
'''
# Create a figure and an array of axes: 2 rows, 1 column with shared y axis
fig, ax = plt.subplots(2, 1, sharey=True)

# Plot Seattle precipitation in the top axes
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], color='b')
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-25PCTL"], color='b', linestyle='--')
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-75PCTL"], color='b', linestyle='--')

# Plot Austin precipitation in the bottom axes
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"], color='r')
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-25PCTL"], color='r', linestyle='--')
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-75PCTL"], color='r', linestyle='--')

plt.show()

# Chapter 2
# Plotting time-series

# Import pandas
import pandas as pd

# Read the data from file using read_csv
climate_change = pd.read_csv('climate_change.csv', parse_dates=["date"], index_col="date")

#Plot time-series data
''''
Add the data from climate_change to the plot: use the DataFrame index for the x value and the "relative_temp" column for the y values.
Set the x-axis label to 'Time'.
Set the y-axis label to 'Relative temperature (Celsius)'.
Show the figure.
'''
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# Add the time-series for "relative_temp" to the plot
ax.plot(climate_change.index,climate_change["relative_temp"])

# Set the x-axis label
ax.set_xlabel('Time')

# Set the y-axis label
ax.set_ylabel('Relative temperature (Celsius)')

# Show the figure
plt.show()

#Using a time index to zoom in
''''
Use plt.subplots to create a Figure with one Axes called fig and ax, respectively.
Create a variable called seventies that includes all the data between "1970-01-01" and "1979-12-31".
Add the data from seventies to the plot: use the DataFrame index for the x value and the "co2" column for the y values.
'''
import matplotlib.pyplot as plt

# Use plt.subplots to create fig and ax
fig, ax = plt.subplots()

# Create variable seventies with data from "1970-01-01" to "1979-12-31"
seventies = climate_change["1970-01-01":"1979-12-31"]

# Add the time-series for "co2" data from seventies to the plot
ax.plot(seventies.index, seventies["co2"])

# Show the figure
plt.show()

#Plotting two variables
''''
Use plt.subplots to create a Figure and Axes objects called fig and ax, respectively.
Plot the carbon dioxide variable in blue using the Axes plot method.
Use the Axes twinx method to create a twin Axes that shares the x-axis.
Plot the relative temperature variable in the twin Axes using its plot method.
'''
import matplotlib.pyplot as plt

# Initalize a Figure and Axes
fig, ax = plt.subplots()

# Plot the CO2 variable in blue
ax.plot(climate_change.index, climate_change["co2"], color='b')

# Create a twin Axes that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature in red
ax2.plot(climate_change.index, climate_change["relative_temp"], color='r')

plt.show()

#Defining a function that plots time-series data
''''
Define a function called plot_timeseries that takes as input an Axes object (axes), data (x,y), a string with the name of a color and strings for x- and y-axis labels.
Plot y as a function of in the color provided as the input color.
Set the x- and y-axis labels using the provided input xlabel and ylabel, setting the y-axis label color using color.
Set the y-axis tick parameters using the tick_params method of the Axes object, setting the colors key-word to color.
'''
# Define a function called plot_timeseries
def plot_timeseries(axes, x, y, color, xlabel, ylabel):

  # Plot the inputs x,y in the provided color
  axes.plot(x, y, color=color)

  # Set the x-axis label
  axes.set_xlabel(xlabel)

  # Set the y-axis label
  axes.set_ylabel(ylabel, color=color)

  # Set the colors tick params for y-axis
  axes.tick_params('y', colors=color)

#Using a plotting function
''''
In the provided ax object, use the function plot_timeseries to plot the "co2" column in blue, with the x-axis label "Time (years)" and y-axis label "CO2 levels".
Use the ax.twinx method to add an Axes object to the figure that shares the x-axis with ax.
Use the function plot_timeseries to add the data in the "relative_temp" column in red to the twin Axes object, with the x-axis label "Time (years)" and y-axis label "Relative temperature (Celsius)".
'''
fig, ax = plt.subplots()

# Plot the CO2 levels time-series in blue
plot_timeseries(ax, climate_change.index, climate_change["co2"], "blue", "Time (years)", "CO2 levels")

# Create a twin Axes object that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature data in red
plot_timeseries(ax, climate_change.index, climate_change["relative_temp"], "red", "Time (years)", "Relative temperature (Celsius)")

plt.show()

#Annotating a plot of time-series data
''''
Use the ax.plot method to plot the DataFrame index against the relative_temp column.
Use the annotate method to add the text '>1 degree' in the location (pd.Timestamp('2015-10-06'), 1).
'''
fig, ax = plt.subplots()

# Plot the relative temperature data
ax.plot(climate_change.index,climate_change["relative_temp"])

# Annotate the date at which temperatures exceeded 1 degree
ax.annotate(">1 degree", (pd.Timestamp('2015-10-06'), 1))

plt.show()

#Plotting time-series: putting it all together
''''
Use the plot_timeseries function to plot CO2 levels against time. Set xlabel to "Time (years)" ylabel to "CO2 levels" and color to 'blue'.
Create ax2, as a twin of the first Axes.
In ax2, plot temperature against time, setting the color ylabel to "Relative temp (Celsius)" and color to 'red'.
Annotate the data using the ax2.annotate method. Place the text ">1 degree" in x=pd.Timestamp('2008-10-06'), y=-0.2 pointing with a gray thin arrow to x=pd.Timestamp('2015-10-06'), y = 1.
'''
fig, ax = plt.subplots()

# Plot the CO2 levels time-series in blue
plot_timeseries(ax, climate_change.index, climate_change["co2"], "blue", "Time (years)", "CO2 levels")

# Create an Axes object that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature data in red
plot_timeseries(ax, climate_change.index, climate_change["relative_temp"], "red", "Time (years)", "Relative temp (Celsius)")

# Annotate point with relative temperature >1 degree
ax2.annotate(">1 degree",xy=(pd.Timestamp('2015-10-06'), 1),xytext=(pd.Timestamp('2008-10-06'),-0.2),arrowprops={"arrowstyle":"->","color":"gray"})

plt.show()

# Chapter 3
# Quantitative comparisons and statistical visualizations

#Bar chart
''''
Call the ax.bar method to plot the "Gold" column as a function of the country.
Use the ax.set_xticklabels to set the x-axis tick labels to be the country names.
In the call to ax.set_xticklabels rotate the x-axis tick labels by 90 degrees by using the rotation key-word argument.
Set the y-axis label to "Number of medals".
'''
fig, ax = plt.subplots()

# Plot a bar-chart of gold medals as a function of country
ax.bar(medals.index, medals["Gold"])

# Set the x-axis tick labels to the country names
ax.set_xticklabels(medals.index, rotation=90)

# Set the y-axis label
ax.set_ylabel("Number of medals")

plt.show()

#Stacked bar chart
''''
Call the ax.bar method to add the "Gold" medals. Call it with the label set to "Gold".
Call the ax.bar method to stack "Silver" bars on top of that, using the bottom key-word argument so the bottom of the bars will be on top of the gold medal bars, and label to add the label "Silver".
Use ax.bar to add "Bronze" bars on top of that, using the bottom key-word and label it as "Bronze".
'''
# Add bars for "Gold" with the label "Gold"
ax.bar(medals.index, medals["Gold"], label="Gold")

# Stack bars for "Silver" on top with label "Silver"
ax.bar(medals.index, medals["Silver"], bottom=medals["Gold"], label="Silver")

# Stack bars for "Bronze" on top of that with label "Bronze"
ax.bar(medals.index, medals["Bronze"], bottom=medals["Gold"] + medals["Silver"], label="Bronze")

# Display the legend
ax.legend()

plt.show()

#Creating histograms
''''
Use the ax.hist method to add a histogram of the "Weight" column from the mens_rowing DataFrame.
Use ax.hist to add a histogram of "Weight" for the mens_gymnastics DataFrame.
Set the x-axis label to "Weight (kg)" and the y-axis label to "# of observations".
'''
fig, ax = plt.subplots()
# Plot a histogram of "Weight" for mens_rowing
ax.hist(mens_rowing["Weight"])

# Compare to histogram of "Weight" for mens_gymnastics
ax.hist(mens_gymnastics["Weight"])

# Set the x-axis label to "Weight (kg)"
ax.set_xlabel("Weight (kg)")

# Set the y-axis label to "# of observations"
ax.set_ylabel("# of observations")

plt.show()

#"Step" histogram
''''
Use the hist method to display a histogram of the "Weight" column from the mens_rowing DataFrame, label this as "Rowing".
Use hist to display a histogram of the "Weight" column from the mens_gymnastics DataFrame, and label this as "Gymnastics".
For both histograms, use the 'histtype' argument to visualize the data using the 'step' type and set the number of bins to use to 5.
Add a legend to the figure, before it is displayed.
'''
fig, ax = plt.subplots()

# Plot a histogram of "Weight" for mens_rowing
ax.hist(mens_rowing["Weight"], label="Rowing",bins=5,histtype="step")

# Compare to histogram of "Weight" for mens_gymnastics
ax.hist(mens_gymnastics["Weight"], label="Gymnastics",bins=5,histtype="step")

ax.set_xlabel("Weight (kg)")
ax.set_ylabel("# of observations")

# Add the legend and show the Figure
ax.legend()
plt.show()

#Adding error-bars to a bar chart
''''
Add a bar with size equal to the mean of the "Height" column in the mens_rowing DataFrame and an error-bar of its standard deviation.
Add another bar for the mean of the "Height" column in mens_gymnastics with an error-bar of its standard deviation.
Add a label to the the y-axis: "Height (cm)".
'''
fig, ax = plt.subplots()

# Add a bar for the rowing "Height" column mean/std
ax.bar("Rowing", mens_rowing["Height"].mean(), yerr=mens_rowing["Height"].std())

# Add a bar for the gymnastics "Height" column mean/std
ax.bar("Gymnastics", mens_gymnastics["Height"].mean(), yerr=mens_gymnastics["Height"].std())

# Label the y-axis
ax.set_ylabel("Height (cm)")

plt.show()

#Adding error-bars to a plot
''''
Use the ax.errorbar method to add the Seattle data: the "MONTH" column as x values, the "MLY-TAVG-NORMAL" as y values and "MLY-TAVG-STDDEV" as yerr values.
Add the Austin data: the "MONTH" column as x values, the "MLY-TAVG-NORMAL" as y values and "MLY-TAVG-STDDEV" as yerr values.
Set the y-axis label as "Temperature (Fahrenheit)".
'''
fig, ax = plt.subplots()

# Add the Seattle temperature data in each month with standard deviation error bars
ax.errorbar(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"], yerr=seattle_weather["MLY-TAVG-STDDEV"])

# Add the Austin temperature data in each month with standard deviation error bars
ax.errorbar(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"], yerr=austin_weather["MLY-TAVG-STDDEV"])

# Set the y-axis label
ax.set_ylabel("Temperature (Fahrenheit)")

plt.show()

#Creating boxplots
''''
Create a boxplot that contains the "Height" column for mens_rowing on the left and mens_gymnastics on the right.
Add x-axis tick labels: "Rowing" and "Gymnastics".
Add a y-axis label: "Height (cm)".
'''
fig, ax = plt.subplots()

# Add a boxplot for the "Height" column in the DataFrames
ax.boxplot([mens_rowing["Height"],mens_gymnastics["Height"]])

# Add x-axis tick labels:
ax.set_xticklabels(["Rowing","Gymnastics"])

# Add a y-axis label
ax.set_ylabel("Height (cm)")

plt.show()

#Simple scatter plot
''''
Using the ax.scatter method, add the data to the plot: "co2" on the x-axis and "relative_temp" on the y-axis.
Set the x-axis label to "CO2 (ppm)".
Set the y-axis label to "Relative temperature (C)".
'''
fig, ax = plt.subplots()

# Add data: "co2" on x-axis, "relative_temp" on y-axis
ax.scatter(climate_change["co2"], climate_change["relative_temp"])

# Set the x-axis label to "CO2 (ppm)"
ax.set_xlabel("CO2 (ppm)")

# Set the y-axis label to "Relative temperature (C)"
ax.set_ylabel("Relative temperature (C)")

plt.show()

#Encoding time by color
''''
Using the ax.scatter method add a scatter plot of the "co2" column (x-axis) against the "relative_temp" column.
Use the c key-word argument to pass in the index of the DataFrame as input to color each point according to its date.
Set the x-axis label to "CO2 (ppm)" and the y-axis label to "Relative temperature (C)".
'''
fig, ax = plt.subplots()

# Add data: "co2", "relative_temp" as x-y, index as color
ax.scatter(climate_change["co2"], climate_change["relative_temp"],c=climate_change.index)

# Set the x-axis label to "CO2 (ppm)"
ax.set_xlabel("CO2 (ppm)")

# Set the y-axis label to "Relative temperature (C)"
ax.set_ylabel("Relative temperature (C)")

plt.show()

# Chapter 4
# Sharing visualizations with others

#Switching between styles
''''
Select the 'ggplot' style, create a new Figure called fig, and a new Axes object called ax with plt.subplots.
'''
# Use the "ggplot" style and create new Figure/Axes
plt.style.use("ggplot")
fig, ax = plt.subplots()
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])
plt.show()

''''
Select the 'Solarize_Light2' style, create a new Figure called fig, and a new Axes object called ax with plt.subplots.
'''
# Use the "Solarize_Light2" style and create new Figure/Axes
plt.style.use("Solarize_Light2")
fig, ax = plt.subplots()
ax.plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
plt.show()

#Saving a file several times

#Save the figure into the file my_figure.png, using the default resolution.
# Save as a PNG file
fig.savefig("my_figure.png")

#Save the figure into the file my_figure_300dpi.png and set the resolution to 300 dpi.
# Save as a PNG file with 300 dpi
fig.savefig("my_figure_300dpi.png", dpi=300)

#Set the figure size as width of 3 inches and height of 5 inches and save it as 'figure_3_5.png' with default resolution.
#Save a figure with different sizes
# Set figure dimensions and save as a PNG
fig.set_size_inches([3,5])
fig.savefig("figure_3_5.png")

#Set the figure size to width of 5 inches and height of 3 inches and save it as 'figure_5_3.png' with default settings.
# Set figure dimensions and save as a PNG
fig.set_size_inches([5,3])
fig.savefig("figure_5_3.png")

#Unique values of a column
# Extract the "Sport" column
sports_column = summer_2016_medals["Sport"]

# Find the unique values of the "Sport" column
sports = summer_2016_medals["Sport"].unique()

# Print out the unique sports values
print(sports)

fig, ax = plt.subplots()

#Automate your visualization

''''
Iterate over the values of sports setting sport as your loop variable.
In each iteration, extract the rows where the "Sport" column is equal to sport.
Add a bar to the provided ax object, labeled with the sport name, with the mean of the "Weight" column as its height, and the standard deviation as a y-axis error bar.
Save the figure into the file "sports_weights.png".
'''

# Loop over the different sports branches
for sport in sports:
  # Extract the rows only for this sport
  sport_df = summer_2016_medals[summer_2016_medals["Sport"]==sport]
  # Add a bar for the "Weight" mean with std y error bar
  ax.bar(sport, sport_df["Weight"].mean(),yerr=sport_df["Weight"].std())

ax.set_ylabel("Weight")
ax.set_xticklabels(sports, rotation=90)

# Save the figure to file
fig.savefig("sports_weights.png")
