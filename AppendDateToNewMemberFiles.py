import os
import pandas

'''
Reads date from filenames of new member files and adds date as a column to each file
'''

# Input
directory_in_str = 'D:\\Documents\\CoachAi\\Club Data Analysis\\FFAus\\20191129 - FFA data\\Raw Data\\new-members'

directory = os.fsencode(directory_in_str)

testCsv = 0

# For each csv file in the directory, extract date from filename, append a 'JoinDate' column, fill column
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".csv"):
         df = pandas.read_csv(filename, names=["Site","Phone","ID","Blank","First","Last","Sex","Birthdate"])
         date = filename[-27:-17]
         df['JoinDate'] = pandas.Series(date, index=df.index)
         df.to_csv(path_or_buf=date + '.csv', header=False)
         