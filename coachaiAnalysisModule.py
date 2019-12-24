import pandas
import numpy
import datetime
import csv

def to_datetime(date):
    """
    Converts a numpy datetime64 object to a python datetime object 
    Input:
      date - a np.datetime64 object
    Output:
      DATE - a python datetime object
    """
    timestamp = ((date - numpy.datetime64('1970-01-01T00:00:00'))
                 / numpy.timedelta64(1, 's'))
    return datetime.datetime.utcfromtimestamp(timestamp)

def GetCoachAiStartDate(df, memberId):
    try:
        startDate = df.at[memberId, 'CoachAiJoinDate']
        if isinstance(startDate, numpy.ndarray):
            startDate = to_datetime(startDate[0])
    except:
        startDate = "None"
        
    return startDate

def CountVisitsBetweenDates(df, memberId, startDate, endDate):
    '''
    From dataframe df, counts visits between startDate and endDate for memberId.
    '''
    count = 0
    previousVisit = datetime.datetime(2100, 12, 12)
    
    try:
        visits = df.at[memberId, 'VisitDate']
    except:
        visits = 0
    
    if isinstance(visits, numpy.ndarray):
        for visit in visits:
            visit = to_datetime(visit)
            if visit >= startDate and visit != previousVisit:
                if visit < endDate:
                    count += 1
                    previousVisit = visit
                else:
                    break
    elif isinstance(visits, pandas._libs.tslibs.timestamps.Timestamp):
        if visits >= startDate and visits < endDate:
            count = 1
            
    return count

def GetSubscriptionStartDateById(df, memberId):
    '''
    Returns subscription start date.  If there is none, returns Jan 1, 2100
    '''
    try: 
        startDate = df.at[memberId, 'SubscriptionStartDate']
        if isinstance(startDate, numpy.ndarray):
            startDate = to_datetime(startDate[0])
    except:
        startDate = datetime.datetime(2100, 1, 1)
        
    return startDate

def GetSubscriptionEndDateById(df, memberId):
    '''
    Returns subscription end date.  If there is none, returns Jan 1, 1900
    '''
    try:
        endDate = df.at[memberId, 'SubscriptionEndDate']
        if isinstance(endDate, numpy.ndarray):
            endDate = to_datetime(endDate[len(endDate) - 1])
    except:
        endDate = datetime.datetime(1900, 1, 1)
    return endDate

def GetSiteById(df, memberId):
    try:
        site = df.at[memberId, 'SiteId']
        if isinstance(site, numpy.ndarray):
            site = site[0]
    except:
        site = "None"
    
    return site

def GetJoinDateById(df, memberId):
    '''
        Returns join date from Contacts df
    '''
    try:
        startDate = df.at[memberId, 'JoinDate']
        if isinstance(startDate, numpy.ndarray):
            startDate = to_datetime(startDate[0])
    except:
        startDate = "None"
        
    return startDate

def GetSexById(df, memberId):
    '''
        Returns sex from Contacts df
    '''
    try:
        sex = df.at[memberId, 'Sex']
        if isinstance(sex, numpy.ndarray):
            sex = sex[0]
    except:
        sex = "None"
    
    return sex

def GetAgeById(df, memberId):
    '''
        Returns age from Contacts df
    '''
    try:
        age = df.at[memberId, 'Age']
        if isinstance(age, numpy.ndarray):
            age = age[0]
    except:
        age = "None"
    
    return age

def GetCoachAiUsageStatus(df, memberId):
    '''
        Returns Status from CoachAiUsers df
    '''
    try:
        usageStatus = df.at[memberId, 'Status']
    except:
        usageStatus = "No"
    
    return usageStatus

def NormalizeDateFormat(df, dateColumnName, inputFormat):
    '''
        Changes date format of dataframe column
    '''
    df[dateColumnName] = pandas.to_datetime(df[dateColumnName], format=inputFormat)
    return df

def SortAttendanceDataByID(attendanceFileName, sliceStart, sliceEnd, dateFormat):
    #filePath = "D:\\Documents\\Jupyter Notebooks\\EA Data for analysis\\"
    AttendanceDF = pandas.read_csv(attendanceFileName)

    # Convert dates from string to datetime objects
    AttendanceDF.VisitDate = AttendanceDF.VisitDate.str.slice(sliceStart, sliceEnd)
    AttendanceDF['VisitDate'] = pandas.to_datetime(AttendanceDF['VisitDate'], format=dateFormat)

    # Sort by index
    AttendanceDF.sort_values(["ID", "VisitDate"], inplace=True)

    #Write to csv
    AttendanceDF.to_csv("Attendance data (Sorted by ID).csv", index=False)

def WriteListToCsv(listName, fileName):
    with open(fileName, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)    
        writer.writerows(listName)
        
    csvFile.close()