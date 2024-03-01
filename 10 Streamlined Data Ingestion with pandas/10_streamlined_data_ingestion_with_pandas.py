# Course 10
# Streamlined Data Ingestion with pandas

#Chapter1
#Data from CSV
#Get data from CSVs
''''
Import the pandas library as pd.
Use read_csv() to load vt_tax_data_2016.csv and assign it to the variable data.
View the first few lines of the data frame with the head() method. This code has been written for you.
'''
# Import pandas as pd
import pandas as pd

# Read the CSV and assign it to the variable data
data = pd.read_csv("vt_tax_data_2016.csv")

# View the first few lines of data
print(data.head())

#Get data from other flat files
''''
Import pandas with the alias pd.
Load vt_tax_data_2016.tsv, making sure to set the correct delimiter with the sep keyword argument.
'''
# Import pandas with the alias pd
import pandas as pd

# Load TSV using the sep keyword argument to set delimiter
data = pd.read_csv("vt_tax_data_2016.tsv", sep="\t")

# Plot the total number of tax returns by income group
counts = data.groupby("agi_stub").N1.sum()
counts.plot.bar()
plt.show()

#Import a subset of columns
''''
Create a list of columns to use: zipcode, agi_stub (income group), mars1 (number of single households), MARS2 (number of households filing as married), and NUMDEP (number of dependents).
Create a data frame from vt_tax_data_2016.csv that uses only the selected columns.
'''
# Create list of columns to use
cols = ['zipcode','agi_stub','mars1','MARS2','NUMDEP']

# Create data frame from csv using only selected columns
data = pd.read_csv("vt_tax_data_2016.csv", usecols=cols)

# View counts of dependents and tax returns by income level
print(data.groupby("agi_stub").sum())

#Import a file in chunks
''''
Use nrows and skiprows to make a data frame, vt_data_next500, with the next 500 rows.
Set the header argument so that pandas knows there is no header row.
Name the columns in vt_data_next500 by supplying a list of vt_data_first500's columns to the names argument.
'''
# Create data frame of next 500 rows with labeled columns
vt_data_next500 = pd.read_csv("vt_tax_data_2016.csv", 
                       		  nrows=500,
                       		  skiprows=500,
                       		  header=None,
                       		  names=vt_data_first500)

# View the Vermont data frames to confirm they're different
print(vt_data_first500.head())
print(vt_data_next500.head())

#Specify data types
#Load vt_tax_data_2016.csv with no arguments and view the data frame's dtypes attribute. Note the data types of zipcode and agi_stub.
# Load csv with no additional arguments
data = pd.read_csv("vt_tax_data_2016.csv")

# Print the data types
print(data.dtypes)

''''
Create a dictionary, data_types, specifying that agi_stub is "category" data and zipcode is string data.
Reload the CSV with the dtype argument and the dictionary to set the correct column data types.
View the data frame's dtypes attribute.
'''
# Create dict specifying data types for agi_stub and zipcode
data_types = {"agi_stub": "category",
			  "zipcode": str}

# Load csv using dtype to set correct data types
data = pd.read_csv("vt_tax_data_2016.csv", dtype=data_types)

# Print data types of resulting frame
print(data.dtypes.head())

#Set custom NA values
# Create dict specifying that 0s in zipcode are NA values
null_values = {"zipcode": 0}

# Load csv using na_values keyword argument
data = pd.read_csv("vt_tax_data_2016.csv", 
                   na_values=null_values)

# View rows with NA ZIP codes
print(data[data.zipcode.isna()])

#Skip bad data
#Try to import the file vt_tax_data_2016_corrupt.csv without any keyword arguments.

try:
  # Import the CSV without any keyword arguments
  data = pd.read_csv("vt_tax_data_2016_corrupt.csv")
  
  # View first 5 records
  print(data.head())
  
except pd.io.common.CParserError:
    print("Your data contained rows that could not be parsed.")

#Import vt_tax_data_2016_corrupt.csv with the error_bad_lines parameter set to skip bad records.
try:
  # Import CSV with error_bad_lines set to skip bad records
  data = pd.read_csv("vt_tax_data_2016_corrupt.csv", 
                     error_bad_lines=False)
 
  # View first 5 records
  print(data.head())
  
