'''
Created on 27 oct. 2024

@author: robert
'''

import sys
import os
sys.path.insert( 0 , os.path.abspath('C:/Users/rober/git/openap/'))
print (sys.path)

import os
from pathlib import Path
import pandas as pd

from openap import prop, FuelFlow, Emission, WRAP

from utils import computeChallengeSubmission, readExtendedAirports
from Aircrafts.FAAaircraftDatabaseFile import FaaAircraftDatabase
from utils import computePotentialEnergy , computeKineticEnergy
from utils import computePotentialPower , computeKineticPower


def computeOpenapProperty( actype , openapProperty):
    if ( str(actype).lower() == 'bcs3' ) or ( str(actype).lower() == 'bcs1' ) :
            actype = 'a310'
    aircraft = prop.aircraft(ac=str(actype).lower(), use_synonym=True)
    return aircraft[openapProperty]


def computeOpenapSubProperty ( actype , mainProperty, subProperty ):
    if ( str(actype).lower() == 'bcs3' ) or ( str(actype).lower() == 'bcs1' ) :
            actype = 'a310'
    aircraft = prop.aircraft(ac=str(actype).lower(), use_synonym=True)
    return aircraft[mainProperty][subProperty]


def createOpenapPropertyCSV(df , openapProperty ):
    print ( df.head() )
    print ( list ( df ))
    
    outputCsvFileName = "extendedOpenap" + "_" + openapProperty + ".csv"
    current_dir = os.getcwd()
        
    directoryPath = os.path.join( os.path.dirname(__file__)  , "Results" )
    directory = Path(directoryPath)
    if directory.is_dir():
        print ( "it is a directory - {0}".format(directoryPath))
        filePath = os.path.join(directory, outputCsvFileName)
            
        df.to_csv(filePath , index = False , sep = ";")

if __name__ == '__main__':
    
    df = computeChallengeSubmission()
    print ( df.shape )
    print ( list ( df ))
    
    for column in ['date', 'callsign', 'adep', 'name_adep', 'country_code_adep', 'ades', 'name_ades', 'country_code_ades', 'actual_offblock_time', 'arrival_time',  'wtc', 'airline', 'flight_duration', 'taxiout_time', 'flown_distance', 'tow']:
        if column in list ( df ):
            df = df.drop(column , axis=1)
        
    print ( list ( df ))
    
    available_acs = prop.available_aircraft(use_synonym=True)

    for actype in available_acs:
        print(actype)
        aircraft = prop.aircraft(ac=actype, use_synonym=True)
        print ( aircraft )
        
    print("---- check aircrafts in openap ----")
    
    unique_aircrafts = df['aircraft_type'].unique()
    for actype in unique_aircrafts:
        if ( str(actype).lower() == 'bcs3' ) or ( str(actype).lower() == 'bcs1' ) :
            actype = 'a310'
        aircraft = prop.aircraft(ac=str(actype).lower(), use_synonym=True)
        print ( "-"*80)
        print ( aircraft )

    print ("-"*80)
        
    for openapProperty in ['mtow','mlw','oew','mfc','vmo','ceiling']:
        print ( openapProperty )
        #df[openapProperty] = df.apply(lambda row: computeOpenapProperty( str( row['aircraft_type'] ).lower() , openapProperty ), axis=1)
        #createOpenapPropertyCSV(df , openapProperty)
        
    for openapProperty in ['height','mach']:
        print ( openapProperty )
        mainProperty = "cruise"
        #df[openapProperty] = df.apply(lambda row: computeOpenapSubProperty( str( row['aircraft_type'] ).lower() , mainProperty , openapProperty ), axis=1)
        #createOpenapPropertyCSV(df , mainProperty + "_" + openapProperty)
        
    for openapProperty in ['fuel_coef']:
        pass
        #df[openapProperty] = df.apply(lambda row: computeOpenapSubProperty( str( row['aircraft_type'] ).lower() , 'fuel', openapProperty ), axis=1)

    for openapProperty in ['max','low','high']:
        mainProperty = "pax"
        print ( openapProperty )
        columnName = mainProperty +"_"+openapProperty
        df[columnName] = df.apply(lambda row: computeOpenapSubProperty( str( row['aircraft_type'] ).lower() , mainProperty, openapProperty ), axis=1)
        createOpenapPropertyCSV(df , mainProperty  + "_" + openapProperty)

    df['pax_high_kg'] =  df.apply ( lambda row :  (row['pax_high'] * 80.0 ) , axis=1)
    createOpenapPropertyCSV(df , "pax_high_kg")
