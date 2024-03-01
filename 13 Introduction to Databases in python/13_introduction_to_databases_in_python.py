# Course 10
# Streamlined Data Ingestion with pandas

#Chapter 1
#Basics of Relational Databases

#Engines and connection strings
''''
Import create_engine from the sqlalchemy module.
Using the create_engine() function, create an engine for a local file named census.sqlite with sqlite as the driver. Be sure to enclose the connection string within quotation marks.
Print the output from the .table_names() method on the engine.
'''
# Import create_engine
from sqlalchemy import create_engine

# Create an engine that connects to the census.sqlite file: engine
engine = create_engine('sqlite:///census.sqlite')

# Print table names
print(engine.table_names())

#Autoloading Tables from a database
''''
Import the Table and MetaData from sqlalchemy.
Create a MetaData object: metadata
Reflect the census table by using the Table object with the arguments:
The name of the table as a string ('census').
The metadata you just initialized.
autoload=True
The engine to autoload with - in this case, engine.
Print the details of census using the repr() function.
'''
# Import create_engine, MetaData, and Table
from sqlalchemy import create_engine, MetaData, Table

# Create engine: engine
engine = create_engine('sqlite:///census.sqlite')

# Create a metadata object: metadata
metadata = MetaData()

# Reflect census table from the engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Print census table metadata
print(repr(census))

#Viewing Table details
''''
Reflect the census table as you did in the previous exercise using the Table() function.
Print a list of column names of the census table by applying the .keys() method to census.columns.
Print the details of the census table using the metadata.tables dictionary along with the repr() function. To do this, first access the 'census' key of the metadata.tables dictionary, and place this inside the provided repr() function.
'''
from sqlalchemy import create_engine, MetaData, Table

engine = create_engine('sqlite:///census.sqlite')

metadata = MetaData()

# Reflect the census table from the engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Print the column names
print(census.columns.keys())

# Print full metadata of census
print(repr(metadata.tables['census']))

#Selecting data from a Table: raw SQL
''''
Use the .connect() method of engine to create a connection.
Build a SQL statement to query all the columns from census and store it in stmt. Note that your SQL statement must be a string.
Use the .execute() and .fetchall() methods on connection and store the result in results. Remember that .execute() comes before .fetchall() and that stmt needs to be passed to .execute().
Print results.
'''
from sqlalchemy import create_engine
engine = create_engine('sqlite:///census.sqlite')

# Create a connection on engine
connection = engine.connect()

# Build select statement for census table: stmt
stmt = 'select * from census'

# Execute the statement and fetch the results: results
results = connection.execute(stmt).fetchall()

# Print results
print(results)

#Selecting data from a Table with SQLAlchemy
''''
Import select from the sqlalchemy module.
Reflect the census table. This code is already written for you.
Create a query using the select() function to retrieve all the records in the census table. To do so, pass a list to select() containing a single element: census.
Print stmt to see the actual SQL query being created. This code has been written for you.
Fetch 10 records from the census table and store then in results. To do this:
Use the .execute() method on connection with stmt as the argument to retrieve the ResultProxy.
Use .fetchmany() with the appropriate size argument on connection.execute(stmt) to retrieve the ResultSet.
'''
# Import select
from sqlalchemy import create_engine,select

# Reflect census table via engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Build select statement for census table: stmt
stmt = select([census])

# Print the emitted statement to see the SQL string
print(stmt)

# Execute the statement on connection and fetch 10 records: result
results = connection.execute(stmt).fetchmany(size=10)

# Execute the statement and print the results
print(results)

#Handling a ResultSet
''''
Extract the first row of results and assign it to the variable first_row.
Print the value of the first column in first_row.
Print the value of the 'state' column in first_row.
'''
# Get the first row of the results by using an index: first_row
first_row = results[0]

# Print the first row of the results
print(first_row)

# Print the first column of the first row by accessing it by its index
print(first_row[0])

# Print the 'state' column of the first row by using its name
print(first_row['state'])

#Chapter 2
#Applying Filtering, Ordering and Grouping to Queries

#Connecting to a PostgreSQL database
''''
Import create_engine from sqlalchemy.
Create an engine to the census database by concatenating the following strings:
'postgresql+psycopg2://'
'student:datacamp'
'@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com'
':5432/census'
Use the .table_names() method on engine to print the table names.
'''
# Import create_engine function
from sqlalchemy import create_engine

# Create an engine to the census database
engine = create_engine('postgresql+psycopg2://student:datacamp@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/census')

# Use the .table_names() method on the engine to print the table names
print(engine.table_names())

