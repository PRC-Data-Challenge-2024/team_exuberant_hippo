
''' if both adep country code and ades country codes points to the same region Europe '''
''' then the flight is domestic otherwise it is international '''

import os
from pathlib import Path
import pandas as pd


from utils import computeChallengeSubmission, readExtendedAirports
from Aircrafts.FAAaircraftDatabaseFile import FaaAircraftDatabase
from utils import computePotentialEnergy , computeKineticEnergy
from utils import computePotentialPower , computeKineticPower

from Countries.Countries import Country

if __name__ == '__main__':

    df = computeChallengeSubmission()
    print ( df.shape )
    print ( list ( df ))

    countries = Country()
    ret = countries.read()

    print("-"*80)
    print ("Countries read correctly = {0}".format(ret))

    columnsToKeep = ['flight_id', 'country_code_adep','country_code_ades']
    for columnName in list(df):
        if columnName in columnsToKeep:
            pass
        else:
            df.drop(labels=columnName, axis=1, inplace=True)

    print ( list ( df ))
    region = "Europe"
    df['isDomestic'] = df.apply(lambda row: countries.isDomestic(row['country_code_adep'], row['country_code_ades'] , region ), axis=1)

    print ( list ( df ) )
        
    outputCsvFileName = "extendedAdepAdesIsDomestic.csv"
        
    directoryPath = os.path.join( os.path.dirname(__file__) , "Results" )
    directory = Path(directoryPath)
    if directory.is_dir():
        print ( "it is a directory - {0}".format(directoryPath))
        filePath = os.path.join(directory, outputCsvFileName)
            
        df.to_csv(filePath , index = False , sep = ";")