except pd.io.common.CParserError:
    print("Your data contained rows that could not be parsed.")

#Update the import with the warn_bad_lines parameter set to issue a warning whenever a bad record is skipped.
try:
  # Set warn_bad_lines to issue warnings about bad records
  data = pd.read_csv("vt_tax_data_2016_corrupt.csv", 
                     error_bad_lines=False, 
                     warn_bad_lines=True)
  
  # View first 5 records
  print(data.head())
  
except pd.io.common.CParserError:
    print("Your data contained rows that could not be parsed.")


#Importing Data From Excel Files
#Get data from a spreadsheet
''''
Load the pandas library as pd.
Read in fcc_survey.xlsx and assign it to the variable survey_responses.
Print the first few records of survey_responses.
'''
# Load pandas as pd
import pandas as pd

# Read spreadsheet and assign it to survey_responses
survey_responses = pd.read_excel("fcc_survey.xlsx")

# View the head of the data frame
print(survey_responses.head())

#Load a portion of a spreadsheet
''''
Create a single string, col_string, specifying that pandas should load column AD and the range AW through BA.
Load fcc_survey_headers.xlsx', setting skiprows and usecols to skip the first two rows of metadata and get only the columns in col_string.
View the selected column names in the resulting data frame.
'''
# Create string of lettered columns to load
col_string = "AD, AW:BA"

# Load data with skiprows and usecols set
survey_responses = pd.read_excel("fcc_survey_headers.xlsx", 
                        skiprows=2, 
                        usecols=col_string)

# View the names of the columns selected
print(survey_responses.columns)

#Select a single sheet
#Create a data frame from the second workbook sheet by passing the sheet's position to sheet_name.
# Create df from second worksheet by referencing its position
responses_2017 = pd.read_excel("fcc_survey.xlsx",
                               sheet_name=1)

# Graph where people would like to get a developer job
job_prefs = responses_2017.groupby("JobPref").JobPref.count()
job_prefs.plot.barh()
plt.show()

#Create a data frame from the 2017 sheet by providing the sheet's name to read_excel().
# Create df from second worksheet by referencing its name
responses_2017 = pd.read_excel("fcc_survey.xlsx",
                               sheet_name="2017")

# Graph where people would like to get a developer job
job_prefs = responses_2017.groupby("JobPref").JobPref.count()
job_prefs.plot.barh()
plt.show()

#Select multiple sheets
#Load both the 2016 and 2017 sheets by name with a list and one call to read_excel().
# Load both the 2016 and 2017 sheets by name
all_survey_data = pd.read_excel("fcc_survey.xlsx",
                                sheet_name=['2016', '2017'])

# View the data type of all_survey_data
print(type(all_survey_data))

#Load the 2016 sheet by its position (0) and 2017 by name. Note the sheet names in the result.
# Load all sheets in the Excel file
all_survey_data = pd.read_excel("fcc_survey.xlsx",
                                sheet_name=[0,'2017'])

# View the sheet names in all_survey_data
print(all_survey_data.keys())

#Load all sheets in the Excel file without listing them all.
# Load all sheets in the Excel file
all_survey_data = pd.read_excel("fcc_survey.xlsx",
                                sheet_name = None)

# View the sheet names in all_survey_data
print(all_survey_data.keys())

#Work with multiple spreadsheets
''''
Create an empty data frame, all_responses.
Set up a for loop to iterate through the values in the responses dictionary.
Append each data frame to all_responses and reassign the result to the same variable name.
'''
# Create an empty data frame
all_responses = pd.DataFrame()

# Set up for loop to iterate through values in responses
for df in responses.values():
  # Print the number of rows being added
  print("Adding {} rows".format(df.shape[0]))
  # Append df to all_responses, assign result
  all_responses = all_responses.append(df)

# Graph employment statuses in sample
counts = all_responses.groupby("EmploymentStatus").EmploymentStatus.count()
counts.plot.barh()
plt.show()

#Set Boolean columns
#Count NA values in each column of survey_data with isna() and sum(). Note which columns besides ID.x, if any, have zero NAs.
# Load the data
survey_data = pd.read_excel("fcc_survey_subset.xlsx")