#Filter data selected from a Table - Simple
''''
Select all records from the census table by passing in census as a list to select().
Append a where clause to stmt to return only the records with a state of 'New York'.
Execute the statement stmt using .execute() on connection and retrieve the results using .fetchall().
Iterate over results and print the age, sex and pop2000 columns from each record. For example, you can print out the age of result with result.age.
'''
# Create a select query: stmt
stmt = select([census])

# Add a where clause to filter the results to only those for New York : stmt_filtered
stmt = stmt.where(census.columns.state == 'New York')

# Execute the query to retrieve all the data returned: results
results = connection.execute(stmt).fetchall()

# Loop over the results and print the age, sex, and pop2000
for result in results:
    print(result.age, result.sex, result.pop2000)

#Filter data selected from a Table - Expressions
''''
Select all records from the census table.
Modify the argument of the where clause to use in_() to return all the records where the value in the census.columns.state column is in the states list.
Loop over the ResultProxy connection.execute(stmt) and print the state and pop2000 columns from each record.
'''
# Define a list of states for which we want results
states = ['New York', 'California', 'Texas']

# Create a query for the census table: stmt
stmt = select([census])

# Append a where clause to match all the states in_ the list states
stmt = stmt.where(census.columns.state.in_(states))

# Loop over the ResultProxy and print the state and its population in 2000
for result in connection.execute(stmt):
    print(result.state, result.pop2000)

#Filter data selected from a Table - Advanced
''''
Import and_ from the sqlalchemy module.
Select all records from the census table.
Append a where clause to filter all the records whose state is 'California', and whose sex is not 'M'.
Execute stmt in the connection and iterate over the ResultProxy to print the age and sex columns from each record.
'''
# Import and_
from sqlalchemy import or_,and_

# Build a query for the census table: stmt
stmt = select([census])

# Append a where clause to select only non-male records from California using and_
stmt = stmt.where(
    # The state of California with a non-male sex
    and_(census.columns.state == 'California',
         census.columns.sex != 'M'
         )
)

# Loop over the ResultProxy printing the age and sex
for result in connection.execute(stmt):
    print(result.age, result.sex)

#Ordering by a single column
''''
Select all records of the state column from the census table. To do this, pass census.columns.state as a list to select().
Append an .order_by() to sort the result output by the state column.
Execute stmt using the .execute() method on connection and retrieve all the results using .fetchall().
Print the first 10 rows of results.
'''
# Build a query to select the state column: stmt
stmt = select([census.columns.state])

# Order stmt by the state column
stmt = stmt.order_by(census.columns.state)

# Execute the query and store the results: results
results = connection.execute(stmt).fetchall()

# Print the first 10 results
print(results[:10])

#Ordering in descending order by a single column
''''
Import desc from the sqlalchemy module.
Select all records of the state column from the census table.
Append an .order_by() to sort the result output by the state column in descending order. Save the result as rev_stmt.
Execute rev_stmt using connection.execute() and fetch all the results with .fetchall(). Save them as rev_results.
Print the first 10 rows of rev_results.
'''
# Import desc
from sqlalchemy import desc

# Build a query to select the state column: stmt
stmt = select([census.columns.state])

# Order stmt by state in descending order: rev_stmt
rev_stmt = stmt.order_by(census.columns.state.desc())

# Execute the query and store the results: rev_results
rev_results = connection.execute(rev_stmt).fetchall()

# Print the first 10 rev_results
print(rev_results[:10])

#Ordering by multiple columns
''''
Select all records of the state and age columns from the census table.
Use .order_by() to sort the output of the state column in ascending order and age in descending order. (NOTE: desc is already imported).
Execute stmt using the .execute() method on connection and retrieve all the results using .fetchall().
Print the first 20 results.
'''
# Build a query to select state and age: stmt
stmt = select([census.columns.state, census.columns.age])

# Append order by to ascend by state and descend by age
stmt = stmt.order_by(census.columns.state, desc(census.columns.age))

# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()

# Print the first 20 results
print(results[:20])

#Counting distinct data
''''
Build a select statement to count the distinct values in the state field of census.
Execute stmt to get the count and store the results as distinct_state_count.
Print the value of distinct_state_count.
'''
# Build a query to count the distinct states values: stmt
stmt = select([func.count(census.columns.state.distinct())])

# Execute the query and store the scalar result: distinct_state_count
distinct_state_count = connection.execute(stmt).scalar()

# Print the distinct_state_count
print(distinct_state_count)

#Count of records by state
''''
Import func from sqlalchemy.
Build a select statement to get the value of the state field and a count of the values in the age field, and store it as stmt.
Use the .group_by() method to group the statement by the state column.
Execute stmt using the connection to get the count and store the results as results.
Print the keys/column names of the results returned using results[0].keys().
'''
# Import func
from sqlalchemy import func

# Build a query to select the state and count of ages by state: stmt
stmt = select([census.columns.state, func.count(census.columns.age)])

