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
analysisStartDate = datetime.datetime(2019, 1, 1)
analysisEndDate = datetime.datetime(2019, 8, 30)
dataEndDate = datetime.datetime(2019, 8, 30)
analysisWeeks = 12

# Initialize timer
runStartTime = datetime.datetime.now()

# Import files
CoachAiUsers = pandas.read_csv(filepath + coachaiFile, dtype={"MemberId": str})
Contacts = pandas.read_csv(filepath + contactsFile, dtype={"ID": str})
Attendance = pandas.read_csv(filepath + attendanceFile, dtype={"ID": str})

# Convert date strings to datetime objects in all files
dateFormat1 = '%Y-%m-%d'
dateFormat2 = '%Y%m%d'
Contacts['JoinDate'] = pandas.to_datetime(Contacts['JoinDate'], format=dateFormat1)
CoachAiUsers['Join'] = pandas.to_datetime(CoachAiUsers['Join'], format=dateFormat1)
Attendance['VisitDate'] = pandas.to_datetime(Attendance['VisitDate'], format=dateFormat1)


# Set ID column as index in all files
Contacts.set_index('ID', inplace=True)
CoachAiUsers.set_index('MemberId', inplace=True)
Attendance.set_index('ID', inplace=True)


# Make list of contact's IDs
IdList = []
for contact in Contacts.iterrows():
    IdList.append(contact[0])

# Initialize results dataframe that will be analyzed and printed to csv
resultsDf = pandas.DataFrame(columns = ['ID', 'Site', 'Status', 'JoinDate', 'AvgVisits'])


# For each ID, get their info and calculate their average visit frequency during their first X weeks
for memberId in IdList:
    joinDate = analysis.GetJoinDateById(Contacts, memberId)
    
    if (joinDate >= analysisStartDate) and (joinDate < analysisEndDate) and (joinDate + datetime.timedelta(weeks=analysisWeeks) < dataEndDate):
        usageStatus = analysis.GetCoachAiUsageStatus(CoachAiUsers, memberId)
        site = analysis.GetSiteById(Contacts, memberId)
        periodEndDate = joinDate + datetime.timedelta(weeks=analysisWeeks)
        avgVisits = analysis.CountVisitsBetweenDates(Attendance, memberId, joinDate, joinDate + datetime.timedelta(weeks=analysisWeeks)) / analysisWeeks
        resultsDf = resultsDf.append({'ID': memberId, 'Site': site, 'Status': usageStatus, 'JoinDate': joinDate, 'AvgVisits': avgVisits}, ignore_index=True)

# Write results to csv
resultsDf.to_csv(filepath + datetime.date.today().strftime(dateFormat2) + ' - ' + str(analysisWeeks) + ' Week New Member Analysis.csv', index=False)

# Prepare and display results summary
controlDf = resultsDf.loc[resultsDf['Status'] == 'No']
usersDf = resultsDf.loc[resultsDf['Status'] != 'No']

print("Summary of Results - " + str(analysisWeeks) + " Weeks:")
analysis.PrintResultsSummary(resultsDf, 'Total')
analysis.PrintResultsSummary(controlDf, 'Non-users')
analysis.PrintResultsSummary(usersDf, 'Users')

# End timer
runEndTime = datetime.datetime.now()
elapsedTime = runEndTime - runStartTime
print("Total run time: " + str(elapsedTime))
