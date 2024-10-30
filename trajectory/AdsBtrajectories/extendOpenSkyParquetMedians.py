
import os
from pathlib import Path
import pandas as pd
from calendar import Calendar, monthrange

from utils import readChallengeSet
from utils import readSubmissionSet , computeChallengeSubmission

''' https://ansperformance.eu/study/data-challenge/ '''

from utils import readParquet
from datetime import date

def date_iter( year, month):
    for i in range(1, monthrange(year, month)[1]  + 1):
        yield date(year, month, i)

def computeMedianClimbRate(df):
    df_climb = df [ ( df['vertical_rate'] >= 0.0 ) ].copy()
    df_climb['medianClimbRateFeetMinutes'] = df_climb.groupby ( ['flight_id'] , as_index=False ) ['vertical_rate'].transform('median')
    df_climb = df_climb.filter( items = ['flight_id','medianClimbRateFeetMinutes'] ).drop_duplicates()
    return df_climb

def computeMedianDescentRate(df):
    df_descent = df [ ( df['vertical_rate'] <= 0.0 ) ].copy()
    df_descent['medianDescentRateFeetMinutes'] = df_descent.groupby ( ['flight_id'] , as_index=False ) ['vertical_rate'].transform('median')
    df_descent = df_descent.filter( items = ['flight_id','medianDescentRateFeetMinutes'] ).drop_duplicates()
    return df_descent

def extendedOneDayParquet(df , df_challengeSubmission):
    
    ''' filter parquet on flight_id in challenge and final sumission '''
    df = df[df['flight_id'].isin(df_challengeSubmission['flight_id'])]

    
    ''' df _filtered is the final dataframe where to merge all results '''
    df_filtered = df.filter( items = ['flight_id'] ).drop_duplicates()

    df_climb_median = computeMedianClimbRate (df)
    df_extended = df_filtered.merge ( df_climb_median  , how="left" , on="flight_id")

    df_descent_median = computeMedianDescentRate(df)
    df_extended = df_extended.merge ( df_descent_median  , how="left" , on="flight_id")

    print ( list ( df_extended ) )
    return df_extended


def extendUsingParquets(testMode=False):
    
    df_challengeSubmission = computeChallengeSubmission()
    
    first = True
    df_final = None
    yearInt = 2022
    
    if ( testMode == True ):
        theDate = date(yearInt, 1, 1)
        fileName = str(theDate) + "." + "parquet"
        df_final = extendedOneDayParquet(readParquet(fileName) , df_challengeSubmission)
    
    else:
        for iMonth in range(1,13):
            for d in date_iter( yearInt, iMonth):
                print(str( d ))
                fileName = str(d) + "." + "parquet"
            
                df = readParquet(fileName)
                if not df is None:
                    if first == True:
                        df_final = extendedOneDayParquet(df , df_challengeSubmission)
                        first = False
                    else:
                        df_extended = extendedOneDayParquet(df , df_challengeSubmission)
                        ''' ignore_index = True auto generate a new index '''
                        df_final = pd.concat ( [df_final , df_extended] , ignore_index=True)           
    
    return df_final



if __name__ == '__main__':
    
    testMode = False
    #testMode = True
    df_final = extendUsingParquets(testMode)

    for columnName in list(df_final):
        if ( columnName in ['flight_id','medianClimbRateFeetMinutes','medianDescentRateFeetMinutes']):
            pass
        else:
            df_final.drop(labels=columnName, axis=1,inplace=True)
    
    fileName = 'extendedOpenSkyMedians.parquet'
        
    directoryPath = os.path.join( os.path.dirname(__file__) , "Results" )
    directory = Path(directoryPath)
    print ( directory )

    if directory.is_dir():
            print ( "it is a directory - {0}".format(directoryPath))
            filePath = os.path.join(directory, fileName)
            ''' write the parquet file to Results '''
            if testMode == False:
                df_final.to_parquet(filePath)
            else:
                print ("--- test mode = {0}".format(testMode))
                                        
    print("--- its all finished ---")
    print ( df_final.shape )
    print ( list ( df_final ))
    print ( df_final.head(100))