# Group stmt by state
stmt = stmt.group_by(census.columns.state)

# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()

# Print results
print(results)

# Print the keys/column names of the results returned
print(results[0].keys())

#Determining the population sum by state
''''
Import func from sqlalchemy.
Build an expression to calculate the sum of the values in the pop2008 field labeled as 'population'.
Build a select statement to get the value of the state field and the sum of the values in pop2008.
Group the statement by state using a .group_by() method.
Execute stmt using the connection to get the count and store the results as results.
Print the keys/column names of the results returned using results[0].keys().
'''
# Import func
from sqlalchemy import func

# Build an expression to calculate the sum of pop2008 labeled as population
pop2008_sum = func.sum(census.columns.pop2008).label('population')

# Build a query to select the state and sum of pop2008: stmt
stmt = select([census.columns.state, pop2008_sum])

# Group stmt by state
stmt = stmt.group_by(census.columns.state)

# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()

# Print results
print(results)

# Print the keys/column names of the results returned
print(results[0].keys())

#ResultsSets and pandas DataFrames
''''
Import pandas as pd.
Create a DataFrame df using pd.DataFrame() on the ResultSet results.
Set the columns of the DataFrame df.columns to be the columns from the first result object results[0].keys().
Print the DataFrame.
'''
# import pandas
import pandas as pd

# Create a DataFrame from the results: df
df = pd.DataFrame(results)

# Set column names
df.columns = results[0].keys()

# Print the DataFrame
print(df)

#From SQLAlchemy results to a plot
''''
Import matplotlib.pyplot as plt.
Create a DataFrame df using pd.DataFrame() on the provided results.
Set the columns of the DataFrame df.columns to be the columns from the first result object results[0].keys().
Print the DataFrame df.
Use the plot.bar() method on df to create a bar plot of the results.
Display the plot with plt.show().
'''
# Import pyplot as plt from matplotlib
import matplotlib.pyplot as plt

# Create a DataFrame from the results: df
df = pd.DataFrame(results)

# Set Column names
df.columns = results[0].keys()

# Print the DataFrame
print(df)

# Plot the DataFrame
df.plot.bar()
plt.show()


#Chapter 3
#Advanced SQLAlchemy Queries
# Import create_engine function
from sqlalchemy import create_engine

# Create an engine to the census database
engine = create_engine('mysql+pymysql://student:datacamp@courses.csrrinzqubik.us-east-1.rds.amazonaws.com:3306/census')

# Print the table names
print(engine.table_names())

#Calculating a difference between two columns
''''
Define a select statement called stmt to return:
i) The state column of the census table (census.columns.state).
ii) The difference in population count between 2008 (census.columns.pop2008) and 2000 (census.columns.pop2000) labeled as 'pop_change'.
Group the statement by census.columns.state.
Order the statement by population change ('pop_change') in descending order. Do so by passing it desc('pop_change').
Use the .limit() method on the previous statement to return only 5 records.
Execute the statement and fetchall() the records.
The print statement has already been written for you. Hit 'Submit Answer' to view the results!
'''
# Build query to return state names by population difference from 2008 to 2000: stmt
stmt = select([census.columns.state, (census.columns.pop2008-census.columns.pop2000).label('pop_change')])

# Append group by for the state: stmt_grouped
stmt_grouped = stmt.group_by(census.columns.state)

# Append order by for pop_change descendingly: stmt_ordered
stmt_ordered = stmt_grouped.order_by(desc('pop_change'))

# Return only 5 results: stmt_top5
stmt_top5 = stmt_ordered.limit(5)

# Use connection to execute stmt_top5 and fetch all results
results = connection.execute(stmt_top5).fetchall()

# Print the state and population change for each record
for result in results:
    print('{}:{}'.format(result.state, result.pop_change))

#Determining the overall percentage of women
''''
Import case, cast, and Float from sqlalchemy.
Build an expression female_pop2000to calculate female population in 2000. To achieve this:
Use case() inside func.sum().
The first argument of case() is a list containing a tuple of
i) A boolean checking that census.columns.sex is equal to 'F'.
ii) The column census.columns.pop2000.
The second argument is the else_ condition, which should be set to 0.
Calculate the total population in 2000 and use cast() to convert it to Float.
Build a query to calculate the percentage of women in 2000. To do this, divide female_pop2000 by total_pop2000 and multiply by 100.
Execute the query and print percent_female.
'''
# import case, cast and Float from sqlalchemy
from sqlalchemy import case, cast, Float

# Build an expression to calculate female population in 2000
female_pop2000 = func.sum(
    case([
        (census.columns.sex == 'F', census.columns.pop2000)
    ], else_=0))

# Cast an expression to calculate total population in 2000 to Float
total_pop2000 = cast(func.sum(census.columns.pop2000), Float)

