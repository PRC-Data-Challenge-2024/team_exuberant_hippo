import os
from pathlib import Path
import pandas as pd
from calendar import Calendar, monthrange

import pandas as pd

import sys
import os
sys.path.insert( 0 , os.path.abspath('C:/Users/rober/git/openap/'))
print (sys.path)

from openap import FuelFlow, prop, FlightPhase

from utils import readChallengeSet
from utils import readSubmissionSet , computeChallengeSubmission

''' https://ansperformance.eu/study/data-challenge/ '''

from utils import readParquet
from datetime import date

def date_iter( year, month):
    for i in range(1, monthrange(year, month)[1]  + 1):
        yield date(year, month, i)

def computeFlightPhaseDurationSeconds( df_filtered ):

        ts = (df_filtered.timestamp - df_filtered.timestamp.iloc[0]).dt.total_seconds()  # second
        alt = df_filtered.altitude.values  # ft
        spd = df_filtered.groundspeed.values  # kts
        roc = df_filtered.vertical_rate.values  # ft/min

        fp = FlightPhase()
        fp.set_trajectory(ts, alt, spd, roc)

        labels = fp.phaselabel()

        '''
        GND: on-ground  
        CL:  climb
        DE:  descend
        LVL: level flight
        CR:  cruise
        NA:  unlabeled
        ''' 
        phase_duration_in_seconds = {}
        for phase in ['GND','CL','DE','LVL','CR']:
            phase_duration_in_seconds[phase] = len(list(filter(lambda x: x == phase, labels)))
            df_filtered[phase+"_duration_sec"] = phase_duration_in_seconds[phase]

        print(phase_duration_in_seconds)
        print ( "-"*80)

        ''' clean '''
        columnsToKeep = ['flight_id','GND_duration_sec','CL_duration_sec','DE_duration_sec','LVL_duration_sec','CR_duration_sec']
        for columnName in list(df_filtered):
            if columnName in columnsToKeep:
                pass
            else:
                df_filtered.drop(columnName, axis=1, inplace=True)

        print(list(df_filtered))
        print("-"*80)
        return df_filtered

def extendedOneDayParquet(df , df_challengeSubmission):
    
    ''' filter parquet on flight_id in challenge and final submission '''
    df = df[df['flight_id'].isin(df_challengeSubmission['flight_id'])]

    ''' df _filtered is the final dataframe where to merge all results '''
    df_filtered = df.filter( items = ['flight_id'] ).drop_duplicates()
    unique_flight_ids = df_filtered['flight_id'].unique()

    first = True

    for flight_id in unique_flight_ids:

        df_one_flight = df[df['flight_id'] == flight_id]
        df_one_flight = df_one_flight.reset_index()

        df_phase_durations = computeFlightPhaseDurationSeconds ( df_one_flight )
        print ( df_phase_durations.shape )
        df_extended = df_filtered.merge ( df_phase_durations  , how="left" , on="flight_id")
        print( df_extended.shape )

        
    print(list(df_extended))
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

    fileName = 'extendedOpenSkyPhaseDurationsSec.csv'
        
    directoryPath = os.path.join( os.path.dirname(__file__) , "Results" )
    directory = Path(directoryPath)
    print ( directory )

    if directory.is_dir():
            print ( "it is a directory - {0}".format(directoryPath))
            filePath = os.path.join(directory, fileName)
            print (filePath)
            ''' write the parquet file to Results '''
            if testMode == False:
                df_final.to_csv(filePath , index = False , sep = ";")

            else:
                print ("--- test mode = {0}".format(testMode))
                                        
    print("--- its all finished ---")
    print ( df_final.shape )
    print ( list ( df_final ))
    print ( df_final.head(100))