# Count NA values in each column
print(survey_data.isna().sum())

''''
Set read_excel()'s dtype argument to load the HasDebt column as Boolean data.
Supply the Boolean column name to the print statement to view financial burdens by group.
'''
# Set dtype to load appropriate column(s) as Boolean data
survey_data = pd.read_excel("fcc_survey_subset.xlsx",
                            dtype={"HasDebt": bool})

# View financial burdens by Boolean group
print(survey_data.groupby("HasDebt").sum())

#Set custom true/false values
#Load the Excel file, specifying "Yes" as a true value and "No" as a false value.
# Load file with Yes as a True value and No as a False value
survey_subset = pd.read_excel("fcc_survey_yn_data.xlsx",
                              dtype={"HasDebt": bool,
                              "AttendedBootCampYesNo": bool},
                              true_values=["Yes"],
                              false_values=["No"])

# View the data
print(survey_subset.head())

#Parse simple dates
''''
Load fcc_survey.xlsx, making sure that the Part1StartTime column is parsed as datetime data.
View the first few values of the survey_data.Part1StartTime to make sure it contains datetimes.
'''
# Load file, with Part1StartTime parsed as datetime data
survey_data = pd.read_excel("fcc_survey.xlsx",
                            parse_dates=["Part1StartTime"])

# Print first few values of Part1StartTime
print(survey_data.Part1StartTime.head())

#Get datetimes from multiple columns
# Create dict of columns to combine into new datetime column
datetime_cols = {"Part2Start": ["Part2StartDate","Part2StartTime"]}


# Load file, supplying the dict to parse_dates
survey_data = pd.read_excel("fcc_survey_dts.xlsx",
                            parse_dates = datetime_cols)

# View summary statistics about Part2Start
print(survey_data.Part2Start.describe())

#Parse non-standard date formats
#Parse Part2EndTime using pd.to_datetime(), the format keyword argument, and the format string you just identified. Assign the result back to the Part2EndTime column.

# Parse datetimes and assign result back to Part2EndTime
survey_data["Part2EndTime"] = pd.to_datetime(survey_data["Part2EndTime"], 
                                             format="%m%d%Y %H:%M:%S")

#Print the head of Part2EndTime to confirm the column now contains datetime values.
# Parse datetimes and assign result back to Part2EndTime
survey_data["Part2EndTime"] = pd.to_datetime(survey_data["Part2EndTime"], 
                                             format="%m%d%Y %H:%M:%S")

# Print first few values of Part2EndTime
print(survey_data.Part2EndTime.head())

#Chapter 3
#Importing Data from Databases

#Import the create_engine() function from sqlalchemy.
# Import sqlalchemy's create_engine() function
from sqlalchemy import create_engine

# Import sqlalchemy's create_engine() function
from sqlalchemy import create_engine

# Create the database engine
engine = create_engine("sqlite:///data.db")

# View the tables in the database
print(engine.table_names())

#Load entire tables
#Use read_sql() to load the hpd311calls table by name, without any SQL.
# Load libraries
import pandas as pd
from sqlalchemy import create_engine

# Create the database engine
engine = create_engine('sqlite:///data.db')

# Load hpd311calls without any SQL
hpd_calls = pd.read_sql("hpd311calls", engine)

# View the first few rows of data
print(hpd_calls.head())

#Use read_sql() and a SELECT * ... SQL query to load the entire weather table.
# Create the database engine
engine = create_engine("sqlite:///data.db")

# Create a SQL query to load the entire weather table
query = """
SELECT * 
  FROM weather;
"""

# Load weather with the SQL query
weather = pd.read_sql("weather", engine)

# View the first few rows of data
print(weather.head())

#Selecting columns with SQL
''''
Create a database engine for data.db.
Write a SQL query that SELECTs the date, tmax, and tmin columns from the weather table.
Make a data frame by passing the query and engine to read_sql() and assign the resulting data frame to temperatures.
'''
# Create database engine for data.db
engine = create_engine("sqlite:///data.db")

# Write query to get date, tmax, and tmin from weather
query = """
SELECT date, 
       tmax, 
       tmin
  FROM weather;
"""

# Make a data frame by passing query and engine to read_sql()
temperatures = pd.read_sql(query,engine)