# Build a query to calculate the percentage of women in 2000: stmt
stmt = select([female_pop2000 / total_pop2000* 100])

# Execute the query and store the scalar result: percent_female
percent_female = connection.execute(stmt).scalar()

# Print the percentage
print(percent_female)

#Automatic joins with an established relationship
''''
Build a statement to join the census and state_fact tables and select the pop2000 column from the first and the abbreviation column from the second.
Execute the statement to get the first result and save it as result.
Hit 'Submit Answer' to loop over the keys of the result object, and print the key and value for each!
'''
# Build a statement to join census and state_fact tables: stmt
stmt = select([census.columns.pop2000, state_fact.columns.abbreviation])

# Execute the statement and get the first result: result
result = connection.execute(stmt).first()

# Loop over the keys in the result object and print the key and value
for key in result.keys():
    print(key, getattr(result, key))

#Joins
''''
Build a statement to select ALL the columns from the census and state_fact tables. To select ALL the columns from two tables employees and sales, for example, you would use stmt = select([employees, sales]).
Append a select_from to stmt to join the census table to the state_fact table by the state column in census and the name column in the state_fact table.
Execute the statement to get the first result and save it as result. This code is already written.
Hit 'Submit Answer' to loop over the keys of the result object, and print the key and value for each!
'''
# Build a statement to select the census and state_fact tables: stmt
stmt = select([census, state_fact])

# Add a select_from clause that wraps a join for the census and state_fact
# tables where the census state column and state_fact name column match
stmt_join = stmt.select_from(
    census.join(state_fact, census.columns.state == state_fact.columns.name))

# Execute the statement and get the first result: result
result = connection.execute(stmt_join).first()

# Loop over the keys in the result object and print the key and value
for key in result.keys():
    print(key, getattr(result, key))

#More practice with joins
''''
Build a statement to select:
The state column from the census table.
The sum of the pop2008 column from the census table.
The census_division_name column from the state_fact table.
Append a .select_from() to stmt in order to join the census and state_fact tables by the state and name columns.
Group the statement by the name column of the state_fact table.
Execute the statement stmt_grouped to get all the records and save it as results.
Hit 'Submit Answer' to loop over the results object and print each record.
'''
# Build a statement to select the state, sum of 2008 population and census
# division name: stmt
stmt = select([
    census.columns.state,
    func.sum(census.columns.pop2008),
    state_fact.columns.census_division_name
])

# Append select_from to join the census and state_fact tables by the census state and state_fact name columns
stmt_joined = stmt.select_from(
    census.join(state_fact, census.columns.state == state_fact.columns.name)
)

# Append a group by for the state_fact name column
stmt_grouped = stmt_joined.group_by(state_fact.columns.name)

# Execute the statement and get the results: results
results = connection.execute(stmt_grouped).fetchall()

# Loop over the results object and print each record.
for record in results:
    print(record)

#Using alias to handle same table joined queries
''''
Save an alias of the employees table as managers. To do so, apply the method .alias() to employees.
Build a query to select the employee's name and their manager's name. The manager's name has already been selected for you. Use label to label the name column of employees as 'employee'.
Append a where clause to stmt to match where the id column of the managers table corresponds to the mgr column of the employees table.
Order the statement by the name column of the managers table.
Execute the statement and store all the results. This code is already written. Hit 'Submit Answer' to print the names of the managers and all their employees.
'''
# Make an alias of the employees table: managers
managers = employees.alias()

# Build a query to select names of managers and their employees: stmt
stmt = select(
    [managers.columns.name.label('manager'),
     employees.columns.name.label('employee')]
)

# Match managers id with employees mgr: stmt_matched
stmt_matched = stmt.where(managers.columns.id == employees.columns.mgr)

# Order the statement by the managers name: stmt_ordered
stmt_ordered = stmt_matched.order_by(managers.columns.name)

# Execute statement: results
results = connection.execute(stmt_ordered).fetchall()

# Print records
for record in results:
    print(record)

#Leveraging functions and group_bys with hierarchical data
''''
Save an alias of the employees table as managers.
Build a query to select the name column of the managers table and the count of the number of their employees. The function func.count() has been imported and will be useful! Use it to count the id column of the employees table.
Using a .where() clause, filter the records where the id column of the managers table and mgr column of the employees table are equal.
Group the query by the name column of the managers table.
Execute the statement and store all the results. Print the names of the managers and their employees. This code has already been written so hit 'Submit Answer' and check out the results!
'''
# Make an alias of the employees table: managers
managers = employees.alias()

# Build a query to select names of managers and counts of their employees: stmt
stmt = select([managers.columns.name, func.count(employees.columns.id)])

