import pandas
import numpy
import datetime
import csv
import math
import coachaiAnalysisModule as analysis


# Import files - ATTENDANCE MUST BE SORTED BY MEMBERID
filepath = "D:\\Documents\\Jupyter Notebooks\\EA Data for analysis\\"
CoachAiUsers = pandas.read_csv(filepath + "CoachAiUsers.csv")
EASubscriptions = pandas.read_csv(filepath + "HistoricalSubscriptionsData.csv")
EAContacts = pandas.read_csv(filepath + "HistoricalContactsData.csv")
EAAttendance = pandas.read_csv(filepath + "AttendanceData (20190818).csv")

# Convert date strings to datetime objects in all files
EASubscriptions.SubscriptionStartDate = EASubscriptions.SubscriptionStartDate.str.slice(0, 10)
EASubscriptions.SubscriptionEndDate = EASubscriptions.SubscriptionEndDate.str.slice(0, 10)
EASubscriptions['SubscriptionStartDate'] = pandas.to_datetime(EASubscriptions['SubscriptionStartDate'], format='%Y-%m-%d')
EASubscriptions['SubscriptionEndDate'] = pandas.to_datetime(EASubscriptions['SubscriptionEndDate'], format='%Y-%m-%d')

EAContacts.ContactCreationDate = EAContacts.ContactCreationDate.str.slice(0, 10)
EAContacts['ContactCreationDate'] = pandas.to_datetime(EAContacts['ContactCreationDate'], format='%Y-%m-%d')

CoachAiUsers.CoachAiJoinDate = CoachAiUsers.CoachAiJoinDate.str.slice(0, 10)
CoachAiUsers['CoachAiJoinDate'] = pandas.to_datetime(CoachAiUsers['CoachAiJoinDate'], format='%Y-%m-%d')

EAAttendance.VisitDate = EAAttendance.VisitDate.str.slice(0, 10)
EAAttendance['VisitDate'] = pandas.to_datetime(EAAttendance['VisitDate'], format='%Y-%m-%d')


# Set ID column as index in all files
EASubscriptions.set_index('ID', inplace=True)
EAContacts.set_index('ID', inplace=True)
CoachAiUsers.set_index('ID', inplace=True)
EAAttendance.set_index('ID', inplace=True)


# Start code
dataStartDate = datetime.datetime(2018, 2, 8)
dataEndDate = datetime.datetime(2019, 8, 8)
IdList = []

for user in CoachAiUsers.iterrows():
    IdList.append(user[0])

csvList = []

for memberId in IdList:
    if analysis.GetCoachAiUsageStatus(CoachAiUsers, memberId) == "Active":
        site = analysis.GetSiteById(EASubscriptions, memberId)
        sex = analysis.GetSexById(EAContacts, memberId)
        age = analysis.GetAgeById(EAContacts, memberId)
        joinDate = analysis.GetJoinDateById(EAContacts, memberId)
        subStartDate = analysis.GetSubscriptionStartDateById(EASubscriptions, memberId)
        CoachAiStartDate = analysis.GetCoachAiStartDate(CoachAiUsers, memberId)
        days = (dataEndDate - CoachAiStartDate).days
        visits = analysis.CountVisitsBetweenDates(EAAttendance, memberId, CoachAiStartDate, dataEndDate)
        visitFrequency = visits / (days / 7)
        row = [memberId, site, sex, age, joinDate, subStartDate, CoachAiStartDate, visitFrequency]
        csvList.append(row)

analysis.WriteListToCsv(csvList, 'All users analysis.csv')