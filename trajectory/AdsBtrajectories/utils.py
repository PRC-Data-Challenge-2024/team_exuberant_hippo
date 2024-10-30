'''
Created on 15 oct. 2024

@author: robert
'''

import os
from pathlib import Path
import pandas as pd
from Airports.AirportDatabaseFile import AirportsDatabase
from datetime import datetime
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer

from Aircrafts.FAAaircraftDatabaseFile import FaaAircraftDatabase
from Guidance.ConstraintsFile import feet2Meters 
from Environment.Constants import  gravity_meter_square_seconds , Knots2MetersSeconds

from Runways.RunWaysDatabaseFile import RunWayDataBase
from Atmosphere.Atmosphere import Atmosphere

DateFormatWithSlashes = '%d/%m/%Y'
DateFormatWithDashes = "%Y-%m-%d"

lbToKilograms = 0.45359237

def readParquet(fileName):
    df = None
    print("--- Read parquet file ---")
    
    current_dir = os.getcwd()
    directoryPath = os.path.join( os.path.dirname(__file__) ,  "AnsPerformanceChallenge" ,'competition-data')
    print ( directoryPath )
    #fileName = "2022-01-01.parquet"
    directory = Path(directoryPath)
    if directory.is_dir():
        print ( "it is a directory - {0}".format(directoryPath))
        filePath = os.path.join(directory, fileName)
        print ( filePath )
        df = pd.read_parquet ( filePath )
        print ( list ( df ))
    return df

def readAircraftOpenapData( openapProperty ):
    df = None
    print("--- Read openap file for property = {0}".format( openapProperty ))
    
    fileName = "extendedOpenap" + "_" + openapProperty + ".csv"
        
    directoryPath = os.path.join( os.path.dirname(__file__) , "Results" )
    directory = Path(directoryPath)
    if directory.is_dir():
        print ( "it is a directory - {0}".format(directoryPath))
        filePath = os.path.join(directory, fileName)
        print ( filePath )
        
        df = pd.read_csv( filePath , sep = ";")
        df = df.drop('aircraft_type', axis=1)
        print ( list ( df ) )
    
    return df 

def readOpenSkyMediansClimbDescentRates( ):

    df = None
    print ("--- read Opensky Median Climb and Descent Rates")

    fileName = "extendedOpenSkyMedians.csv"
    directoryPath = os.path.join( os.path.dirname(__file__) , "Results" )
    directory = Path(directoryPath)
    if directory.is_dir():
        print ( "it is a directory - {0}".format(directoryPath))
        filePath = os.path.join(directory, fileName)
        print ( filePath )
        
        df = pd.read_csv( filePath , sep = ";")

        print ( list ( df ) )
    
    return df 


def readExtendedAirports():
    
    df = None
    
    fileName = "extendedAirports.csv"
    current_dir = os.getcwd()
        
    directoryPath = os.path.join( os.path.dirname(__file__) , "Results" )
    directory = Path(directoryPath)
    if directory.is_dir():
        print ( "it is a directory - {0}".format(directoryPath))
        filePath = os.path.join(directory, fileName)
        print ( filePath )
        
        df = pd.read_csv( filePath , sep = ";")
        df = df.drop('adep', axis=1)
        df = df.drop('ades', axis=1)

    return df

def readExtendedAirportsRunways():
    
    df = None 
    fileName = 'extendedAirportsRunways.csv'
    current_dir = os.getcwd()
    directoryPath = os.path.join( os.path.dirname(__file__) , "Results" )
    directory = Path(directoryPath)
    if directory.is_dir():
        print ( "it is a directory - {0}".format(directoryPath))
        filePath = os.path.join(directory, fileName)
        print ( filePath )
        
        df = pd.read_csv( filePath , sep = ";")
        df = df.drop('adep', axis=1)
        df = df.drop('ades', axis=1)

    return df

def readExtendedAircrafts():
    
    df = None
    fileName = "extendedAircrafts.csv"
    
    current_dir = os.getcwd()
    directoryPath = os.path.join( os.path.dirname(__file__) , "Results" )
    directory = Path(directoryPath)
    if directory.is_dir():
        print ( "it is a directory - {0}".format(directoryPath))
        filePath = os.path.join(directory, fileName)
        print ( filePath )
        
        df = pd.read_csv( filePath , sep = ";")
        
        for column in ['date','callsign','adep','name_adep','country_code_adep','ades','name_ades','country_code_ades']:
            df = df.drop(column, axis=1)
        for column in ['actual_offblock_time', 'arrival_time', 'aircraft_type', 'wtc', 'airline', 'flight_duration', 'taxiout_time', 'flown_distance', 'tow']:
            df = df.drop(column, axis=1)
        for column in ['adep_elevation_meters', 'ades_elevation_meters', 'adep_latitude_degrees', 'adep_longitude_degrees', 'ades_latitude_degrees', 'ades_longitude_degrees']:
            df = df.drop(column, axis=1)
        for column in ['adep_ades_GC_Nm', 'adep_isa_temperature_degrees', 'ades_isa_temperature_degrees', 'adep_air_density', 'ades_air_density', 'adep_pressure', 'ades_pressure']:
            df = df.drop(column, axis=1)


    return df