# Append a where clause that ensures the manager id and employee mgr are equal: stmt_matched 
stmt_matched = stmt.where(managers.columns.id == employees.columns.mgr)

# Group by Managers Name: stmt_grouped
stmt_grouped = stmt_matched.group_by(managers.columns.name)

# Execute statement: results
results = connection.execute(stmt_grouped).fetchall()

# print manager
for record in results:
    print(record)

#Working on blocks of records
''''
Use a while loop that checks if there are more_results.
Inside the loop, apply the method .fetchmany() to results_proxy to get 50 records at a time and store those records as partial_results.
After fetching the records, if partial_results is an empty list (that is, if it is equal to []), set more_results to False.
Loop over the partial_results and, if row.state is a key in the state_count dictionary, increment state_count[row.state] by 1; otherwise set state_count[row.state] to 1.
After the while loop, close the ResultProxy results_proxy using .close().
Hit 'Submit Answer' to print state_count.
'''
# Start a while loop checking for more results
while more_results:
    # Fetch the first 50 results from the ResultProxy: partial_results
    partial_results = results_proxy.fetchmany(50)

    # if empty list, set more_results to False
    if partial_results == []:
        more_results = False

    # Loop over the fetched records and increment the count for the state
    for row in partial_results:
        if row.state in state_count:
            state_count[row.state] += 1
        else:
            state_count[row.state] = 1

# Close the ResultProxy, and thus the connection
results_proxy.close()

# Print the count by state
print(state_count)

#Creating tables with SQLAlchemy
''''
Import Table, Column, String, Integer, Float, Boolean from sqlalchemy.
Build a new table called data with columns 'name' (String(255)), 'count' (Integer()), 'amount'(Float()), and 'valid' (Boolean()) columns. The second argument of Table() needs to be metadata, which has already been initialized.
Create the table in the database by passing engine to metadata.create_all().
'''
# Import Table, Column, String, Integer, Float, Boolean from sqlalchemy
from sqlalchemy import Table, Column, String, Integer, Float, Boolean

# Define a new table with a name, count, amount, and valid column: data
data = Table('data', metadata,
             Column('name', String(255)),
             Column('count', Integer()),
             Column('amount', Float()),
             Column('valid', Boolean())
)

# Use the metadata to create the table
metadata.create_all(engine)

# Print table details
print(repr(data))

#Constraints and data defaults
''''
Table, Column, String, Integer, Float, Boolean are already imported from sqlalchemy.
Build a new table called data with a unique name (String), count (Integer) defaulted to 1, amount (Float), and valid (Boolean) defaulted to False.
Hit 'Submit Answer' to create the table in the database and to print the table details for data.
'''
# Import Table, Column, String, Integer, Float, Boolean from sqlalchemy
from sqlalchemy import Table, Column, String, Integer, Float, Boolean

# Define a new table with a name, count, amount, and valid column: data
data = Table('data', metadata,
             Column('name', String(255), unique=True),
             Column('count', Integer(), default=1),
             Column('amount', Float()),
             Column('valid', Boolean(), default=False)
)

# Use the metadata to create the table
metadata.create_all(engine)

# Print the table details
print(repr(metadata.tables['data']))

#Inserting a single row
''''
Import insert and select from the sqlalchemy module.
Build an insert statement insert_stmt for the data table to set name to 'Anna', count to 1, amount to 1000.00, and valid to True.
Execute insert_stmt with the connection and store the results.
Print the .rowcount attribute of results to see how many records were inserted.
Build a select statement to query data for the record with the name of 'Anna'.
Hit 'Run Solution' to print the results of executing the select statement.
'''
# Import insert and select from sqlalchemy
from sqlalchemy import insert, select

# Build an insert statement to insert a record into the data table: insert_stmt
insert_stmt = insert(data).values(name='Anna', count=1, amount=1000.00, valid=True)

# Execute the insert statement via the connection: results
results = connection.execute(insert_stmt)

# Print result rowcount
print(results.rowcount)

# Build a select statement to validate the insert: select_stmt
select_stmt = select([data]).where(data.columns.name == 'Anna')

# Print the result of executing the query.
print(connection.execute(select_stmt).first())

#Inserting multiple records at once
''''
Build a list of dictionaries called values_list with two dictionaries. In the first dictionary set name to 'Anna', count to 1, amount to 1000.00, and valid to True. In the second dictionary of the list, set name to 'Taylor', count to 1, amount to 750.00, and valid to False.
Build an insert statement for the data table for a multiple insert, save it as stmt.
Execute stmt with the values_list via connection and store the results. Make sure values_list is the second argument to .execute().
Print the rowcount of the results.
'''
# Build a list of dictionaries: values_list
values_list = [
    {'name': 'Anna', 'count': 1, 'amount': 1000.00, 'valid': True},
    {'name': 'Taylor', 'count': 1, 'amount': 750.00, 'valid': False}
]

