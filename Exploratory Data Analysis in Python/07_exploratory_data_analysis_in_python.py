# Course 7
# Exploratory Data Analysis in Python

# Chapter 1
# Read, clean, and validate

#Exploring the NSFG data

#Calculate the number of rows and columns in the DataFrame nsfg.
nsfg.shape

#Display the names of the columns in nsfg.
nsfg.columns

#Select the column 'birthwgt_oz1' and assign it to a new variable called ounces.
# Select column birthwgt_oz1: ounces
ounces = nsfg['birthwgt_oz1']

#Display the first 5 elements of ounces.
# Print the first 5 elements of ounces
print(ounces.head())

#Clean a variable
''''
In the 'nbrnaliv' column, replace the value 8, in place, with the special value NaN.
Confirm that the value 8 no longer appears in this column by printing the values and their frequencies.
'''
# Replace the value 8 with NaN
nsfg['nbrnaliv'].replace(8, np.nan, inplace=True)

# Print the values and their frequencies
print(nsfg['nbrnaliv'].value_counts())

#Compute a variable
''''
Select 'agecon' and 'agepreg', divide them by 100, and assign them to the local variables agecon and agepreg.
'''
# Select the columns and divide by 100
agecon = nsfg['agecon'] / 100
agepreg = nsfg['agepreg'] / 100

#Compute the difference, which is an estimate of the duration of the pregnancy. Keep in mind that for each pregnancy, agepreg will be larger than agecon.
# Select the columns and divide by 100
agecon = nsfg['agecon'] / 100
agepreg = nsfg['agepreg'] / 100

# Compute the difference
preg_length = agepreg-agecon

#Use .describe() to compute the mean duration and other summary statistics.
# Select the columns and divide by 100
agecon = nsfg['agecon'] / 100
agepreg = nsfg['agepreg'] / 100

# Compute the difference
preg_length = agepreg - agecon

# Compute summary statistics
print(preg_length.describe())

#Make a histogram
#Plot a histogram of agecon with 20 bins.

# Plot the histogram
plt.hist(agecon.dropna(), bins = 20)

# Label the axes
plt.xlabel('Age at conception')
plt.ylabel('Number of pregnancies')

# Show the figure
plt.show()

#Adapt your code to make an unfilled histogram by setting the parameter histtype to be 'step'.
# Plot the histogram
plt.hist(agecon, bins=20, histtype='step')

# Label the axes
plt.xlabel('Age at conception')
plt.ylabel('Number of pregnancies')

# Show the figure
plt.show()

#Compute birth weight
''''
Make a Boolean Series called full_term that is true for babies with 'prglngth' greater than or equal to 37 weeks.
Use full_term and birth_weight to select birth weight in pounds for full-term babies. Store the result in full_term_weight.
Compute the mean weight of full-term babies.
'''
# Create a Boolean Series for full-term babies
full_term = nsfg['prglngth'] >= 37

# Select the weights of full-term babies
full_term_weight = birth_weight[full_term]

# Compute the mean weight of full-term babies
print(full_term_weight.mean())

#Filter
''''
Use the variable 'nbrnaliv' to make a Boolean Series that is True for single births (where 'nbrnaliv' equals 1) and False otherwise.
Use Boolean Series and logical operators to select single, full-term babies and compute their mean birth weight.
For comparison, select multiple, full-term babies and compute their mean birth weight.
'''
# Filter full-term babies
full_term = nsfg['prglngth'] >= 37

# Filter single births
single = nsfg['nbrnaliv'] == 1

# Compute birth weight for single full-term babies
single_full_term_weight = birth_weight[single & full_term]
print('Single full-term mean:', single_full_term_weight.mean())

# Compute birth weight for multiple full-term babies
mult_full_term_weight = birth_weight[~single & full_term]
print('Multiple full-term mean:', mult_full_term_weight.mean())

# Chapter 2
# Distributions

#Make a PMF
#Make a PMF for year with normalize=False and display the result.
# Compute the PMF for year
pmf_year = Pmf(gss['year'], normalize=False)

# Print the result
print(pmf_year)

#Plot a PMF
#Select the 'age' column from the gss DataFrame and store the result in age.

#Make a normalized PMF of age. Store the result in pmf_age.
# Select the age column
age = gss['age']

# Make a PMF of age
pmf_age = Pmf(age)

#Plot pmf_age as a bar chart.
# Select the age column
age = gss['age']

# Make a PMF of age
pmf_age = Pmf(age)

# Plot the PMF
pmf_age.bar()

# Label the axes
plt.xlabel('Age')
plt.ylabel('PMF')
plt.show()