def readChallengeSet():
    df = None
    
    print ("--- read challenge set CSV file ---")
    current_dir = os.getcwd()
    print ( current_dir )
    directoryPath = os.path.join( os.path.dirname(__file__) , "AnsPerformanceChallenge" )

    fileName = "challenge_set.csv"
    directory = Path(directoryPath)
    print ( directory )
    if directory.is_dir():
        print ( "it is a directory - {0}".format(directoryPath))
        filePath = os.path.join(directory, fileName)
        print ( filePath )
        
        df = pd.read_csv ( filePath , sep = "," )
    return df


def readSubmissionSet(fileName):
    df = None
    print("--- Read submission set CSV file-> {0}".format(fileName))
    
    #fileName = "final_submission_set.csv"

    current_dir = os.getcwd()
    directoryPath = os.path.join( os.path.dirname(__file__) , "AnsPerformanceChallenge" )

    directory = Path(directoryPath)
    if directory.is_dir():
        print ( "it is a directory - {0}".format(directoryPath))
        filePath = os.path.join(directory, fileName)
        print ( filePath )
        
        df = pd.read_csv ( filePath , sep = "," )
    
    return df

def extractISOYear(dateStr):
    ''' 01/01/2024 '''
    if str(dateStr).find("-")>0:
        date = datetime.strptime(dateStr, DateFormatWithDashes )
    else:
        date = datetime.strptime(dateStr, DateFormatWithSlashes)
    iso_year, iso_week, iso_weekday = date.isocalendar()
    return iso_year

def extractISOWeek(dateStr):
    ''' 01/01/2024 '''
    if str(dateStr).find("-")>0:
        date = datetime.strptime(dateStr, DateFormatWithDashes )
    else:
        date = datetime.strptime(dateStr, DateFormatWithSlashes)
 
    iso_year, iso_week, iso_weekday = date.isocalendar()
    return iso_week

def extractISOWeekDay(dateStr):
    if str(dateStr).find("-")>0:
        date = datetime.strptime(dateStr, DateFormatWithDashes )
    else:
        date = datetime.strptime(dateStr, DateFormatWithSlashes )
 
    iso_year, iso_week, iso_weekday = date.isocalendar()
    return iso_weekday

def extractMonth(dateStr):
    if str(dateStr).find("-")>0:
        date = datetime.strptime(dateStr, DateFormatWithDashes )
    else:
        date = datetime.strptime(dateStr, DateFormatWithSlashes )
 
    return date.month

def oneHotEncoder(columnNameList):
    assert ( isinstance ( columnNameList , list ))
    transformer = make_column_transformer( (OneHotEncoder(), columnNameList ), remainder='passthrough')
    return transformer
    

def extendDataSetWithDates(df):
    
    if ( not df is None ) and ( isinstance(df , pd.DataFrame )):
        print ("--------- extend dataset with dates as integers -----")
        
        df['date_year'] = df.apply ( lambda row : extractISOYear( row['date']), axis=1)
        df['date_month'] = df.apply ( lambda row : extractMonth( row['date']), axis=1)
        df['date_week'] = df.apply ( lambda row : extractISOWeek( row['date']), axis=1)
        df['date_week_day'] = df.apply ( lambda row : extractISOWeekDay( row['date']), axis=1)
        ''' drop string date '''
        df = df.drop(columns=['date'])

    return df

def computePotentialEnergy( aircraft_mass_lb , max_altitude_feet , adep_elevation_meters ):
    aircraft_mass_kilograms = lbToKilograms * aircraft_mass_lb
    max_altitude_meters = max_altitude_feet * feet2Meters
    return aircraft_mass_kilograms * gravity_meter_square_seconds * ( max_altitude_meters - adep_elevation_meters)


