# Course 4
# Introduction to Importing Data in Python

# Chapter 1
# Introduction and flat files

#Importing entire text files
''''
Open the file moby_dick.txt as read-only and store it in the variable file. Make sure to pass the filename enclosed in quotation marks ''.
Print the contents of the file to the shell using the print() function. As Hugo showed in the video, you'll need to apply the method read() to the object file.
Check whether the file is closed by executing print(file.closed).
Close the file using the close() method.
Check again that the file is closed as you did above.
'''
# Open a file: file
file = open('moby_dick.txt', mode='r')

# Print it
print(file.read())

# Check whether file is closed
print(file.closed)

# Close file
file.close()

# Check whether file is closed
print(file.closed)

#Importing text files line by line
''''
Open moby_dick.txt using the with context manager and the variable file.
Print the first three lines of the file to the shell by using readline() three times within the context manager.
'''
# Read & print the first 3 lines
with open('moby_dick.txt') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())

#Using NumPy to import flat files
''''
Fill in the arguments of np.loadtxt() by passing file and a comma ',' for the delimiter.
Fill in the argument of print() to print the type of the object digits. Use the function type().
Execute the rest of the code to visualize one of the rows of the data.
'''
# Import package
import numpy as np

# Assign filename to variable: file
file = 'digits.csv'

# Load file as array: digits
digits = np.loadtxt(file, delimiter=',')

# Print datatype of digits
print(type(digits))

# Select and reshape a row
im = digits[21, 1:]
im_sq = np.reshape(im, (28, 28))

# Plot reshaped data (matplotlib.pyplot already loaded as plt)
plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()

#Customizing your NumPy import
''''
Complete the arguments of np.loadtxt(): the file you're importing is tab-delimited, you want to skip the first row and you only want to import the first and third columns.
Complete the argument of the print() call in order to print the entire array that you just imported.
'''
# Import numpy
import numpy as np

# Assign the filename: file
file = 'digits_header.txt'

# Load the data: data
data = np.loadtxt(file, delimiter='\t', skiprows=1, usecols=[0, 2])

# Print data
print(data)

#Importing different datatypes
''''
Complete the first call to np.loadtxt() by passing file as the first argument.
Execute print(data[0]) to print the first element of data.
Complete the second call to np.loadtxt(). The file you're importing is tab-delimited, the datatype is float, and you want to skip the first row.
Print the 10th element of data_float by completing the print() command. Be guided by the previous print() call.
Execute the rest of the code to visualize the data.
'''
# Assign filename: file
file = 'seaslug.txt'

# Import file: data
data = np.loadtxt(file, delimiter='\t', dtype=str)

# Print the first element of data
print(data[0])

# Import data as floats and skip the first row: data_float
data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)

# Print the 10th element of data_float
print(data_float[9])

# Plot a scatterplot of the data
plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()

#Working with mixed datatypes (2)
''''
Import titanic.csv using the function np.recfromcsv() and assign it to the variable, d. You'll only need to pass file to it because it has the defaults delimiter=',' and names=True in addition to dtype=None!
Run the remaining code to print the first three entries of the resulting array d.
'''
# Assign the filename: file
file = 'titanic.csv'

# Import file using np.recfromcsv: d
d = np.recfromcsv(file)

# Print out first three entries of d
print(d[:3])

#Using pandas to import flat files as DataFrames (1)
''''
Import the pandas package using the alias pd.
Read titanic.csv into a DataFrame called df. The file name is already stored in the file object.
In a print() call, view the head of the DataFrame.
'''
# Import pandas
import pandas as pd

# Assign the filename: file
file = 'titanic.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# View the head of the DataFrame
print(df.head())

#Using pandas to import flat files as DataFrames (2)
''''
Import the first 5 rows of the file into a DataFrame using the function pd.read_csv() and assign the result to data. You'll need to use the arguments nrows and header (there is no header in this file).
Build a numpy array from the resulting DataFrame in data and assign to data_array.
Execute print(type(data_array)) to print the datatype of data_array.
'''
# Assign the filename: file
file = 'digits.csv'

