'''
Created on 15 oct. 2024

@author: robert
'''
import os

from utils import readChallengeSet
from utils import readSubmissionSet
from utils import extendDataSetWithAirportData
from utils import extendDataSetWithDates
from utils import extendDataSetWithRunwaysdata
from utils import extendDataSetWithAircraftData
from utils import readExtendedAirportsRunways , readExtendedAirports, readExtendedAircrafts
from utils import readAircraftOpenapData , readOpenSkyMediansClimbDescentRates , readExtendedChallengeSetDurations

from pathlib import Path
from datetime import datetime

from sklearn.metrics import  root_mean_squared_error
from utils import encodeCategoryColumn
import pandas as pd
import xgboost as xgb
from xgboost import XGBRegressor
from extendOpenSkyParquet import extendUsingParquets


def convert_airlines_keys(unique_airlines_values , rowValue):
    order = 0
    for unique_airline_value in unique_airlines_values:
        if ( unique_airline_value == rowValue ):
            return "airline" + "_" + str(order)
        order = order + 1
    return 0


if __name__ == '__main__':
    
    ''' extract flight ids related data to flight ids '''
    ''' ---------------- extract parquet data -----------'''
    
    fileName = 'extendedOpenSky.parquet'
    testMode = False
    extendedParquetIsExisting = True
    if ( extendedParquetIsExisting == True ):
        
        current_dir = os.getcwd()
        directoryPath = os.path.join( current_dir , "Results" )

        directory = Path(directoryPath)
        if directory.is_dir():
            print ( "it is a directory - {0}".format(directoryPath))
            filePath = os.path.join(directory, fileName)
            print (filePath)
            
            df_parquets = pd.read_parquet ( filePath )
            print ( df_parquets.shape )
            print ( list ( df_parquets))
        
    
    print(''' ---------- read the challenge train dataset with True TOW values ''')
    df_challenge = readChallengeSet()
    print ( list ( df_challenge ) )
    print( df_challenge.shape )
    
    ''' extend dates in challenge dataset because date format in challenge and in submission is not the same '''
    df_challenge = extendDataSetWithDates (df_challenge)
    print ( df_challenge.shape )
    
    print (''' ------------- read the submission dataset with empty TOW values ----''')
    fileName = "final_submission_set.csv"
    df_submission = readSubmissionSet(fileName)
    print ( list ( df_submission ) )
    print( df_submission.shape )
    
    ''' extend dates in submission dataset because date format in challenge and in submission is not the same '''
    df_submission = extendDataSetWithDates ( df_submission )
    print ( df_submission.shape )
    
    print( "--- concat challenge and submission ---")
    ''' If your index is autogenerated and you don't want to keep it, you can use the ignore_index=True option. '''
    ''' This will autogenerate a new index for you '''
    df = pd.concat([df_challenge,df_submission], ignore_index=True)
    print ( df.shape )
    print ( list ( df ))
    print ( "number of rows = {0}".format ( len(df.index) ) )

    extendedAirportsIsExisting = True
    if ( extendedAirportsIsExisting == True ):
        
        df_airports = readExtendedAirports()
        
        print ( "--- left join challenge and final submission with runways data ---")
        df = df.merge( df_airports , how="left", on="flight_id"  )
        print ( df.shape )
        print ( list ( df ))
        
        
    extendedAirportsRunwaysIsExisting = True
    if extendedAirportsRunwaysIsExisting == True:
        
        print ( "--- read number of runways per airport Adep or Ades ---")
        df_runways = readExtendedAirportsRunways()
        
        print ( "--- left join challenge and final submission with runways data ---")
        df = df.merge( df_runways , how="left", on="flight_id"  )
        print ( df.shape )
        print ( list ( df ))
 
        
    if ( testMode == False):

        print('''--- left join challenge and submission -> with parquet files data --- ''')
        ''' parquet data is needed in aircrafts extension '''
        #df = df.merge( df_parquets, how="left", on="flight_id" )
        
        print('''--- fill Not a Number ---''')
        #df.fillna(df.mean(), inplace=True)
        columnListWithNan = ['maxAltitudeFeet','maxClimbRateFeetMinutes','avgClimbRateFeetMinutes','maxDescentRateFeetMinutes','avgDescentRateFeetMinutes','avgGroundSpeedKnots','maxGroundSpeedKnots']
        for columnWithNan in columnListWithNan:
            print ("fill Nan in column {0}".format(columnWithNan))
            #df[columnWithNan].fillna(value=0.0, inplace=True)
        
        print ( list ( df ))
        #print ( df.shape )
        
    ''' parquet content is already in the extended aircrafts data '''
    extendedAircraftsDataIsExisting = True
    if extendedAircraftsDataIsExisting == True:
        
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

    extendedOpenSkyMediansIsExisting = True
    if extendedOpenSkyMediansIsExisting == True:

        df_medians = readOpenSkyMediansClimbDescentRates()
        print('''--- left join challenge and submission -> with openSky median climb descent rates --- ''')

        df = df.merge( df_medians, how="left", on="flight_id" )
        print ( df.shape )
        print ( list ( df ))

    extendedClimbDescentCruiseIsExisting = False
    if extendedClimbDescentCruiseIsExisting == True:

        df_durations = readExtendedChallengeSetDurations()
        print('''--- left join challenge and submission -> with openSky median climb descent rates --- ''')

        df = df.merge( df_durations, how="left", on="flight_id" )
        print ( df.shape )
        print ( list ( df ))


    print(''' drop unused columns ''')
    print(''' column containing a string must be dropped because string cannot be converted to float ''')
    #df = df.drop(columns=['flight_id', 'callsign', 'actual_offblock_time','arrival_time'])
    df = df.drop(columns=[ 'callsign', 'actual_offblock_time','arrival_time'])
    print ( list ( df ))
    
    print ("--- encode airline ---")
    unique_airlines_keys = df['airline'].unique()
    #print("unique airlines = {0}".format((unique_airlines_keys)))
    print("number of unique airlines = {0}".format(len(unique_airlines_keys)))
        
    df['airline'] = df['airline'].apply( lambda x : convert_airlines_keys(unique_airlines_keys, x) )
        
    print(''' encoding airline, aircraft type and wtc , adep and ades and their country codes ''')
    
    oheAirline , df_encoded_airline , final_df = encodeCategoryColumn( df , 'airline' )
    oheAircraftType , df_encoded_aircraft_type, final_df = encodeCategoryColumn( final_df , 'aircraft_type')
    oheWTC , df_encoded_wtc , final_df = encodeCategoryColumn(final_df  , 'wtc')
    oheClassEngine , df_encoded_class_engine, final_df = encodeCategoryColumn( final_df , 'physicalClassEngine')
    ''' 23 October 2024 encode adep and ades '''
    oheAdep , df_encoded_adep , final_df = encodeCategoryColumn ( final_df , 'adep')
    oheAdes , df_encoded_ades , final_df = encodeCategoryColumn ( final_df , 'ades')
    ''' 23 October 2024 - Encode adep country code and ades country code '''
    oheAdepCountryCode , df_encoded_adep_country , final_df = encodeCategoryColumn ( final_df , 'country_code_adep')
    oheAdesCountryCode , df_encoded_ades_country , final_df = encodeCategoryColumn ( final_df , 'country_code_ades')
    
    print(list(final_df))
    ''' drop columns containing categories '''
    for column in ['name_adep','name_ades']:
        if column in list(final_df):
            final_df = final_df.drop(column, axis=1)
        
    ''' 27th October 2024 '''
    #final_df = final_df.extendedAircraftsWithOpenap(df)
    
    print ( list ( final_df ))
    print(final_df.head(10))
    
    print ( '--- keep only records with tow being not null ---')
    tow_not_null_df = final_df[final_df['tow'].notnull()]
    print ( tow_not_null_df.shape  )
    
    print ("---- build the train dataset ---")
    ''' Creating a dataframe with 80% values of original dataframe '''
    train_df = tow_not_null_df.sample(frac = 0.8)
    print ( train_df.shape  )
    
    print ("---- get the test dataset  ---")
    print(''' --- creating a dataframe with rest 20% of original dataframe ''')
    test_df = tow_not_null_df.drop(train_df.index)
    print ( test_df.shape )
    
    print ("--- drop tow column in X train -> tow is the prediction ---")
    X_train_df = train_df.drop(columns=['tow'])
    print ( X_train_df.shape )

    print ("--- Y train ---")
    # Keep only 'tow'  column
    Y_train_df = train_df[train_df['tow'].notnull()]
    print ('''--- keep only tow column in Y train ''')
    Y_train_df = Y_train_df[['tow']]
    print ( Y_train_df.shape )
    
    print ( ''' --- call Gradient Boosting Regressor --- ''')
    #regOne = ensemble.GradientBoostingRegressor()
    #regTwo = ensemble.HistGradientBoostingRegressor()
    modelXgb = XGBRegressor(n_estimators=5000,max_depth=13,eta=0.1,subsample=0.9)
    
    #regOne.fit(X_train_df, Y_train_df)
    #regTwo.fit(X_train_df, Y_train_df)
    modelXgb.fit( X_train_df, Y_train_df )
    #print ( estimator.score(X_train_df, Y_train_df) )
    
    print ("---- build X_test -> drop tow column ---")
    X_test_df = test_df.drop(columns=['tow'])
    print ( X_test_df.shape )

    print ("--- build Y test to compare with ---")
    print('''--- keep only the tow column in the Y test ''')
    Y_test_df = test_df[['tow']]
    print ( Y_test_df.shape )

    print ("--- compute Y predictions from X test --- ")
    #Y_predict_df = regOne.predict(X_test_df)
    #Y_predict_df = regTwo.predict(X_test_df)
    Y_predict_df = modelXgb.predict(X_test_df)
    print ( Y_predict_df.shape )
    
    print("--- compute RMSE ---")
    rmse = root_mean_squared_error( Y_test_df, Y_predict_df )
    print("The root mean squared error (MSE) on test set: {:.4f}".format(rmse))

    #mse = mean_squared_error ( Y_test_df , Y_predict_df )
    #print("The mean squared error (MSE) on test set: {:.4f}".format(mse))

    print ("--- apply prediction on tow null rows ---")
    print("--- select rows where tow column has null values ")
    X_submission_df = final_df[final_df['tow'].isnull()]
    print ( X_submission_df.shape  )
    print ( list ( X_submission_df ) )
    
    print ( '''--- drop tow column in X Submission ''')
    X_submission_df = X_submission_df.drop(columns=['tow'])
    X_submission_df.reset_index(drop=True, inplace=True)
    
    print ( X_submission_df.shape  )
    print ( list ( X_submission_df ) )
    print ( X_submission_df.head())
    
    print ('--- compute prediction on submission dataset ---')
    #Y_submission_df = regOne.predict( X_submission_df )
    #Y_submission_df = regTwo.predict( X_submission_df )
    Y_submission_df = modelXgb.predict( X_submission_df )
    
    print ( Y_submission_df.shape )
    
    print ( "--- convert NumPy array to pandas DataFrame")
    Y_submission_df = pd.DataFrame( data=Y_submission_df )
    print ( Y_submission_df.shape )
    
    Y_submission_df.reset_index(drop=True, inplace=True)
    
    print ( list ( Y_submission_df ))
    print ( Y_submission_df.head(10))
    
    
    outputFileName = "final_team_submission"
    outputFileName = outputFileName + '_{0}.csv'.format(datetime.now().strftime("%d-%b-%Y-%Hh%Mm%S"))
    
    current_dir = os.getcwd()
    directoryPath = os.path.join( current_dir , "Results" )
    directory = Path(directoryPath)
    if directory.is_dir():
        print ( "it is a directory - {0}".format(directoryPath))
        filePath = os.path.join(directory, outputFileName)
        print(filePath)
        
        Y_submission_df.to_csv(filePath, sep="," , index=False)
    
