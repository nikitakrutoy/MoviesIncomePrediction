import pytrends
import pandas as pd
from pytrends.request import TrendReq
import sys
import csv

#with open('Google_Searches_v0.3.csv', newline='') as csvfile:
#    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='"')


# Load the Pandas libraries with alias 'pd'
import pandas as pd
# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
df = pd.read_csv("Google_Searches_v0.5(+8).csv")
#print(df.head())
a = df.transpose()
df = df.set_index('Название в ЕАИС')


df1 = pd.read_csv("Movies_Final_F.csv")
# Preview the first 5 lines of the loaded data
print(df1.head())

with open('Movies_Final_F1.csv', newline='', encoding='utf-8-sig') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for line in csvreader:
            date_list = ['nan', 'nan', 'nan', 'nan', 'nan', 'nan', 'nan', 'nan', 'nan']
            print(date_list)
            mov = str(line[0])
            date = 0
            try:
                date = int(line[41])
            except:
                pass
            print(mov)
            print(date)
            print('Ключи')
            print(df.index)
            try:
                date_list = df.loc[mov].tolist()
            except:
                print("Unexpected error:", sys.exc_info()[0])
            print('----------------------------')
            print(len(date_list))
            print(date_list)
            print(type(date_list))
            print('----------------------------')

            print('</>Ключи')
            with open('dates_newest1.csv', 'a', newline='', encoding='utf-8-sig') as csvfile1:
                spamwriter = csv.writer(csvfile1, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
                #try:
                spamwriter.writerow([mov] + [date_list[(date)]] + [date_list[(date+1)]] + [date_list[(date+2)]] + [date_list[(date+3)]] + [date_list[(date + 4)]] + [date_list[(date + 5)]] + [date_list[(date + 6)]] + [date_list[(date + 7)]]+ [date_list[(date + 8)]])
                print([mov] + [date_list[(date)]] + [date_list[(date+1)]] + [date_list[(date+2)]] + [date_list[(date+3)]] + [date_list[(date + 4)]] + [date_list[(date + 5)]] + [date_list[(date + 6)]] + [date_list[(date + 7)]]+ [date_list[(date + 8)]])
                #except:
                #    print("Unexpected error:", sys.exc_info()[0])


#df1.loc[df['Название в ЕАИС'] == 'release_week_rus', 'H'] = df['release_week_rus']

#new_df = pd.merge(data0, data1, on=['Название в ЕАИС'])
#print(new_df.head())
#new_df.to_csv('new_merged.csv')