# Read the first 5 rows of the file into a DataFrame: data
data = pd.read_csv(file, nrows=5, header=None)

# Build a numpy array from the DataFrame: data_array
data_array = data.values

# Print the datatype of data_array to the shell
print(type(data_array))

#Customizing your pandas import
''''
Complete the sep (the pandas version of delim), comment and na_values arguments of pd.read_csv(). comment takes characters that comments occur after in the file, which in this case is '#'. na_values takes a list of strings to recognize as NA/NaN, in this case the string 'Nothing'.
Execute the rest of the code to print the head of the resulting DataFrame and plot the histogram of the 'Age' of passengers aboard the Titanic.
'''
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Assign filename: file
file = 'titanic_corrupt.txt'

# Import file: data
data = pd.read_csv(file, sep='\t', comment='#', na_values=['Nothing'])

# Print the head of the DataFrame
print(data.head())

# Plot 'Age' variable in a histogram
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()

# Chapter 2
# Importing data from other file types

# Import pickle package
import pickle

# Open pickle file and load data
with open('data.pkl', 'rb') as file:
    d = pickle.load(file)

# Print data
print(d)

# Print datatype
print(type(d))

#Listing sheets in Excel files
''''
Assign the spreadsheet filename (provided above) to the variable file.
Pass the correct argument to pd.ExcelFile() to load the file using pandas, assigning the result to the variable xls.
Print the sheetnames of the Excel spreadsheet by passing the necessary argument to the print() function.
'''
# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = 'battledeath.xlsx'

# Load spreadsheet: xls
xls = pd.ExcelFile(file)

# Print sheet names
print(xls.sheet_names)

#Importing sheets from Excel files
''''
Load the sheet '2004' into the DataFrame df1 using its name as a string.
Print the head of df1 to the shell.
Load the sheet 2002 into the DataFrame df2 using its index (0).
Print the head of df2 to the shell.
'''
# Load a sheet into a DataFrame by name: df1
df1 = xls.parse('2004')

# Print the head of the DataFrame df1
print(df1.head())

# Load a sheet into a DataFrame by index: df2
df2 = xls.parse(0)

# Print the head of the DataFrame df2
print(df2.head())

#Customizing your spreadsheet import
''''
Parse the first sheet by index. In doing so, skip the first row of data and name the columns 'Country' and 'AAM due to War (2002)' using the argument names. The values passed to skiprows and names all need to be of type list.
Parse the second sheet by index. In doing so, parse only the first column with the usecols parameter, skip the first row and rename the column 'Country'. The argument passed to usecols also needs to be of type list.
'''
# Parse the first sheet and rename the columns: df1
df1 = xls.parse(0, skiprows=[0], names=['Country', 'AAM due to War (2002)'])

# Print the head of the DataFrame df1
print(df1.head())

# Parse the first column of the second sheet and rename the column: df2
df2 = xls.parse(1, usecols=[0], skiprows=[0], names=['Country'])

# Print the head of the DataFrame df2
print(df2.head())

#Importing SAS files
''''
Import the module SAS7BDAT from the library sas7bdat.
In the context of the file 'sales.sas7bdat', load its contents to a DataFrame df_sas, using the method to_data_frame() on the object file.
Print the head of the DataFrame df_sas.
Execute your entire script to produce a histogram plot!
'''
# Import sas7bdat package
from sas7bdat import SAS7BDAT

# Save file to a DataFrame: df_sas
with SAS7BDAT('sales.sas7bdat') as file:
    df_sas = file.to_data_frame()

# Print head of DataFrame
print(df_sas.head())

# Plot histograms of a DataFrame feature (pandas and pyplot already imported)
pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()

#Importing Stata files
''''
Use pd.read_stata() to load the file 'disarea.dta' into the DataFrame df.
Print the head of the DataFrame df.
Visualize your results by plotting a histogram of the column disa10. We’ve already provided this code for you, so just run it!
'''
# Import pandas
import pandas as pd

# Load Stata file into a pandas DataFrame: df
df = pd.read_stata('disarea.dta')

