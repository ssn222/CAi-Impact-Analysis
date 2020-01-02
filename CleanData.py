import pandas
import coachaiAnalysisModule as analysis

'''
Toolkit for cleaning data files via python shell.  Load correct file and uncomment commands as needed.

'''

# Data folder path
filepath = "D:\\Documents\\CoachAi\\Club Data\\FFAus\\20193012 - FFA Historical data\\"
file = "Attendance Data (1.19 - 12.19).csv"

# Reference for date formats
dateFormat1 = '%Y-%m-%d'
dateFormat2 = '%m/%d/%Y'
dateFormat3 = '%d/%m/%Y'
dateFormat4 = '%d-%m-%y'

# Import file to dataframe
df = pandas.read_csv(filepath + file, dtype={"ID": str})

'''
# FUNCTION 1: Normalize date formats by converting date strings to datetime format
# Inputs
sliceStart = 0
sliceEnd = 8
dateColumn = 'VisitDate'
df.VisitDate = df.VisitDate.str.slice(sliceStart, sliceEnd)

df = analysis.NormalizeDateFormat(df, dateColumn, dateFormat4)
'''

'''
# FUNCTION 2: Clean Contacts data - sort by ID and remove duplicates
print("Dataframe length before cleaning: " + str(len(df.index)))
df = analysis.CleanContactsDF(df)
print("Dataframe length after cleaning: " + str(len(df.index)))
'''

'''
#FUNCTION 3: Sort attendance data by ID and VisitDate **Requires VisitDate to be normalized
df = analysis.SortAttendanceDataByID(df)
'''


# Write cleaned data into a new csv file
df.to_csv(filepath + file[0:-4] + " (Cleaned).csv", index=False)
