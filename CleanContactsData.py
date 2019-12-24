import pandas

filepath = "D:\\Documents\\CoachAi\\Club Data Analysis\\FFAus\\20191129 - FFA data\\"
Contacts = pandas.read_csv(filepath + "Contacts.csv")

Contacts.sort_values(['ID', 'JoinDate'], inplace = True)
Contacts.drop_duplicates('ID', inplace = True)
Contacts.dropna(axis=0, how='any', inplace=True)

    
Contacts.to_csv(filepath + "Cleaned Contacts Data1.csv", index = False)