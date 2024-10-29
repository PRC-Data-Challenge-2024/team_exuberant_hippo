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
    climbDifferenceFeet = cruiseAltitudeFeet - departureAirportAltitudeFeet
    if ( abs ( AverageClimbRateFeetPerMinutes) < sys.float_info.epsilon ):
        return 15.0
    else:
        return abs(climbDifferenceFeet) / abs(AverageClimbRateFeetPerMinutes)

def computeDurationOfDescentMinutes(destinationAirportAltitudeFeet , cruiseAltitudeFeet , averageDescentRateFeetPerMinutes):
    descentDifferenceFeet = cruiseAltitudeFeet - destinationAirportAltitudeFeet
    if ( abs( averageDescentRateFeetPerMinutes) < sys.float_info.epsilon):
        return 30.0
    else:
        return abs(descentDifferenceFeet) / abs(averageDescentRateFeetPerMinutes)

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
    print ( end - start)

    print("-"*80)
    start = time.time()
    df['descentDurationMinutes'] = df.apply(lambda row: computeDurationOfDescentMinutes(row['ades_elevation_meters']*Meter2Feet , row['maxAltitudeFeet'], row['avgDescentRateFeetMinutes']), axis=1)
    end = time.time()
    print ( end - start)

    print("-"*80)
    start = time.time()
    df['cuiseDurationMinutes'] = df.apply(lambda row: (row['flight_duration'] - row['descentDurationMinutes'] - row['climbDurationMinutes']), axis=1)
    end = time.time()
    print ( end - start)
 
    print ( list ( df ) )
    for columnName in ['date', 'callsign', 'adep', 'name_adep', 'country_code_adep', 'ades', 'name_ades', 'country_code_ades']:
        df.drop(labels=columnName, axis=1, inplace=True)

    for columnName in ['actual_offblock_time', 'arrival_time', 'aircraft_type', 'wtc', 'airline', 'flight_duration']:
        df.drop(labels=columnName, axis=1 ,inplace=True)

    for columnName in ['taxiout_time', 'flown_distance', 'tow', 'maxAltitudeFeet', 'timeStarttoTopOfDescentMin', 'maxClimbRateFeetMinutes', 'avgClimbRateFeetMinutes', 'maxDescentRateFeetMinutes']:
        df.drop(labels=columnName, axis=1 ,inplace=True)

    for columnName in ['avgDescentRateFeetMinutes', 'avgGroundSpeedKnots', 'maxGroundSpeedKnots', 'aircraft_mtow_lb', 'aircraft_mlaw_lb', 'potential_energy', 'kinetic_energy', 'potential_power', 'kinetic_power', 'physicalClassEngine', 'NumEngines', 'approachSpeedKnots']:
        df.drop(labels=columnName, axis=1,inplace=True)

    for columnName in ['adep_elevation_meters', 'ades_elevation_meters', 'adep_latitude_degrees', 'adep_longitude_degrees', 'ades_latitude_degrees', 'ades_longitude_degrees', 'adep_ades_GC_Nm', 'adep_isa_temperature_degrees', 'ades_isa_temperature_degrees', 'adep_air_density', 'ades_air_density', 'adep_pressure', 'ades_pressure']:
        df.drop(labels=columnName, axis=1,inplace=True)

        
    outputCsvFileName = "extendedChallengeSetDurations.csv"

    directoryPath = os.path.join( os.path.dirname(__file__) , "Results" )
    directory = Path(directoryPath)
    if directory.is_dir():
        print ( "it is a directory - {0}".format(directoryPath))
        filePath = os.path.join(directory, outputCsvFileName)
            
        df.to_csv(filePath , index = False , sep = ";")