# View the resulting data frame
print(temperatures)

#Selecting rows
''''
Create a query that selects all columns of records in hpd311calls that have 'SAFETY' as their complaint_type.
Use read_sql() to query the database and assign the result to the variable safety_calls.
Run the last section of code to create a graph of safety call counts in each borough.
'''
# Create query to get hpd311calls records about safety
query = """
select *
from hpd311calls
where complaint_type = 'SAFETY';
"""

# Query the database and assign result to safety_calls
safety_calls = pd.read_sql(query,engine)

# Graph the number of safety calls by borough
call_counts = safety_calls.groupby('borough').unique_key.count()
call_counts.plot.barh()
plt.show()

#Filtering on multiple conditions
''''
Create a query that selects records in weather where tmax is less than or equal to 32 degrees OR snow is greater than or equal to 1 inch.
Use read_sql() to query the database and assign the result to the variable wintry_days.
View summary statistics with the describe() method to make sure all records in the data frame meet the given criteria.
'''
# Create query for records with max temps <= 32 or snow >= 1
query = """
SELECT * 
  FROM weather
 WHERE tmax <= 32
    OR snow >= 1;
"""

# Query database and assign result to wintry_days
wintry_days = pd.read_sql(query, engine)

# View summary stats about the temperatures
print(wintry_days.describe())

#Getting distinct values
''''
Create a query that gets DISTINCT values for borough and complaint_type (in that order) from hpd311calls.
Use read_sql() to load the results of the query to a data frame, issues_and_boros.
Print the data frame to check if the assumption that all issues besides literature requests appear with boroughs listed.
'''
# Create query for unique combinations of borough and complaint_type
query = """
SELECT DISTINCT borough, 
       complaint_type
  from hpd311calls;
"""

# Load results of query to a data frame
issues_and_boros = pd.read_sql(query,engine)

# Check assumption about issues and boroughs
print(issues_and_boros)

#Counting in groups
''''
Create a SQL query that gets the complaint_type column and counts of all records from hpd311calls, grouped by complaint_type.
Create a data frame with read_sql() of call counts by issue, calls_by_issue.
Run the last section of code to graph the number of calls for each housing issue.
'''
# Create query to get call counts by complaint_type
query = """
SELECT complaint_type, 
       COUNT(*)
  FROM hpd311calls
 GROUP BY complaint_type;
"""

# Create data frame of call counts by issue
calls_by_issue = pd.read_sql(query, engine)

# Graph the number of calls for each housing issue
calls_by_issue.plot.barh(x="complaint_type")
plt.show()

#Working with aggregate functions
#Create a query to pass to read_sql() that will get months and the MAX value of tmax by monthfrom weather.
# Create a query to get month and max tmax by month
query = """
SELECT month, 
       MAX(tmax)
  FROM weather 
 GROUP BY month;"""

# Get data frame of monthly weather stats
weather_by_month = pd.read_sql(query, engine)

# View weather stats by month
print(weather_by_month)

#Modify the query to also get the MIN tmin value for each month.
# Create a query to get month, max tmax, and min tmin by month
query = """
SELECT month, 
	   MAX(tmax), 
       MIN(tmin)
  FROM weather 
 GROUP BY month;
"""

# Get data frame of monthly weather stats
weather_by_month = pd.read_sql(query, engine)

# View weather stats by month
print(weather_by_month)

#Modify the query to also get the total precipitation (prcp) for each month.
# Create query to get temperature and precipitation by month
query = """
SELECT month, 
        MAX(tmax), 
        MIN(tmin),
        SUM(prcp)
  FROM weather 
 GROUP BY month;
"""

# Get data frame of monthly weather stats
weather_by_month = pd.read_sql(query, engine)

# View weather stats by month
print(weather_by_month)

#Joining tables
''''
Complete the query to join weather to hpd311calls by their date and created_date columns, respectively.
Query the database and assign the resulting data frame to calls_with_weather.
Print the first few rows of calls_with_weather to confirm all columns were joined.
'''
# Query to get hpd311calls and precipitation values
query = """
SELECT hpd311calls.*, weather.prcp
  FROM hpd311calls
  JOIN weather
    ON hpd311calls.created_date = weather.date;"""

