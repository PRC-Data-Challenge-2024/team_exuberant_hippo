
import os
from pathlib import Path
import pandas as pd


from datetime import datetime
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer


DateFormatWithSlashes = '%d/%m/%Y'
DateFormatWithDashes = "%Y-%m-%d"

lbToKilograms = 0.45359237

def extendDataSetWithDates(df):
    
    if ( not df is None ) and ( isinstance(df , pd.DataFrame )):
        print ("--------- extend dataset with dates as integers -----")
        
        df['date_year'] = df.apply ( lambda row : extractISOYear( row['date'] ), axis=1)
        df['date_month'] = df.apply ( lambda row : extractMonth( row['date'] ), axis=1)
        df['date_week'] = df.apply ( lambda row : extractISOWeek( row['date'] ), axis=1)
        df['date_week_day'] = df.apply ( lambda row : extractISOWeekDay( row['date'] ), axis=1)
        df['date_quarter'] = df.apply ( lambda row : extractQuarter ( row['date'] ) , axis=1)
        
        ''' drop string date '''
        df = df.drop(columns=['date'])

    return df

def readSubmissionSet(fileName):
    df = None
    print("--- Read submission set CSV file-> {0}".format(fileName))
    
    #fileName = "final_submission_set.csv"

    current_dir = os.getcwd()
    directoryPath = os.path.join( os.path.dirname(__file__) , ".." ,  "AnsPerformanceChallenge" )

    directory = Path(directoryPath)
    if directory.is_dir():
        print ( "it is a directory - {0}".format(directoryPath))
        filePath = os.path.join(directory, fileName)
        print ( filePath )
        
        df = pd.read_csv ( filePath , sep = "," )
    
    return df

def extractISOYear(dateStr):
    ''' 01/01/2024 '''
    if str(dateStr).find("-")>0:
        date = datetime.strptime(dateStr, DateFormatWithDashes )
    else:
        date = datetime.strptime(dateStr, DateFormatWithSlashes)
    iso_year, iso_week, iso_weekday = date.isocalendar()
    return iso_year

def extractISOWeek(dateStr):
    ''' 01/01/2024 '''
    if str(dateStr).find("-")>0:
        date = datetime.strptime(dateStr, DateFormatWithDashes )
    else:
        date = datetime.strptime(dateStr, DateFormatWithSlashes)
 
    iso_year, iso_week, iso_weekday = date.isocalendar()
    return iso_week

def extractISOWeekDay(dateStr):
    if str(dateStr).find("-")>0:
        date = datetime.strptime(dateStr, DateFormatWithDashes )
    else:
        date = datetime.strptime(dateStr, DateFormatWithSlashes )
 
    iso_year, iso_week, iso_weekday = date.isocalendar()
    return iso_weekday

def extractMonth(dateStr):
    if str(dateStr).find("-")>0:
        date = datetime.strptime(dateStr, DateFormatWithDashes )
    else:
        date = datetime.strptime(dateStr, DateFormatWithSlashes )
    return date.month

def extractQuarter(dateStr):
    if str(dateStr).find("-")>0:
        date = datetime.strptime(dateStr, DateFormatWithDashes )
    else:
        date = datetime.strptime(dateStr, DateFormatWithSlashes )
    return pd.Timestamp(date).quarter
