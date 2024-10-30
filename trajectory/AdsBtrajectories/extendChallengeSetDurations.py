from openap import FuelFlow
import pandas as pd
import math
import os
from utils import computeChallengeSubmission, readExtendedAircrafts, readExtendedAirports
from Environment.Constants import Meter2Feet
from pathlib import Path
import sys
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


def computeDurationOfClimbMinutes(departureAirportAltitudeFeet, cruiseAltitudeFeet, AverageClimbRateFeetPerMinutes):
    defaultDurationMinutes = 15.0
    if math.isnan(AverageClimbRateFeetPerMinutes) or math.isnan(cruiseAltitudeFeet):
        return defaultDurationMinutes

    climbDifferenceFeet = cruiseAltitudeFeet - departureAirportAltitudeFeet
    if ( abs ( AverageClimbRateFeetPerMinutes)  < sys.float_info.epsilon ):
        return defaultDurationMinutes
    else:
        durationOfClimbMinutes = abs(climbDifferenceFeet) / abs(AverageClimbRateFeetPerMinutes)
        if  abs ( durationOfClimbMinutes ) < sys.float_info.epsilon:
            return defaultDurationMinutes
        else:
            return max ( abs(durationOfClimbMinutes) , defaultDurationMinutes )

def computeDurationOfDescentMinutes(destinationAirportAltitudeFeet , cruiseAltitudeFeet , averageDescentRateFeetPerMinutes):
    defaultDurationMinutes = 30.0
    if math.isnan(averageDescentRateFeetPerMinutes) or math.isnan(cruiseAltitudeFeet):
        return defaultDurationMinutes

    descentDifferenceFeet = cruiseAltitudeFeet - destinationAirportAltitudeFeet
    if ( abs( averageDescentRateFeetPerMinutes) < sys.float_info.epsilon):
        return defaultDurationMinutes
    else:
        durationOfDescentMinutes = abs(descentDifferenceFeet) / abs(averageDescentRateFeetPerMinutes)
        if ( abs(durationOfDescentMinutes) < sys.float_info.epsilon):
            return defaultDurationMinutes
        else:
            return max ( abs(durationOfDescentMinutes) , defaultDurationMinutes )
    
def computeDurationOfCruiseMinutes( flightDurationMinutes, descentDurationMinutes , climbDurationMinutes):
    cruiseDurationMinutes = flightDurationMinutes
    if (flightDurationMinutes > descentDurationMinutes):
        cruiseDurationMinutes = flightDurationMinutes - descentDurationMinutes
    if (cruiseDurationMinutes > climbDurationMinutes):
        cruiseDurationMinutes = cruiseDurationMinutes - climbDurationMinutes
    return cruiseDurationMinutes

if __name__ == '__main__':

    df = computeChallengeSubmission()
    print ( df.shape )
    print ( list ( df ))

    df_aircrafts = readExtendedAircrafts()
        
    print('''--- left join challenge and submission -> with aircraft files data --- ''')
    df = df.merge( df_aircrafts, how="left", on="flight_id" )
    print ( df.shape )
    print ( list ( df ))

    df_airports = readExtendedAirports()
        
    print ( "--- left join challenge and final submission with runways data ---")
    df = df.merge( df_airports , how="left", on="flight_id"  )
    print ( df.shape )
    print ( list ( df ))

    print("-"*80)
    start = time.time()
    df['climbDurationMinutes'] = df.apply(lambda row: computeDurationOfClimbMinutes(row['adep_elevation_meters']*Meter2Feet , row['maxAltitudeFeet'], row['avgClimbRateFeetMinutes']), axis=1)
    end = time.time()
    print ("time to compute Climb Duration Minutes -> {0} seconds".format(end - start))

    print("-"*80)
    start = time.time()
    df['descentDurationMinutes'] = df.apply(lambda row: computeDurationOfDescentMinutes(row['ades_elevation_meters']*Meter2Feet , row['maxAltitudeFeet'], row['avgDescentRateFeetMinutes']), axis=1)
    end = time.time()
    print ("time to compute Descent Duration Minutes -> {0} seconds".format(end - start))


    print("-"*80)
    start = time.time()
    df['cuiseDurationMinutes'] = df.apply(lambda row: computeDurationOfCruiseMinutes( row['flight_duration'] , row['descentDurationMinutes'], row['climbDurationMinutes']), axis=1)
    end = time.time()
    print ("time to compute Cruise Duration Minutes -> {0} seconds".format(end - start))
 
    print ( list ( df ) )
    for columnName in list ( df ) :
        if columnName in ['flight_id', 'climbDurationMinutes','descentDurationMinutes' , 'cuiseDurationMinutes']:
            pass
        else:
            df.drop(labels=columnName, axis=1, inplace=True)
    
    print("-"*80)
    print ( list( df ))
    print("-"*80)
    outputCsvFileName = "extendedChallengeSetDurations.csv"

    directoryPath = os.path.join( os.path.dirname(__file__) , "Results" )
    directory = Path(directoryPath)
    if directory.is_dir():
        print ( "it is a directory - {0}".format(directoryPath))
        filePath = os.path.join(directory, outputCsvFileName)
        print ( filePath )
        df.to_csv(filePath , index = False , sep = ";")
