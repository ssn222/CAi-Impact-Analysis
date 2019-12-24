import pandas
import coachaiAnalysisModule as analysis

'''
Converts a date column from a csv file to a '%Y-%m-%d' format

'''


filepath = "D:\\Documents\\CoachAi\\Club Data Analysis\\FFAus\\20191129 - FFA data\\"
filename = "Attendance data through 28th (Sorted).csv"

dateFormat1 = '%Y-%m-%d'
dateFormat2 = '%m/%d/%Y'
dateFormat3 = '%d/%m/%Y'
dateFormat4 = '%d-%m-%y'

df = pandas.read_csv(filepath + filename)
df = analysis.NormalizeDateFormat(df, 'VisitDate', dateFormat4)

df.to_csv(filename + ' (Date normalized).csv', index=False)