'''
Created on 26 oct. 2024

@author: robert

create a CSV containing the airports adep , ades and number of runways 
write and create a CSV file

'''

import os
from utils import computeChallengeSubmission
from utils import extendDataSetWithRunwaysdata
from pathlib import Path

if __name__ == '__main__':

    df = computeChallengeSubmission()
    print ( df.shape )
    print ( list ( df ))
    
    df = extendDataSetWithRunwaysdata(df)
    print ( df.shape )
    print ( list ( df ))
    
    ''' keep only flight_id , adep , adep_nb_runways , ades_nb_runways '''
    columnsToDrop = [ 'date', 'callsign',  'name_adep', 'country_code_adep',  'name_ades', 'country_code_ades', 'actual_offblock_time', 'arrival_time', 'aircraft_type', 'wtc', 'airline', 'flight_duration', 'taxiout_time', 'flown_distance', 'tow']
    
    for columnToDrop in columnsToDrop:
        df = df.drop(columnToDrop, axis=1)
        
    print ( df.shape )
    print( list ( df ))
    
    outputCsvFileName = "extendedAirportsRunways.csv"
    current_dir = os.getcwd()
        
    directoryPath = os.path.join( os.path.dirname(__file__) , "Results" )
    directory = Path(directoryPath)
    if directory.is_dir():
        print ( "it is a directory - {0}".format(directoryPath))
        filePath = os.path.join(directory, outputCsvFileName)
        
        df.to_csv(filePath , index = False , sep = ";")

    
    