# Load query results into the leak_calls data frame
leak_calls = pd.read_sql(query, engine)

# View the data frame
print(leak_calls.head())

#Modify query to get only rows that have 'WATER LEAK' as their complaint_type.
# Query to get water leak calls and daily precipitation
query = """
SELECT hpd311calls.*, weather.prcp
  FROM hpd311calls
  JOIN weather
    ON hpd311calls.created_date = weather.date
 WHERE hpd311calls.complaint_type = 'WATER LEAK';"""

# Load query results into the leak_calls data frame
leak_calls = pd.read_sql(query, engine)

# View the data frame
print(leak_calls.head())

#Joining, filtering, and aggregating
''''
Complete the query to get created_date and counts of records whose complaint_type is HEAT/HOT WATER from hpd311calls by date.
Create a data frame,df, containing the results of the query.
'''
# Query to get heat/hot water call counts by created_date
query = """
SELECT hpd311calls.created_date, 
       COUNT(*)
  FROM hpd311calls 
 WHERE hpd311calls.complaint_type = 'HEAT/HOT WATER' 
 GROUP BY hpd311calls.created_date;
"""

# Query database and save results as df
df = pd.read_sql(query, engine)

# View first 5 records
print(df.head())

''''
Modify the query to join tmax and tmin from the weather table. 
(There is only one record per date in weather, so we do not need SQL's MAX and MIN functions here.) 
Join the tables on created_date in hpd311calls and date in weather.
'''
# Modify query to join tmax and tmin from weather by date
query = """
SELECT hpd311calls.created_date, 
       COUNT(*), 
       weather.tmax, 
       weather.tmin
  FROM hpd311calls 
       JOIN weather 
       ON hpd311calls.created_date = weather.date
 WHERE hpd311calls.complaint_type = 'HEAT/HOT WATER' 
 GROUP BY hpd311calls.created_date;
 """

# Query database and save results as df
df = pd.read_sql(query, engine)

# View first 5 records
print(df.head())

#Chapter 4
#Importing JSON Data and Working with APIs

#Load JSON data
''''
Get a sense of the contents of dhs_daily_report.json, which are printed in the console.
Load pandas as pd.
Use read_json() to load dhs_daily_report.json to a data frame, pop_in_shelters.
View summary statistics about pop_in_shelters with the data frame's describe() method.
'''
# Load pandas as pd
import pandas as pd

# Load the daily report to a data frame
pop_in_shelters = pd.read_json("dhs_daily_report.json")

# View summary stats about pop_in_shelters
print(pop_in_shelters.describe())

#Work with JSON orientations
#Try loading dhs_report_reformatted.json without any keyword arguments.
try:
    # Load the JSON without keyword arguments
    df = pd.read_json("dhs_report_reformatted.json")
    
    # Plot total population in shelters over time
    df["date_of_census"] = pd.to_datetime(df["date_of_census"])
    df.plot(x="date_of_census", 
            y="total_individuals_in_shelter")
    plt.show()
    
except ValueError:
    print("pandas could not parse the JSON.")

#Load dhs_report_reformatted.json to a data frame with orient specified.
try:
    # Load the JSON with orient specified
    df = pd.read_json("dhs_report_reformatted.json",
                      orient="split")
    
    # Plot total population in shelters over time
    df["date_of_census"] = pd.to_datetime(df["date_of_census"])
    df.plot(x="date_of_census", 
            y="total_individuals_in_shelter")
    plt.show()
    
except ValueError:
    print("pandas could not parse the JSON.")

#Get data from an API
''''
Get data about New York City cafes from the Yelp API (api_url) with requests.get(). The necessary params and headers information has been provided.
Extract the JSON data from the response with its json() method, and assign it to data.
Load the cafe listings to the data frame cafes with pandas's DataFrame() function. The listings are under the "businesses" key in data.
Print the data frame's dtypes to see what information you're getting.
'''
api_url = "https://api.yelp.com/v3/businesses/search"

# Get data about NYC cafes from the Yelp API
response = requests.get(api_url, 
                headers=headers, 
                params=params)

# Extract JSON data from the response
data = response.json()

# Load data to a data frame
cafes = pd.DataFrame(data["businesses"])

# View the data's dtypes
print(cafes.dtypes)