# Print the head of the DataFrame df
print(df.head())

# Plot histogram of one column of the DataFrame
pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of countries')
plt.show()

#Using h5py to import HDF5 files
# Import packages
import numpy as np
import h5py

# Assign filename: file
file = 'LIGO_data.hdf5'

# Load file: data
data = h5py.File(file, 'r')

# Print the datatype of the loaded file
print(type(data))

# Print the keys of the file
for key in data.keys():
    print(key)

#Extracting data from your HDF5 file
''''
Assign the HDF5 group data['strain'] to group.
In the for loop, print out the keys of the HDF5 group in group.
Assign to the variable strain the values of the time series data data['strain']['Strain'] using the attribute .value.
Set num_samples equal to 10000, the number of time points we wish to sample.
Execute the rest of the code to produce a plot of the time series data in LIGO_data.hdf5.
'''
# Get the HDF5 group: group
group = data['strain']

# Check out keys of group
for key in group.keys():
    print(key)

# Set variable equal to time series data: strain
strain = data['strain']['Strain'].value

# Set number of time points to sample: num_samples
num_samples = 10000

# Set time vector
time = np.arange(0, 1, 1/num_samples)

# Plot data
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()

#Loading .mat files
''''
Import the package scipy.io.
Load the file 'albeck_gene_expression.mat' into the variable mat; do so using the function scipy.io.loadmat().
Use the function type() to print the datatype of mat to the IPython shell.
'''
# Import package
import scipy.io

# Load MATLAB file: mat
mat = scipy.io.loadmat('albeck_gene_expression.mat')

# Print the datatype type of mat
print(type(mat))

#The structure of .mat in Python
''''
se the method .keys() on the dictionary mat to print the keys. Most of these keys (in fact the ones that do NOT begin and end with '__') are variables from the corresponding MATLAB environment.
Print the type of the value corresponding to the key 'CYratioCyt' in mat. Recall that mat['CYratioCyt'] accesses the value.
Print the shape of the value corresponding to the key 'CYratioCyt' using the numpy function shape().
Execute the entire script to see some oscillatory gene expression data!
'''
# Print the keys of the MATLAB dictionary
print(mat.keys())

# Print the type of the value corresponding to the key 'CYratioCyt'
print(type(mat['CYratioCyt']))

# Print the shape of the value corresponding to the key 'CYratioCyt'
print(np.shape(mat['CYratioCyt']))

# Subset the array and plot it
data = mat['CYratioCyt'][25, 5:]
fig = plt.figure()
plt.plot(data)
plt.xlabel('time (min.)')
plt.ylabel('normalized fluorescence (measure of expression)')
plt.show()

# Chapter 3
# Working with relational databases in Python

#Creating a database engine
''''
Import the function create_engine from the module sqlalchemy.
Create an engine to connect to the SQLite database 'Chinook.sqlite' and assign it to engine.
'''
# Import necessary module
from sqlalchemy import create_engine

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

#What are the tables in the database?
''''
Import the function create_engine from the module sqlalchemy.
Create an engine to connect to the SQLite database 'Chinook.sqlite' and assign it to engine.
Using the method table_names() on the engine engine, assign the table names of 'Chinook.sqlite' to the variable table_names.
Print the object table_names to the shell.
'''
# Import necessary module
from sqlalchemy import create_engine

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Save the table names to a list: table_names
table_names = engine.table_names()

# Print the table names to the shell
print(table_names)

#The Hello World of SQL Queries!
# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine connection
con = engine.connect()

# Perform query: rs
rs = con.execute("SELECT * FROM Album")

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())

# Close connection
con.close()

# Print head of DataFrame df
print(df.head())

#Customizing the Hello World of SQL Queries
''''
Execute the SQL query that selects the columns LastName and Title from the Employee table. Store the results in the variable rs.
Apply the method fetchmany() to rs in order to retrieve 3 of the records. Store them in the DataFrame df.
Using the rs object, set the DataFrame's column names to the corresponding names of the table columns.
'''
# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("SELECT LastName, Title FROM Employee")
    df = pd.DataFrame(rs.fetchmany(size=3))
    df.columns = rs.keys()

