'''
Created on 26 oct. 2024

@author: rober
'''

import os
from pathlib import Path
import pandas as pd

from trajectory.AdsBtrajectories.utils import computeChallengeSubmission, readExtendedAirports
from trajectory.AdsBtrajectories.Aircrafts.FAAaircraftDatabaseFile import FaaAircraftDatabase
from trajectory.AdsBtrajectories.utils import computePotentialEnergy , computeKineticEnergy
from trajectory.AdsBtrajectories.utils import computePotentialPower , computeKineticPower

if __name__ == '__main__':
    
    df = computeChallengeSubmission()
    print ( df.shape )
    print ( list ( df ))
    
    df_airports = readExtendedAirports()
    print ( list ( df_airports))
        
    print ( "--- left join challenge and final submission with runways data ---")
    df = df.merge( df_airports , how="left", on="flight_id"  )
    print ( list ( df ))

    print("--- read extended OpenSky parquet ---")
    
    fileName = 'extendedOpenSky.parquet'
    testMode = False
    extendedParquetIsExisting = True
    if ( extendedParquetIsExisting == True ):
        current_dir = os.getcwd()
        directoryPath = os.path.join( os.path.dirname(__file__) , "Results" )

        directory = Path(directoryPath)
        if directory.is_dir():
            print ( "it is a directory - {0}".format(directoryPath))
            filePath = os.path.join(directory, fileName)
            print (filePath)
            
            df_parquets = pd.read_parquet ( filePath )
            print ( df_parquets.shape )
            print ( list ( df_parquets))

    
    print('''--- left join challenge and submission -> with parquet files data --- ''')
    df = df.merge( df_parquets, how="left", on="flight_id" )

    print ("--- Read aircrafts database ")
            
    faaAircraftDatabase = FaaAircraftDatabase()
    if ( faaAircraftDatabase.read()):
                
        print ("--- aircraft database read correctly")
        print ("--- start adding aircraft informations ----")
                
        df['aircraft_mtow_lb'] = df.apply(lambda row: faaAircraftDatabase.getMTOW_lb(row['aircraft_type']), axis=1)
        df['aircraft_mlaw_lb'] = df.apply(lambda row: faaAircraftDatabase.getMALW_lb(row['aircraft_type']), axis=1)
            
        df['potential_energy'] = df.apply( lambda row: computePotentialEnergy( faaAircraftDatabase.getMTOW_lb(row['aircraft_type']) , row['maxAltitudeFeet'] , row['adep_elevation_meters'] ) , axis=1)
        df['kinetic_energy'] = df.apply ( lambda row : computeKineticEnergy ( faaAircraftDatabase.getMTOW_lb(row['aircraft_type']) , row['avgGroundSpeedKnots'] ) , axis=1)
            
        df['potential_power'] = df.apply ( lambda row : computePotentialPower( faaAircraftDatabase.getMTOW_lb(row['aircraft_type']) , row['maxAltitudeFeet'] , row['adep_elevation_meters'] , row['flight_duration']) , axis=1 )
        df['kinetic_power'] = df.apply ( lambda row : computeKineticPower( faaAircraftDatabase.getMTOW_lb(row['aircraft_type']) , row['avgGroundSpeedKnots'] , row['flight_duration']) , axis=1 )
        
        ''' this is a categorical feature '''
        df['physicalClassEngine'] = df.apply( lambda row : faaAircraftDatabase.getPhysicalClassEngine(row['aircraft_type']) , axis=1)
            
        df['NumEngines'] = df.apply( lambda row : faaAircraftDatabase.getNumberOfEngines(row['aircraft_type']) , axis=1)
        df['approachSpeedKnots'] = df.apply( lambda row : faaAircraftDatabase.getApproachSpeedKnots(row['aircraft_type']) , axis=1)

        print ( list ( df ) )
        
        outputCsvFileName = "extendedAircrafts.csv"
        current_dir = os.getcwd()
        
        directoryPath = os.path.join( os.path.dirname(__file__) , "Results" )
        directory = Path(directoryPath)
        if directory.is_dir():
            print ( "it is a directory - {0}".format(directoryPath))
            filePath = os.path.join(directory, outputCsvFileName)
            
            df.to_csv(filePath , index = False , sep = ";")

 