#Set API parameters
''''
Create a dictionary, parameters, with the term and location parameters set to search for "cafe"s in "NYC".
Query the Yelp API (api_url) with requests's get() function and the headers and params keyword arguments set. Save the result as response.
Extract the JSON data from response with the appropriate method. Save the result as data.
Load the "businesses" values in data to the data frame cafes and print the head.
'''
# Create dictionary to query API for cafes in NYC
parameters = {"term":"cafe",
          	  "location":"NYC"}

# Query the Yelp API with headers and params set
response = requests.get(api_url,
                params=parameters,
                headers=headers)

# Extract JSON data from response
data = response.json()

# Load "businesses" values to a data frame and print head
cafes = pd.DataFrame(data["businesses"])
print(cafes.head())

#Set request headers
''''
Create a dictionary, headers, that passes the formatted key string to the "Authorization" header value.
Query the Yelp API (api_url) with get() and the necessary headers and parameters. Save the result as response.
Extract the JSON data from response. Save the result as data.
Load the "businesses" values in data to the data frame cafes and print the names column.
'''
# Create dictionary that passes Authorization and key string
headers = {"Authorization": "Bearer {}".format(api_key)}

# Query the Yelp API with headers and params set
response = requests.get(api_url,
                params=params,
                headers=headers)

# Extract JSON data from response
data = response.json()

# Load "businesses" values to a data frame and print names
cafes = pd.DataFrame(data["businesses"])
print(cafes.name)

# Load json_normalize()
from pandas.io.json import json_normalize

# Isolate the JSON data from the API response
data = response.json()

# Flatten business data into a data frame, replace separator
cafes = json_normalize(data["businesses"],
                       sep="_")

# View data
print(cafes.head())

#Handle deeply nested data
#Use json_normalize() to flatten records under the businesses key in data, setting underscores (_) as separators.
# Flatten businesses records and set underscore separators
flat_cafes = json_normalize(data["businesses"],
                            sep="_")

# View the data
print(flat_cafes.head())

#Specify the record_path to the categories data.
# Specify record path to get categories data
flat_cafes = json_normalize(data["businesses"],
                            sep="_",
                    		record_path="categories")

# View the data
print(flat_cafes.head())

#Set the meta keyword argument to get business name, alias, rating, and the attributes nested under coordinates: latitude and longitude.
#Add "biz_" as a meta_prefix to prevent duplicate column names.
# Load other business attributes and set meta prefix
flat_cafes = json_normalize(data["businesses"],
                            sep="_",
                    		record_path="categories",
                    		meta=["name", 
                                  "alias",  
                                  "rating",
                          		  ["coordinates", "latitude"], 
                          		  ["coordinates", "longitude"]],
                    		meta_prefix="biz_")

# View the data
print(flat_cafes.head())

#Append data frames
''''
Add an "offset" parameter to params so that the Yelp API call will get cafes 51-100.
Append the results of the API call to top_50_cafes, setting ignore_index so rows will be renumbered.
Print the shape of the resulting data frame, cafes, to confirm there are 100 records.
'''
# Add an offset parameter to get cafes 51-100
params = {"term": "cafe", 
          "location": "NYC",
          "sort_by": "rating", 
          "limit": 50,
          "offset": 50}

result = requests.get(api_url, headers=headers, params=params)
next_50_cafes = json_normalize(result.json()["businesses"])

# Append the results, setting ignore_index to renumber rows
cafes = top_50_cafes.append(next_50_cafes, ignore_index=True)

# Print shape of cafes
print(cafes.shape)

#Merge data frames
''''
Use the DataFrame method to merge cafes and crosswalk on location_zip_code and zipcode, respectively. Assign the result to cafes_with_pumas.
Merge pop_data into cafes_with_pumas on their puma fields. Save the result as cafes_with_pop.
'''
# Merge crosswalk into cafes on their zip code fields
cafes_with_pumas = cafes.merge(crosswalk, 
                   			   left_on="location_zip_code", 
                               right_on="zipcode")

# Merge pop_data into cafes_with_pumas on puma field
cafes_with_pop = cafes_with_pumas.merge(pop_data, on="puma")

# View the data
print(cafes_with_pop.head())
