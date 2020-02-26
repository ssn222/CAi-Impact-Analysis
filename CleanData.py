import pandas
import coachaiAnalysisModule as analysis

'''
Toolkit for cleaning data files via python shell.  Load correct file and uncomment commands as needed.

'''

# Data folder path
filepath = "D:\\Documents\\CoachAi\\Club Data\\FFAus\\Analysis 3 (20200128)\\"
file = "Attendance data (20190101 - 20200120).csv"

# Reference for date formats
dateFormat1 = '%Y-%m-%d'
dateFormat2 = '%m/%d/%Y'
dateFormat3 = '%d/%m/%Y'
dateFormat4 = '%d-%m-%y'



'''
# FUNCTION 1: Normalize date formats by converting date strings to datetime format
# Inputs
df = pandas.read_csv(filepath + file)
sliceStart = 0
sliceEnd = 10
dateColumn = 'VisitDate'
df.VisitDate = df.VisitDate.str.slice(sliceStart, sliceEnd)

df = analysis.NormalizeDateFormat(df, dateColumn, dateFormat1)
'''

'''
# FUNCTION 2: Clean Contacts data - sort by ID and remove duplicates
df = pandas.read_csv(filepath + file, dtype={"ID": str})
print("Dataframe length before cleaning: " + str(len(df.index)))
df = analysis.CleanContactsDF(df)
print("Dataframe length after cleaning: " + str(len(df.index)))
'''

'''
# FUNCTION 3: Sort attendance data by ID and VisitDate **Requires VisitDate to be normalized
df = pandas.read_csv(filepath + file, dtype={"ID": str})
df = analysis.SortAttendanceDataByID(df)
'''

'''
# FUNCTION 4: Drop a column from a csv
# Inputs
columnName = "Club"

df = pandas.read_csv(filepath + file)
df = df.drop(columnName, axis=1)
'''

'''
# FUNCTION 5: Rearrange existing columns in a csv
# Inputs
column1 = "ID"
column2 = "Site"
column3 = "JoinDate"
column4 = "CancelDate"

df = pandas.read_csv(filepath + file)
df = df[[column1, column2, column3, column4]]
'''


# Write cleaned data into a new csv file
df.to_csv(filepath + file[0:-4] + " (Cleaned).csv", index=False)