# Print the length of the DataFrame df
print(len(df))

# Print the head of the DataFrame df
print(df.head())

#Filtering your database records using SQL's WHERE
''''
Complete the argument of create_engine() so that the engine for the SQLite database 'Chinook.sqlite' is created.
Execute the query that selects all records from the Employee table where 'EmployeeId' is greater than or equal to 6. Use the >= operator and assign the results to rs.
Apply the method fetchall() to rs in order to fetch all records in rs. Store them in the DataFrame df.
Using the rs object, set the DataFrame's column names to the corresponding names of the table columns.
'''
# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Employee WHERE EmployeeId >= 6")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print the head of the DataFrame df
print(df.head())

#Ordering your SQL records with ORDER BY
''''
Using the function create_engine(), create an engine for the SQLite database Chinook.sqlite and assign it to the variable engine.
In the context manager, execute the query that selects all records from the Employee table and orders them in increasing order by the column BirthDate. Assign the result to rs.
In a call to pd.DataFrame(), apply the method fetchall() to rs in order to fetch all records in rs. Store them in the DataFrame df.
Set the DataFrame's column names to the corresponding names of the table columns.
'''
# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine in context manager
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Employee ORDER BY BirthDate")
    df = pd.DataFrame(rs.fetchall())

    # Set the DataFrame's column names
    df.columns = rs.keys()

# Print head of DataFrame
print(df.head())

#Pandas and The Hello World of SQL Queries!
''''
Import the pandas package using the alias pd.
Using the function create_engine(), create an engine for the SQLite database Chinook.sqlite and assign it to the variable engine.
Use the pandas function read_sql_query() to assign to the variable df the DataFrame of results from the following query: select all records from the table Album.
The remainder of the code is included to confirm that the DataFrame created by this method is equal to that created by the previous method that you learned.
'''
# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query("SELECT * FROM Album", engine)

# Print head of DataFrame
print(df.head())

# Open engine in context manager and store query result in df1
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Album")
    df1 = pd.DataFrame(rs.fetchall())
    df1.columns = rs.keys()

# Confirm that both methods yield the same result
print(df.equals(df1))

#Pandas for more complex querying
''''
Using the function create_engine(), create an engine for the SQLite database Chinook.sqlite and assign it to the variable engine.
Use the pandas function read_sql_query() to assign to the variable df the DataFrame of results from the following query: select all records from the Employee table where the EmployeeId is greater than or equal to 6 and ordered by BirthDate (make sure to use WHERE and ORDER BY in this precise order).
'''
# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query(
    "SELECT * FROM Employee WHERE EmployeeId >= 6 ORDER BY BirthDate",
    engine
)

# Print head of DataFrame
print(df.head())

#The power of SQL lies in relationships between tables: INNER JOIN
''''
Assign to rs the results from the following query: select all the records, extracting the Title of the record and Name of the artist of each record from the Album table and the Artist table, respectively. To do so, INNER JOIN these two tables on the ArtistID column of both.
In a call to pd.DataFrame(), apply the method fetchall() to rs in order to fetch all records in rs. Store them in the DataFrame df.
Set the DataFrame's column names to the corresponding names of the table columns.
'''
# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("SELECT Title, Name FROM Album INNER JOIN Artist on Album.ArtistID = Artist.ArtistID")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print head of DataFrame df
print(df.head())

#Filtering your INNER JOIN
''''
Use the pandas function read_sql_query() to assign to the variable df the DataFrame of results from the following query: 
select all records from PlaylistTrack INNER JOIN Track on PlaylistTrack.TrackId = Track.TrackId that satisfy the condition Milliseconds < 250000.
'''
# Execute query and store records in DataFrame: df
df = pd.read_sql_query(
    "SELECT * FROM PlaylistTrack INNER JOIN Track ON PlaylistTrack.TrackId = Track.TrackId WHERE Milliseconds < 250000",
    engine
)

# Print head of DataFrame
print(df.head())
