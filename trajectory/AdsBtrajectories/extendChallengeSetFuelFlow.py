
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

def usage():
    # create a fuel flow model for A320
    fuelflow = FuelFlow(ac='A320')

    # estimate fuel flow during cruise
    FuelFlowKgPerSeconds = fuelflow.enroute(mass=60000, tas=230, alt=32000)
    print ("en route fuel flow = {0} kilograms per second".format(FuelFlowKgPerSeconds))
    print('-'*70) 

    # estimate fuel flow at climb, with vertical speed (feet/min)
    FuelFlowKgPerSeconds = fuelflow.enroute(mass=60000, tas=200, alt=20000, vs=1000)
    print ("en route fuel flow = {0} kilograms per second".format(FuelFlowKgPerSeconds))
    print('-'*70) 

    # estimate fuel flow at with a given thrust (e.g., derived from drag model)
    FuelFlowKgPerSeconds = fuelflow.at_thrust(acthr=50000, alt=30000)
    print ("at thrust fuel flow = {0} kilograms per second".format(FuelFlowKgPerSeconds))
    print('-'*70) 

    # estimate fuel flow at takeoff
    FuelFlowKgPerSeconds = fuelflow.takeoff(tas=100, alt=0, throttle=1)
    print ("takeoff fuel flow = {0} kilograms per second".format(FuelFlowKgPerSeconds))
    print('-'*70) 

def cleanAircraftMaxAltitudeFeet(maxAltitudeFeet , ceilingFeet ):
    if math.isnan(maxAltitudeFeet):
        ''' 11000 meters ceiling'''
        return max ( ceilingFeet , 11000.0 * Meter2Feet)
    else:
        return maxAltitudeFeet

def getOpenapAircraftFuelFlow(aircraft_type):
    fuelflow = FuelFlow(ac=str(aircraft_type).lower() )
    return fuelflow

def cleanAvgGroundSpeedKnots(avgGroundSpeedKnots , vmo):
    if math.isnan(avgGroundSpeedKnots):
        return vmo
    else:
        return avgGroundSpeedKnots

def computeTopOfDescentWeightKg(aircraft_type, maxTakeOffWeightKg , avgGroundSpeedKnots, vmo, maxAltitudeFeet, ceilingFeet , flightDurationMinutes):
    print(aircraft_type)
    aircraft = prop.aircraft(ac=aircraft_type, eng=None)
    print ('-'*70)
    print ( aircraft )
    kwargs = {"use_synonym":True}
    fuelflow = FuelFlow(ac=str(aircraft_type).lower() , eng=None )
    avgGroundSpeedKnots = cleanAvgGroundSpeedKnots ( avgGroundSpeedKnots, vmo )
    maxAltitudeFeet = cleanAircraftMaxAltitudeFeet( maxAltitudeFeet , ceilingFeet)
    fuelFlowKgPerSeconds = fuelflow.enroute(mass=maxTakeOffWeightKg, tas=avgGroundSpeedKnots, alt=maxAltitudeFeet)
    fuelLossKg = fuelFlowKgPerSeconds * ( flightDurationMinutes * 60.0)
    if ( maxTakeOffWeightKg > fuelLossKg):
        return maxTakeOffWeightKg - fuelLossKg
    else:
        return fuelLossKg

if __name__ == '__main__':

    df = computeChallengeSubmission()
    print ( df.shape )
    print ( list ( df ))

    df_aircrafts = readExtendedAircrafts()
        
    print('''--- left join challenge and submission -> with aircraft files data --- ''')
    df = df.merge( df_aircrafts, how="left", on="flight_id" )
    print ( df.shape )
    print ( list ( df ))

    ''' add openap data for each aircraft '''
    for openapProperty in ['ceiling', 'cruise_mach']:

        df_openap = readAircraftOpenapData( openapProperty )
    
        print('''--- left join challenge and submission -> with openap data --- ''')
        df = df.merge( df_openap, how="left", on="flight_id" )
        print ( df.shape )
        print ( list ( df ))


    #df_post_cruise_weight_kg = 
    df['topOfDescentWeightKg'] = df.apply(lambda row: computeTopOfDescentWeightKg(row['aircraft_type'], row['mtow'] , row['avgGroundSpeedKnots'], row['vmo'] , row['maxAltitudeFeet'], row['ceiling']*Meter2Feet , row['flight_duration']), axis=1)

    print ( list ( df ) )
    for columnName in list ( df ) :
        if columnName in ['flight_id', 'topOfDescentWeightKg']:
            pass
        else:
            df.drop(labels=columnName, axis=1, inplace=True)
    
    print("-"*80)
    print ( list( df ))
    print("-"*80)
    outputCsvFileName = "extendedChallengeSetFuelFlow.csv"

    directoryPath = os.path.join( os.path.dirname(__file__) , "Results" )
    directory = Path(directoryPath)
    if directory.is_dir():
        print ( "it is a directory - {0}".format(directoryPath))
        filePath = os.path.join(directory, outputCsvFileName)
        print ( filePath )
        df.to_csv(filePath , index = False , sep = ";")