# Build an insert statement for the data table: stmt
stmt = insert(data)

# Execute stmt with the values_list: results
results = connection.execute(stmt, values_list)

# Print rowcount
print(results.rowcount)

#Loading a CSV into a table
''''
Use pd.read_csv() to load the "census.csv" file into a DataFrame. Set the header parameter to None since the file doesn't have a header row.
Rename the columns of census_df to "state", "sex", age, "pop2000", and "pop2008" to match the columns of the "census" table in the database.
'''
# import pandas
import pandas as pd

# read census.csv into a DataFrame : census_df
census_df = pd.read_csv("census.csv", header=None)

# rename the columns of the census DataFrame
census_df.columns = ['state', 'sex', 'age', 'pop2000', 'pop2008']

''''
Use the .to_sql() method on census_df to append the data to the "census" table in the database using the connection.
Since "census" already exists in the database, you will need to specify an appropriate value for the if_exists parameter.
'''
# import pandas
import pandas as pd

# read census.csv into a DataFrame : census_df
census_df = pd.read_csv("census.csv", header=None)

# rename the columns of the census DataFrame
census_df.columns = ['state', 'sex', 'age', 'pop2000', 'pop2008']

# append the data from census_df to the "census" table via connection
census_df.to_sql(name="census", con=connection, if_exists="append", index=False)

#Updating individual records
''''
Build a statement to select all columns from the state_fact table where the value in the name column is 'New York'. Call it select_stmt.
Fetch all the results and assign them to results.
Print the results and the fips_state column of the first row of the results.
'''
# Build a select statement: select_stmt
select_stmt = select([state_fact]).where(state_fact.columns.name == 'New York')

# Execute select_stmt and fetch the results
results = connection.execute(select_stmt).fetchall()

# Print the results of executing the select_stmt
print(results)

# Print the FIPS code for the first row of the result
print(results[0]['fips_state'])

''''
Notice that there is only one record in state_fact for the state of New York. It currently has the FIPS code of 0.
Build an update statement to change the fips_state column code to 36, save it as update_stmt.
Use a where clause to filter for states with the name of 'New York' in the state_fact table.
Execute update_stmt via the connection and save the output as update_results.
'''
select_stmt = select([state_fact]).where(state_fact.columns.name == 'New York')
results = connection.execute(select_stmt).fetchall()
print(results)
print(results[0]['fips_state'])

# Build a statement to update the fips_state to 36: update_stmt
update_stmt = update(state_fact).values(fips_state = 36)

# Append a where clause to limit it to records for New York state
update_stmt = update_stmt.where(state_fact.columns.name == 'New York')

# Execute the update statement: update_results
update_results = connection.execute(update_stmt)

''''
Now you will confirm that the record for New York was updated by selecting all the records for New York from state_fact and repeating what you did in Step 1.
Execute select_stmt again, fetch all the results, and assign them to new_results. Print the new_results and the fips_state column of the first row of the new_results.
'''
select_stmt = select([state_fact]).where(state_fact.columns.name == 'New York')
results = connection.execute(select_stmt).fetchall()
print(results)
print(results[0]['fips_state'])

update_stmt = update(state_fact).values(fips_state = 36)
update_stmt = update_stmt.where(state_fact.columns.name == 'New York')
update_results = connection.execute(update_stmt)

# Execute select_stmt again and fetch the new results
new_results = connection.execute(select_stmt).fetchall()

# Print the new_results
print(new_results)

# Print the FIPS code for the first row of the new_results
print(new_results[0]['fips_state'])

#Updating multiple records
''''
Build an update statement to update the notes column in the state_fact table to 'The Wild West'. Save it as stmt.
Use a where clause to filter for records that have 'West' in the census_region_name column of the state_fact table.
Execute stmt_west via the connection and save the output as results.
Hit 'Run Solution' to print rowcount of the results.
'''
# Build a statement to update the notes to 'The Wild West': stmt
stmt = update(state_fact).values(notes='The Wild West')

# Append a where clause to match the West census region records: stmt_west
stmt_west = stmt.where(state_fact.columns.census_region_name == 'West')

# Execute the statement: results
results = connection.execute(stmt_west)

# Print rowcount
print(results.rowcount)

#Correlated updates
''''
Build a statement to select the name column from state_fact. Save the statement as fips_stmt.
Append a where clause to fips_stmt that matches fips_state from the state_fact table with fips_code in the flat_census table.
Build an update statement to set the state_name in flat_census to fips_stmt. Save the statement as update_stmt.
Hit 'Submit Answer' to execute update_stmt, store the results and print the rowcount of results.
'''
# Build a statement to select name from state_fact: fips_stmt
fips_stmt = select([state_fact.columns.name])