#Make a CDF
#Select the 'age' column. Store the result in age.
# Select the age column
age = gss['age']

# Compute the CDF of age
cdf_age = Cdf(age)

# Calculate the CDF of 30
print(cdf_age(30))

#Compute IQR
#Calculate the 75th percentile of income and store it in percentile_75th.
# Calculate the 75th percentile 
p = 0.75
percentile_75th = cdf_income.inverse(p)
print(percentile_75th)

#Calculate the 25th percentile of income and store it in percentile_25th.
# Calculate the 75th percentile 
percentile_75th = cdf_income.inverse(0.75)

#Calculate the interquartile range of income. Store the result in iqr.
# Calculate the 25th percentile
percentile_25th = cdf_income.inverse(0.25)

# Calculate the 75th percentile 
percentile_75th = cdf_income.inverse(0.75)

# Calculate the 25th percentile
percentile_25th = cdf_income.inverse(0.25)

# Calculate the interquartile range
iqr = percentile_75th - percentile_25th

# Print the interquartile range
print(iqr)

#Plot a CDF
''''
Select 'realinc' from the gss dataset.
Make a Cdf object called cdf_income.
Create a plot of cdf_income using .plot().
'''
# Select realinc
income = gss['realinc']

# Make the CDF
cdf_income = Cdf(income)

# Plot it
cdf_income.plot()

# Label the axes
plt.xlabel('Income (1986 USD)')
plt.ylabel('CDF')
plt.show()

#Extract education levels
# Select educ
educ = gss['educ']

# Bachelor's degree
bach = (educ >= 16)

# Associate degree
assc = (educ >= 14) & (educ < 16)

# High school
high = (educ <= 12)
print(high.mean())

#Plot income CDFs
#Fill in the missing lines of code to plot the CDFs.
income = gss['realinc']

# Plot the CDFs
Cdf(income[high]).plot(label='High school')
Cdf(income[assc]).plot(label='Associate')
Cdf(income[bach]).plot(label='Bachelor')

# Label the axes
plt.xlabel('Income (1986 USD)')
plt.ylabel('CDF')
plt.legend()
plt.show()

#Distribution of income
''''
Extract 'realinc' from gss and compute its logarithm using np.log10().
Compute the mean and standard deviation of the result.
Make a norm object by passing the computed mean and standard deviation to norm().
'''
# Extract realinc and compute its log
income = gss['realinc']
log_income = np.log10(income)

# Compute mean and standard deviation
mean = log_income.mean()
std = log_income.std()
print(mean, std)

# Make a norm object
from scipy.stats import norm
dist = norm(0, 1)

#Comparing CDFs
''''
Evaluate the normal cumulative distribution function using dist.cdf.
Use the Cdf() function to compute the CDF of log_income.
Plot the result.
'''
# Evaluate the model CDF
xs = np.linspace(2, 5.5)
ys = dist.cdf(xs)

# Plot the model CDF
plt.clf()
plt.plot(xs, ys, color='gray')

# Create and plot the Cdf of log_income
Cdf(log_income).plot()
    
# Label the axes
plt.xlabel('log10 of realinc')
plt.ylabel('CDF')
plt.show()

#Comparing PDFs
''''
Evaluate the normal PDF using dist, which is a norm object with the same mean and standard deviation as the data.
Make a KDE plot of the logarithms of the incomes, using log_income, which is a Series object.
'''
# Evaluate the normal PDF
xs = np.linspace(2, 5.5)
ys = dist.pdf(xs)

# Plot the model PDF
plt.clf()
plt.plot(xs, ys, color='gray')

# Plot the data KDE
sns.kdeplot(log_income)

# Label the axes
plt.xlabel('log10 of realinc')
plt.ylabel('PDF')
plt.show()

#Chapter 3
#Relationships

#PMF of age
''''
Extract the variable 'AGE' from the DataFrame brfss and assign it to age.
Get the PMF of age and plot it as a bar chart.
'''
# Extract age
age = brfss['AGE']

# Plot the PMF
pmf_age = Pmf(age)
pmf_age.bar()

# Label the axes
plt.xlabel('Age in years')
plt.ylabel('PMF')
plt.show()

#Scatter plot
#Make a scatter plot of weight and age with format string 'o' and alpha=0.1.
# Select the first 1000 respondents
brfss = brfss[:1000]

# Extract age and weight
age = brfss['AGE']
weight = brfss['WTKG3']

# Make a scatter plot
plt.plot(age, weight, 'o', alpha = 0.1)

plt.xlabel('Age in years')
plt.ylabel('Weight in kg')

