
import sys
import os
sys.path.insert( 0 , os.path.abspath('C:/Users/rober/git/openap/'))
print (sys.path)

from openap import FuelFlow, prop
import pandas as pd
import math

from utils import computeChallengeSubmission, readExtendedAircrafts, readExtendedAirports
from utils import readAircraftOpenapData
from Environment.Constants import Meter2Feet
from pathlib import Path

import time
from Engines.Engines import Engines


def computeFuelFlowKilograms(engineFuelFlowKgSeconds, ):
    pass
    return 0.0

def getDefaultEngine( aircraft_type , unique_aircrafts):
    for actype in unique_aircrafts:
        if str( aircraft_type ) .lower() == str(actype).lower():
            if ( str(actype).lower() == 'bcs3' ) or ( str(actype).lower() == 'bcs1' ) :
                actype = 'a310'
            aircraft = prop.aircraft(ac=str(actype).lower(), use_synonym=True)
            if (aircraft):
                pass
            else:
                raise ValueError("aircraft not found - {0}".format( actype))
            #print ( aircraft )
            
            return ( aircraft['engine']['default'])
    return "unknown-engine"


def getNumberOfEngines(aircraft_type , unique_aircrafts):
    for actype in unique_aircrafts:
        if str( aircraft_type ) .lower() == str(actype).lower():
            if ( str(actype).lower() == 'bcs3' ) or ( str(actype).lower() == 'bcs1' ) :
                actype = 'a310'
            aircraft = prop.aircraft(ac=str(actype).lower(), use_synonym=True)
            if (aircraft):
                pass
            else:
                raise ValueError("aircraft not found - {0}".format( actype))
            #print ( aircraft )
            
            return ( int(aircraft['engine']['number']) )
    return 2

def getDefaultEngineFuelFlowKgSeconds( aircraft_type , unique_aircrafts , engines ):
    for actype in unique_aircrafts:
        if str( aircraft_type ) .lower() == str(actype).lower():
            if ( str(actype).lower() == 'bcs3' ) or ( str(actype).lower() == 'bcs1' ) :
                actype = 'a310'
            aircraft = prop.aircraft(ac=str(actype).lower(), use_synonym=True)
            if (aircraft):
                pass
            else:
                raise ValueError("aircraft not found - {0}".format( actype))
            #print ( aircraft )
            
            return  engines.getFuelFlowAtClimbOutKgPerSeconds(aircraft['engine']['default'])
    return 0.0 

if __name__ == '__main__':

    df = computeChallengeSubmission()
    print ( df.shape )
    print ( list ( df ))

    df_aircrafts = readExtendedAircrafts()
        
    print('''--- left join challenge and submission -> with aircraft files data --- ''')
    df = df.merge( df_aircrafts, how="left", on="flight_id" )
    print ( df.shape )
    print ( list ( df ))

    unique_aircrafts = df['aircraft_type'].unique()
    print (unique_aircrafts)

    engines = Engines()
    df_engines = engines.read()

    print ("-"*80)
    print("--- default engine ---")
    df['default_engine'] = df.apply( lambda row: getDefaultEngine( row['aircraft_type'] , unique_aircrafts )   , axis=1 )

    print ("-"*80)
    print("--- number of engines ---")
    df['number_of_engines'] = df.apply( lambda row: getNumberOfEngines( row['aircraft_type'] , unique_aircrafts )   , axis=1 )

    print ("-"*80)
    print("--- default engine fuel flow kg per Seconds ---")
    df['fuel_flow_kg_sec'] = df.apply( lambda row : getDefaultEngineFuelFlowKgSeconds ( row['aircraft_type'] , unique_aircrafts , engines ) , axis=1)

    ColumnsToKeep = ['flight_id','aircraft_type','default_engine','number_of_engines','fuel_flow_kg']
    for columnName in list(df):
        if columnName in ColumnsToKeep:
            pass
        else:
            df.drop(columnName, axis=1 , inplace=True)

    print ( list ( df ) )
        
    outputCsvFileName = "extendedOpenap_Engines.csv"
        
    directoryPath = os.path.join( os.path.dirname(__file__) , "Results" )
    directory = Path(directoryPath)
    if directory.is_dir():
        print ( "it is a directory - {0}".format(directoryPath))
        filePath = os.path.join(directory, outputCsvFileName)
            
        df.to_csv(filePath , index = False , sep = ";")


