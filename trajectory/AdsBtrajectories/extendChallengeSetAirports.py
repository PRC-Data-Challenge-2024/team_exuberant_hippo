'''
Created on 15 oct. 2024

@author: robert

'''

import os 
from pathlib import Path

from trajectory.AdsBtrajectories.Airports.AirportDatabaseFile import AirportsDatabase
from trajectory.AdsBtrajectories.utils import computeChallengeSubmission
from trajectory.AdsBtrajectories.Atmosphere.Atmosphere import Atmosphere

if __name__ == '__main__':
    
    df = computeChallengeSubmission()
    print ( df.shape )
    print ( list ( df ))
    
    print("--- read Atmosphere ---")
    atmosphere = Atmosphere()
    atmosphereOk = atmosphere.read()
    print ("--- atmosphere read correctly = {0}".format(atmosphereOk))
    
    print ( "Read airports database ")
    
    airportsDatabase = AirportsDatabase()
    airportsDBOk = airportsDatabase.read()
    print ( "--- airports database read correctly = {0}".format( airportsDBOk ) )
    
    print("Read challenge set file")
    
    if ( not df is None ) and ( airportsDBOk == True) and ( atmosphereOk ):

        print ( list ( df ) )
        print ( "number of rows = {0}".format ( len(df.index) ) )
        
        print ( "--- start adding adep ades informations ----")
        
        ''' create a new column '''
        df["adep_elevation_meters"] = df.apply(lambda row: airportsDatabase.getAirportElevationMeters(row['adep']), axis=1)
        df["ades_elevation_meters"] = df.apply(lambda row: airportsDatabase.getAirportElevationMeters(row['ades']), axis=1)
        
        df['adep_latitude_degrees'] = df.apply(lambda row: airportsDatabase.getAirportLatitudeDegrees(row['adep']), axis=1)
        df['adep_longitude_degrees'] = df.apply(lambda row: airportsDatabase.getAirportLongitudeDegrees(row['adep']), axis=1)

        df['ades_latitude_degrees'] = df.apply(lambda row: airportsDatabase.getAirportLatitudeDegrees(row['ades']), axis=1)
        df['ades_longitude_degrees'] = df.apply(lambda row: airportsDatabase.getAirportLongitudeDegrees(row['ades']), axis=1)
        
        df['adep_ades_GC_Nm'] = df.apply(lambda row: airportsDatabase.computeDistanceNm( row['adep'] , row['ades']), axis=1)

        df['adep_isa_temperature_degrees'] = df.apply( lambda row: atmosphere.getTemperatureDegrees( airportsDatabase.getAirportElevationMeters(row['adep']) )  , axis=1)
        df['ades_isa_temperature_degrees'] = df.apply( lambda row: atmosphere.getTemperatureDegrees( airportsDatabase.getAirportElevationMeters(row['ades']) )  , axis=1)

        df['adep_air_density'] = df.apply ( lambda row : atmosphere.getAirDensityKilogramsPerCubicMeters ( airportsDatabase.getAirportElevationMeters(row['adep']) ),axis=1)
        df['ades_air_density'] = df.apply ( lambda row : atmosphere.getAirDensityKilogramsPerCubicMeters ( airportsDatabase.getAirportElevationMeters(row['ades']) ),axis=1)

        df['adep_pressure'] = df.apply ( lambda row : atmosphere.getPressurePascals ( airportsDatabase.getAirportElevationMeters(row['adep']) ),axis=1)
        df['ades_pressure'] = df.apply ( lambda row : atmosphere.getPressurePascals ( airportsDatabase.getAirportElevationMeters(row['ades']) ),axis=1)
 
        print ("------- end adding adep ades informations ----------")
        
        for index, row in df.iterrows():
            if ( index < 10 ):
                print("-----------")
                print(index, row['flight_id'] , row['adep'] , row["adep_elevation_meters"])
                print(index, row['flight_id'] , row['ades'] , row["ades_elevation_meters"])
                print(index ,row['flight_id'] , row['adep'] , row['adep_latitude_degrees'], row['adep_longitude_degrees'])
                print(index ,row['flight_id'] , row['ades'] , row['ades_latitude_degrees'], row['ades_longitude_degrees'])
                
                print(index ,row['flight_id'] , row['adep'] , row['adep_isa_temperature_degrees'])
                print(index ,row['flight_id'] , row['ades'] , row['ades_isa_temperature_degrees'])
            else:
                break
        
        columnsToDrop = [ 'date', 'callsign',  'name_adep', 'country_code_adep',  'name_ades', 'country_code_ades', 'actual_offblock_time', 'arrival_time', 'aircraft_type', 'wtc', 'airline', 'flight_duration', 'taxiout_time', 'flown_distance', 'tow']
    
        for columnToDrop in columnsToDrop:
            df = df.drop(columnToDrop, axis=1)
            
        print ( list ( df ))

        outputCsvFileName = "extendedAirports.csv"
        current_dir = os.getcwd()
        
        directoryPath = os.path.join( os.path.dirname(__file__) , "Results" )
        directory = Path(directoryPath)
        if directory.is_dir():
            print ( "it is a directory - {0}".format(directoryPath))
            filePath = os.path.join(directory, outputCsvFileName)
            
            df.to_csv(filePath , index = False , sep = ";")
