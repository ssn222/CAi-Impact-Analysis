import pandas
import datetime
import coachaiAnalysisModule as analysis

'''
Requires 3 files:
    CoachAi Users.csv - MemberId,Status,Join,SiteId
    Contacts Data.csv - ID,Age,Sex,JoinDate,MembershipType
    Attendance data (Sorted by ID).csv - ID,VisitDate(,VisitTime,Entrance) *Sorted by ID, JoinDate
    
Inputs:
    dateFormat = Format of date strings in club files
        2019-12-31 - '%Y-%m-%d'
        20/10/2019 - '%d/%m/%Y'
        
    analysisWeeks = Analysis period (i.e.: visit frequency over the first X weeks of membership)
        
'''

# Inputs
filePath = 'D:\\Documents\\CoachAi\\Club Data Analysis\\FFAus\\20191129 - FFA data\\'
dateFormat1 = '%Y-%m-%d'
dateFormat2 = '%m/%d/%Y'
dateFormat3 = '%d/%m/%Y'
dateFormat4 = '%d-%m-%y'
analysisStartDate = datetime.datetime(2019, 9, 2)
analysisWeeks = 10


# Import files
CoachAiUsers = pandas.read_csv(filePath + "CoachAi Users.csv", dtype={"MemberId": str})
Contacts = pandas.read_csv(filePath + "Cleaned Contacts Data.csv", dtype={"ID": str})
Attendance = pandas.read_csv(filePath + "Attendance data (Sorted by ID).csv", dtype={"ID": str})

# Convert date strings to datetime objects in all files
Contacts.JoinDate = Contacts.JoinDate.str.slice(0, 10)
Contacts['JoinDate'] = pandas.to_datetime(Contacts['JoinDate'], format=dateFormat1)

#CoachAiUsers.Join = CoachAiUsers.Join.str.slice(0, 10)
#CoachAiUsers['Join'] = pandas.to_datetime(CoachAiUsers['Join'], format=dateFormat1)

Attendance.VisitDate = Attendance.VisitDate.str.slice(0, 10)
Attendance['VisitDate'] = pandas.to_datetime(Attendance['VisitDate'], format=dateFormat1)


# Set ID column as index in all files
Contacts.set_index('ID', inplace=True)
CoachAiUsers.set_index('MemberId', inplace=True)
Attendance.set_index('ID', inplace=True)


# Make list of contact's IDs
IdList = []
for contact in Contacts.iterrows():
    IdList.append(contact[0])

# Initialize list that will be printed to csv
csvList = []
csvList.append(['ID', 'Site', 'Status', 'JoinDate', 'AnalysisEnd', 'AvgVisits'])


# For each ID, get their info and calculate their average visit frequency during their first X weeks
for memberId in IdList:
    joinDate = analysis.GetJoinDateById(Contacts, memberId)
    
    if joinDate >= analysisStartDate:
        usageStatus = analysis.GetCoachAiUsageStatus(CoachAiUsers, memberId)
        site = analysis.GetSiteById(Contacts, memberId)
        periodEndDate = joinDate + datetime.timedelta(weeks=analysisWeeks)
        avgVisits = analysis.CountVisitsBetweenDates(Attendance, memberId, joinDate, joinDate + datetime.timedelta(weeks=analysisWeeks)) / analysisWeeks
        row = [memberId, site, usageStatus, joinDate, periodEndDate, avgVisits]
        csvList.append(row)

analysis.WriteListToCsv(csvList, 'New Member Analysis (By Join Date).csv')