plt.show()

#Jittering
# Select the first 1000 respondents
brfss = brfss[:1000]

# Add jittering to age
age = brfss['AGE'] + np.random.normal(0, 2.5, size=len(brfss))
# Extract weight
weight = brfss['WTKG3']

# Make a scatter plot
plt.plot(age, weight, 'o', markersize=5, alpha=0.2)

plt.xlabel('Age in years')
plt.ylabel('Weight in kg')
plt.show()

#Height and weight
''''
Fill in the parameters of .boxplot() to plot the distribution of weight ('WTKG3') in each height ('_HTMG10') group. Specify whis=10, just as was done in the video.
Add a line to plot the y-axis on a logarithmic scale.
'''
# Drop rows with missing data
data = brfss.dropna(subset=['_HTMG10', 'WTKG3'])

# Make a box plot
sns.boxplot(x='_HTMG10', y='WTKG3', data = data, whis = 10)

# Plot the y-axis on a log scale
plt.yscale('log')

# Remove unneeded lines and label axes
sns.despine(left=True, bottom=True)
plt.xlabel('Height in cm')
plt.ylabel('Weight in kg')
plt.show()

#Distribution of income
''''
Extract 'INCOME2' from the brfss DataFrame and assign it to income.
Plot the PMF of income as a bar chart.
'''
# Extract income
income = brfss['INCOME2']

# Plot the PMF
Pmf(income).bar()

# Label the axes
plt.xlabel('Income level')
plt.ylabel('PMF')
plt.show()

#Income and height
''''
Create a violin plot to plot the distribution of height ('HTM4') in each income ('INCOME2') group. Specify inner=None to simplify the plot.
'''
# Drop rows with missing data
data = brfss.dropna(subset=['INCOME2', 'HTM4'])

# Make a violin plot
sns.violinplot(x='INCOME2',y='HTM4',data=data, inner = None)

# Remove unneeded lines and label axes
sns.despine(left=True, bottom=True)
plt.xlabel('Income level')
plt.ylabel('Height in cm')
plt.show()

#Computing correlations
''''
From the brfss DataFrame, select the columns 'AGE', 'INCOME2', and '_VEGESU1'.
Compute the correlation matrix for these variables.
'''
# Select columns
columns = ['AGE', 'INCOME2', '_VEGESU1']
subset = brfss[columns]

# Compute the correlation matrix
print(subset.corr())

#Income and vegetables
''''
Extract the columns 'INCOME2' and '_VEGESU1' from subset into xs and ys respectively.
Compute the simple linear regression of these variables.
'''
from scipy.stats import linregress

# Extract the variables
subset = brfss.dropna(subset=['INCOME2', '_VEGESU1'])
xs = subset['INCOME2']
ys = subset['_VEGESU1']

# Compute the linear regression
res = linregress(xs,ys)
print(res)

#Fit a line
''''
Set fx to the minimum and maximum of xs, stored in a NumPy array.
Set fy to the points on the fitted line that correspond to the fx.
'''
# Plot the scatter plot
plt.clf()
x_jitter = xs + np.random.normal(0, 0.15, len(xs))
plt.plot(x_jitter, ys, 'o', alpha=0.2)

# Plot the line of best fit
fx = np.array([xs.min(),xs.max()])
fy = res.intercept + res.slope * fx
plt.plot(fx, fy, '-', alpha=0.7)

plt.xlabel('Income code')
plt.ylabel('Vegetable servings per day')
plt.ylim([0, 6])
plt.show()

# Chapter 4
# Multivariate Thinking

#Using StatsModels
''''
Compute the regression of '_VEGESU1' as a function of 'INCOME2' using SciPy's linregress().
Compute the regression of '_VEGESU1' as a function of 'INCOME2' using StatsModels' smf.ols().
'''
from scipy.stats import linregress
import statsmodels.formula.api as smf

# Run regression with linregress
subset = brfss.dropna(subset=['INCOME2', '_VEGESU1'])
xs = subset['INCOME2']
ys = subset['_VEGESU1']
res = linregress(xs,ys)
print(res)

# Run regression with StatsModels
results = smf.ols('_VEGESU1 ~ INCOME2', data = brfss).fit()
print(results.params)

#Plot income and education
''''
Group gss by 'educ'. Store the result in grouped.
From grouped, extract 'realinc' and compute the mean.
Plot mean_income_by_educ as a scatter plot. Specify 'o' and alpha=0.5.
'''
# Group by educ
grouped = gss.groupby('educ')

# Compute mean income in each group
mean_income_by_educ = grouped['realinc'].mean()