def computePotentialPower( aircraft_mass_lb , max_altitude_feet , adep_elevation_meters , flight_duration_minutes ):
    aircraft_mass_kilograms = lbToKilograms * aircraft_mass_lb
    max_altitude_meters = max_altitude_feet * feet2Meters
    potential_energy = aircraft_mass_kilograms * gravity_meter_square_seconds * ( max_altitude_meters - adep_elevation_meters)
    return ( potential_energy / ( flight_duration_minutes * 60.0 ))


def computeKineticEnergy( aircraft_mass_lb , average_ground_speed_knots ):
    aircraft_mass_kilograms = lbToKilograms * aircraft_mass_lb
    average_ground_speed_meters_per_second = average_ground_speed_knots * Knots2MetersSeconds
    return 0.5 * aircraft_mass_kilograms * average_ground_speed_meters_per_second * average_ground_speed_meters_per_second

def computeKineticPower( aircraft_mass_lb , average_ground_speed_knots  ,flight_duration_minutes ):
    aircraft_mass_kilograms = lbToKilograms * aircraft_mass_lb
    average_ground_speed_meters_per_second = average_ground_speed_knots * Knots2MetersSeconds
    kinetic_energy = 0.5 * aircraft_mass_kilograms * average_ground_speed_meters_per_second * average_ground_speed_meters_per_second
    return ( kinetic_energy / ( flight_duration_minutes * 60.0 ) )
    

def extendDataSetWithRunwaysdata(df):

    runWaysDatabase = RunWayDataBase()
    if runWaysDatabase.read():
        print ( '--- runways DB correctly read ---' )
        df['adep_nb_runways'] = df.apply( lambda row: runWaysDatabase.getNumberOfRunways( row['adep']) , axis=1)
        df['ades_nb_runways'] = df.apply( lambda row: runWaysDatabase.getNumberOfRunways( row['ades']) , axis=1)
    
    return df 

def extendDataSetWithAircraftData(df):
    if ( not df is None ) and ( isinstance(df , pd.DataFrame )):
        
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
    return df
                

def extendDataSetWithAirportData(df):
    if ( not df is None ) and ( isinstance(df , pd.DataFrame )):
        
        print ( "Read airports database ")
        
        atmosphere = Atmosphere()
        atmosphereOk = atmosphere.read()
        print ("--- atmosphere read correctly = {0}".format(atmosphereOk))
    
        airportsDatabase = AirportsDatabase()
        airportsDBOk = airportsDatabase.read()
        print ("--- airports read correctly = {0}".format(airportsDBOk))
        
        print ( airportsDBOk )
        if airportsDBOk and atmosphereOk:
        
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
                        
            print ("------- end adding adep ades informations ----------")
            #columnsToDrop = ['ades', 'adep', 'name_adep', 'country_code_adep', 'name_ades' , 'country_code_ades']
            ''' 23 October 2024 - encode adep an ades hence do not drop them here  '''
            ''' 23 October 2024 - encode country codes hence do not drop them here '''
            columnsToDrop = [ 'name_adep', 'name_ades' , 'country_code_adep' , 'country_code_ades']
            df = df.drop(columns=columnsToDrop)
            
            print ( list ( df ) )
        
    return df

def encodeCategoryColumn(df , columnNameToEncode):
    print ( "--- encode category column = {0}".format(columnNameToEncode))
    assert ( isinstance ( df , pd.DataFrame ))
    assert ( isinstance ( columnNameToEncode , str ))
    
    ohe = OneHotEncoder(handle_unknown='ignore')
    df_encoded = pd.DataFrame( ohe.fit_transform( df[[columnNameToEncode]] ).toarray() )
    #print ( ohe.get_feature_names_out( ) )
    
    final_df = df.join( df_encoded )
    final_df = final_df.rename(columns=lambda x: columnNameToEncode + '_' + str(x) if str(x).isdigit() else x)
    
    final_df = final_df.drop(columns=[columnNameToEncode])
    print ( list ( final_df ) )

    print("---- encoding dataframe is finished ---")
    return ohe , df_encoded , final_df


def computeChallengeSubmission():
    
    print(''' ---------- read the challenge train dataset with True TOW values ''')
    df_challenge = readChallengeSet()
    print ( list ( df_challenge ) )
    print( df_challenge.shape )

    fileName = "final_submission_set.csv"
    df_submission = readSubmissionSet(fileName)
    print ( list ( df_submission ) )
    print( df_submission.shape )
    
    print( "--- concat challenge and submission ---")
    ''' If your index is autogenerated and you don't want to keep it, you can use the ignore_index=True option. '''
    ''' This will autogenerate a new index for you '''
    df_concat = pd.concat([df_challenge,df_submission], ignore_index=True)
    print ( df_concat.shape )
    print ( list ( df_concat ))
    return df_concat
