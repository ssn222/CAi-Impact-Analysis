# CAi-Impact-Analysis

A toolkit for analyzing member engagement, retention, and club profitability using data taken from customers' club management software

Files Required: (Filename - Minimum required columns)
    CoachAi Users.csv - MemberId,Status,Join,SiteId
    Contacts Data.csv - ID,JoinDate, SiteId
    Attendance data.csv - ID,VisitDate(,VisitTime,Entrance) *Sorted by ID, JoinDate
File Formats:

Inverclyde Analysis Steps:
1. Clean and sort contacts data - Convert DOB to age, rename columns
2. Run CleanData.py on Contacts Data, Attendance Data, and CoachAi Users.csv

FFA Analysis Steps (Data from Omer)