# Append a where clause to match the fips_state to flat_census fips_code: fips_stmt
fips_stmt = fips_stmt.where(
    state_fact.columns.fips_state == flat_census.columns.fips_code)

# Build an update statement to set the name to fips_stmt_where: update_stmt
update_stmt = update(flat_census).values(state_name=fips_stmt)

# Execute update_stmt: results
results = connection.execute(update_stmt)

# Print rowcount
print(results.rowcount)

#Deleting all the records from a table
''''
Import delete and select from sqlalchemy.
Build a delete statement to remove all the data from the census table. Save it as delete_stmt.
Execute delete_stmt via the connection and save the results.
Hit 'Submit Answer' to select all remaining rows from the census table and print the result to confirm that the table is now empty!
'''
# Import delete, select
from sqlalchemy import delete, select

# Build a statement to empty the census table: stmt
delete_stmt = delete(census)

# Execute the statement: results
results = connection.execute(delete_stmt)

# Print affected rowcount
print(results.rowcount)

# Build a statement to select all records from the census table : select_stmt
select_stmt = select([census])

# Print the results of executing the statement to verify there are no rows
print(connection.execute(select_stmt).fetchall())

#Deleting specific records
''''
Build a delete statement to remove data from the census table. Save it as delete_stmt.
Append a where clause to delete_stmt that contains an and_ to filter for rows which have 'M' in the sex column AND 36 in the age column.
Execute the delete statement.
Hit 'Submit Answer' to print the rowcount of the results, as well as to_delete, which returns the number of rows that should be deleted. These should match and this is an important sanity check!
'''
# Build a statement to count records using the sex column for Men (M) age 36: count_stmt
count_stmt = select([func.count(census.columns.sex)]).where(
    and_(census.columns.sex == 'M',
         census.columns.age == 36)
)

# Execute the select statement and use the scalar() fetch method to save the record count
to_delete = connection.execute(count_stmt).scalar()

# Build a statement to delete records from the census table: delete_stmt
delete_stmt = delete(census)

# Append a where clause to target Men ('M') age 36: delete_stmt
delete_stmt = delete_stmt.where(
    and_(census.columns.sex == 'M',
         census.columns.age == 36)
)

# Execute the statement: results
results = connection.execute(delete_stmt)

# Print affected rowcount and to_delete record count, make sure they match
print(results.rowcount, to_delete)

#Deleting a table completely
''''
Drop the state_fact table by applying the method .drop() to it and passing it the argument engine (in fact, engine will be the sole argument for every function/method in this exercise!)
Check to see if state_fact exists via print. Use the .exists() method with engine as the argument.
Drop all the tables via the metadata using the .drop_all() method.
Use a print statement to check if the census table exists.
'''
# Drop the state_fact tables
state_fact.drop(engine)

# Check to see if state_fact exists
print(state_fact.exists(engine))

# Drop all tables
metadata.drop_all(engine)

# Check to see if census exists
print(census.exists(engine))

#Chapter 5
#Putting it all together

#Setup the engine and metadata
''''
Import create_engine and MetaData from sqlalchemy.
Create an engine to the chapter 5 database by using 'sqlite:///chapter5.sqlite' as the connection string.
Create a MetaData object as metadata.
'''
# Import create_engine, MetaData
from sqlalchemy import create_engine, MetaData

# Define an engine to connect to chapter5.sqlite: engine
engine = create_engine('sqlite:///chapter5.sqlite')

# Initialize MetaData: metadata
metadata = MetaData()

#Create the table to the database
''''
Import Table, Column, String, and Integer from sqlalchemy.
Define a census table with the following columns:
'state' - String - length of 30
'sex' - String - length of 1
'age' - Integer
'pop2000' - Integer
'pop2008' - Integer
Create the table in the database using the metadata and engine.
'''
# Import Table, Column, String, and Integer
from sqlalchemy import Table, Column, String, Integer

# Build a census table: census
census = Table('census', metadata,
               Column('state', String(30)),
               Column('sex', String(1)),
               Column('age', Integer()),
               Column('pop2000', Integer()),
               Column('pop2008', Integer()))

# Create the table in the database
metadata.create_all(engine)

#Reading the data from the CSV
''''
Create an empty list called values_list.
Iterate over the rows of csv_reader with a for loop, creating a dictionary called data for each row and append it to values_list.
Within the for loop, row will be a list whose entries are 'state' , 'sex', 'age', 'pop2000' and 'pop2008' (in that order).
'''
# Create an empty list: values_list
values_list = []

# Iterate over the rows
for row in csv_reader:
    # Create a dictionary with the values
    data = {'state': row[0], 'sex': row[1], 'age': row[2], 'pop2000': row[3],
            'pop2008': row[4]}
    # Append the dictionary to the values list
    values_list.append(data)