# Plot mean income as a scatter plot
plt.plot(mean_income_by_educ,'o',alpha=0.5)

# Label the axes
plt.xlabel('Education (years)')
plt.ylabel('Income (1986 $)')
plt.show()

#Non-linear model of education
''''
Add a column named 'educ2' to the gss DataFrame; it should contain the values from 'educ' squared.
Run a regression model that uses 'educ', 'educ2', 'age', and 'age2' to predict 'realinc'.
'''
import statsmodels.formula.api as smf

# Add a new column with educ squared
gss['educ2'] = gss['educ']**2

# Run a regression model with educ, educ2, age, and age2
results = smf.ols('realinc ~ educ + educ2 + age + age2', data=gss).fit()

# Print the estimated parameters
print(results.params)

#Making predictions
# Run a regression model with educ, educ2, age, and age2
results = smf.ols('realinc ~ educ + educ2 + age + age2', data=gss).fit()

# Make the DataFrame
df = pd.DataFrame()
df['educ'] = np.linspace(0, 20)
df['age'] = 30
df['educ2'] = df['educ']**2
df['age2'] = df['age']**2

# Generate and plot the predictions
pred = results.predict(df)
print(pred.head())

#Visualizing predictions
''''
Plot mean_income_by_educ using circles ('o'). Specify an alpha of 0.5.
Plot the prediction results with a line, with df['educ'] on the x-axis and pred on the y-axis.
'''
# Plot mean income in each age group
plt.clf()
grouped = gss.groupby('educ')
mean_income_by_educ = grouped['realinc'].mean()
plt.plot(mean_income_by_educ,'o',alpha=0.5)

# Plot the predictions
pred = results.predict(df)
plt.plot(df['educ'], pred, label='Age 30')

# Label axes
plt.xlabel('Education (years)')
plt.ylabel('Income (1986 $)')
plt.legend()
plt.show()

#Predicting a binary variable
''''
Fill in the parameters of smf.logit() to predict grass using the variables age, age2, educ, and educ2, along with sex as a categorical variable.
'''
# Recode grass
gss['grass'].replace(2, 0, inplace=True)

# Run logistic regression
results = smf.logit('grass ~ age + age2 + educ + educ2 + C(sex)', data=gss).fit()
results.params

''''
Add a column called educ and set it to 12 years; then compute a second column, educ2, which is the square of educ.
'''
# Recode grass
gss['grass'].replace(2, 0, inplace=True)

# Run logistic regression
results = smf.logit('grass ~ age + age2 + educ + educ2 + C(sex)', data=gss).fit()
results.params

# Make a DataFrame with a range of ages
df = pd.DataFrame()
df['age'] = np.linspace(18, 89)
df['age2'] = df['age']**2

# Set the education level to 12
df['educ'] = 12
df['educ2'] = df['educ']**2

#Generate separate predictions for men and women.
# Recode grass
gss['grass'].replace(2, 0, inplace=True)

# Run logistic regression
results = smf.logit('grass ~ age + age2 + educ + educ2 + C(sex)', data=gss).fit()
results.params

# Make a DataFrame with a range of ages
df = pd.DataFrame()
df['age'] = np.linspace(18, 89)
df['age2'] = df['age']**2

# Set the education level to 12
df['educ'] = 12
df['educ2'] = df['educ']**2

# Generate predictions for men and women
df['sex'] = 1
pred1 = results.predict(df)

df['sex'] = 2
pred2 = results.predict(df)

''''
Fill in the missing code to compute the mean of 'grass' for each age group, and then the arguments of plt.plot() to plot pred2 versus df['age'] with the label 'Female'.
'''
# Recode grass
gss['grass'].replace(2, 0, inplace=True)

# Run logistic regression
results = smf.logit('grass ~ age + age2 + educ + educ2 + C(sex)', data=gss).fit()
results.params

# Make a DataFrame with a range of ages
df = pd.DataFrame()
df['age'] = np.linspace(18, 89)
df['age2'] = df['age']**2

# Set the education level to 12
df['educ'] = 12
df['educ2'] = df['educ']**2

# Generate predictions for men and women
df['sex'] = 1
pred1 = results.predict(df)

df['sex'] = 2
pred2 = results.predict(df)

plt.clf()
grouped = gss.groupby('age')
favor_by_age = grouped['grass'].mean()
plt.plot(favor_by_age, 'o', alpha=0.5)

plt.plot(df['age'], pred1, label='Male')
plt.plot(df['age'], pred2, label='Female')

plt.xlabel('Age')
plt.ylabel('Probability of favoring legalization')
plt.legend()
plt.show()
