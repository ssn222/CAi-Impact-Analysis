import pandas
import datetime
import coachaiAnalysisModule as analysis

'''
Requires 3 files: (Filename - Minimum required columns)
    CoachAi Users.csv - MemberId,Status,Join,SiteId
    Contacts Data.csv - ID,JoinDate, SiteId
    Attendance data.csv - ID,VisitDate(,VisitTime,Entrance) *Sorted by ID, JoinDate
        
'''

# Inputs
filepath = 'D:\\Documents\\CoachAi\\Club Data\\FFAus\\20200102 - FFA Historical analysis\\20190102 - Second analysis\\'
contactsFile = "Contacts data (Cleaned).csv"
attendanceFile = "Attendance data (Cleaned).csv"
coachaiFile = "CoachAi Users.csv"