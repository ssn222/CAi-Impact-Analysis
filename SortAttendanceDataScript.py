import coachaiAnalysisModule as analysis


'''
Sorts an attendance file by member ID.  File must have 3 columns: "ID","VisitDate","Site"

sliceStart = datetime substring start index

sliceEnd = datetime substring start index

Date formats:
    2019-12-31 - '%Y-%m-%d'
    20/10/2019 - '%d/%m/%Y'

'''

# Inputs to sort attendance data
filePath = 'D:\\Documents\\CoachAi\\Club Data Analysis\\FFAus\\20191129 - FFA data\\'
attendanceFileName = "Attendance Data.csv"
sliceStart = 0
sliceEnd = 10
dateFormat = '%Y-%m-%d'


analysis.SortAttendanceDataByID(filePath + attendanceFileName, sliceStart, sliceEnd, dateFormat)