#Load data from a list into the Table
''''
Import insert from sqlalchemy.
Build an insert statement for the census table.
Execute the statement stmt along with values_list. You will need to pass them both as arguments to connection.execute().
Print the rowcount attribute of results.
'''
# Import insert
from sqlalchemy import insert

# Build insert statement: stmt
stmt = insert(census)

# Use values_list to insert data: results
results = connection.execute(stmt, values_list)

# Print rowcount
print(results.rowcount)

#Determine the average age by population
''''
Import select and func from sqlalchemy.
Write a statement to select the average of age (age) weighted by population in 2000 (pop2000) from census.
'''
# Import select and func
from sqlalchemy import select, func

# Select the average of age weighted by pop2000
stmt = select([func.sum(census.columns.pop2000 * census.columns.age) 
  					/ func.sum(census.columns.pop2000)
			  ])

#Modify the select statement to alias the new column with weighted average as 'average_age' using .label().
# Import select and func
from sqlalchemy import select, func

# Relabel the new column as average_age
stmt = select([(func.sum(census.columns.pop2000 * census.columns.age) 
  					/ func.sum(census.columns.pop2000)).label('average_age')
			  ])

''''
Modify the select statement to select the sex column of census in addition to the weighted average, with the sex column coming first.
Group by the sex column of census.
'''
# Import select and func
from sqlalchemy import select, func

# Add the sex column to the select statement
stmt = select([census.columns.sex,
  			   (func.sum(census.columns.pop2000 * census.columns.age) 
  					/ func.sum(census.columns.pop2000)).label('average_age')               
			  ])

# Group by sex
stmt = stmt.group_by(census.columns.sex)

''''
Execute the statement on the connection (which has been created for you) and fetch all the results.
Loop over the results and print the values in the sex and average_age columns for each record in the results.
'''
# Import select and func
from sqlalchemy import select, func

# Select sex and average age weighted by 2000 population
stmt = select([(func.sum(census.columns.pop2000 * census.columns.age) 
  					/ func.sum(census.columns.pop2000)).label('average_age'),
               census.columns.sex
			  ])

# Group by sex
stmt = stmt.group_by(census.columns.sex)

# Execute the query and fetch all the results
results = connection.execute(stmt).fetchall()

# Print the sex and average age column for each result
for result in results:
    print(result.sex, result.average_age)

#Determine the percentage of population by gender and state
''''
Import case, cast and Float from sqlalchemy.
Define a statement to select state and the percentage of women in 2000.
Inside func.sum(), use case() to select women (using the sex column) from pop2000. Remember to specify else_=0 if the sex is not 'F'.
To get the percentage, divide the number of women in the year 2000 by the overall population in 2000. Cast the divisor - census.columns.pop2000 - to Float before multiplying by 100.
Group the query by state.
Execute the query and store it as results.
Print state and percent_female for each record. This has been done for you, so hit 'Submit Answer' to see the result.
'''
# import case, cast and Float from sqlalchemy
from sqlalchemy import case, cast, Float

# Build a query to calculate the percentage of women in 2000: stmt
stmt = select([census.columns.state,
    (func.sum(
        case([
            (census.columns.sex == 'F', census.columns.pop2000)
        ], else_=0)) /
     cast(func.sum(census.columns.pop2000), Float) * 100).label('percent_female')
])

# Group By state
stmt = stmt.group_by(census.columns.state)

# Execute the query and store the results: results
results = connection.execute(stmt).fetchall()

# Print the percentage
for result in results:
    print(result.state, result.percent_female)

#Determine the difference by state from the 2000 and 2008 censuses
''''
Build a statement to:
Select state.
Calculate the difference in population between 2008 (pop2008) and 2000 (pop2000).
Group the query by census.columns.state using the .group_by() method on stmt.
Order by 'pop_change' in descending order using the .order_by() method with the desc() function on 'pop_change'.
Limit the query to the top 10 states using the .limit() method.
Execute the query and store it as results.
Print the state and the population change for each result. This has been done for you, so hit 'Submit Answer' to see the result!
'''
# Build query to return state name and population difference from 2008 to 2000
stmt = select([census.columns.state,
     (census.columns.pop2008-census.columns.pop2000).label('pop_change')
])

# Group by State
stmt = stmt.group_by(census.columns.state)

# Order by Population Change
stmt = stmt.order_by(desc('pop_change'))

# Limit to top 10
stmt = stmt.limit(10)

# Use connection to execute the statement and fetch all results
results = connection.execute(stmt).fetchall()

# Print the state and population change for each record
for result in results:
    print('{}:{}'.format(result.state, result.pop_change))
