
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

from Engines.Engines import Engines
import time



if __name__ == '__main__':

    df = computeChallengeSubmission()
    print ( df.shape )
    print ( list ( df ))

    print ( list ( df ))
    columnToKeep = ['aircraft_type']
    for columnName in list(df):
        if columnName in columnToKeep:
            pass
        else:
            df = df.drop(columnName , axis=1)

    print( list ( df))
    
    print ("-"*80)
    available_acs = prop.available_aircraft(use_synonym=True)

    for actype in available_acs:
        print(actype)
        aircraft = prop.aircraft(ac=actype, use_synonym=True)
        print("-"*80)
        print ( aircraft )

    print ("-"*80)

    engines = Engines()
    df_engines = engines.read()
        
    print("---- check aircrafts in openap ----")
    
    unique_aircrafts = df['aircraft_type'].unique()
    for actype in unique_aircrafts:
        if ( str(actype).lower() == 'bcs3' ) or ( str(actype).lower() == 'bcs1' ) :
            actype = 'a310'
        aircraft = prop.aircraft(ac=str(actype).lower(), use_synonym=True)
        if (aircraft):
            pass
        else:
            raise ValueError("aircraft not found - {0}".format( actype))
        #print ( aircraft )
        print ("-"*80)
        print ( aircraft['engine']['default'])

        if (engines.isEngineInEmissionDatabase(aircraft['engine']['default'])):
            pass
            print("{0}  fuel flow - {1}".format(aircraft['engine']['default'] , engines.getFuelFlowAtClimbOutKgPerSeconds(aircraft['engine']['default']))) 
        else:
            raise ValueError("{0} not found".format(aircraft['engine']['default']))

        print("-"*80)
