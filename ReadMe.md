## dependencies
openap -> used to get aircrafts characteristics
sklearn -> root mean square
xgboost -> the XGBregressor

## to improve the performance a set of CSV files are computed before hand


## pre requesite

download all the 2022 parquet files in the AnsPerformanceChallenge folder

## to improve performances, all 2023 parquet files are read one by one and analysed
## only the flights ids found in the challengeSet and in the final submission set are considered

execute "extendOpenSkyParquet.py" file to analyse all the parquet files and generate a final parquet file with only the flight_ids from the challenge and the submission set

execute "extendChallengeSetAircrafts.py" should produce "extendedAircrafts.csv" in the "Results" folder
execute "extendChallengeSetAirports.py" should produce "extendedAirports.csv" in the "Results" folder
execute "extendChallengeSetRunways.py" should produce "extendedAirportsRunways.csv" in the "Results" folder

execute "RunWaysDatabase_test.py" in order to check access to the Runways database located in Runways folder

execute "extendChallengeSetOpenap.py" should produce "extendedOpenap_ceiling.csv" 
execute "extendChallengeSetOpenapCruise.py" should produce "extendedOpenap_cruise_mach.csv"

## main script compute the submission CSV file

execute "allInOneTrainTest.py" -> should create in "Results" a file "final_team_submission_DD-MMM-2024-HHhmmms.csv"

open the file "createSubmissionCsvFile.py" and 
   1) modify the inputFileName = "final_team_submission_23-Oct-2024-23h48m59.csv"
   2) modify the version line 63

    teamId = "f8afb85a-8f3f-4270-b0bd-10f9ba83adf4"
    teamName = "team_exuberant_hippo"
    version = "v8"
    outputFileName = teamName + "_" + version + "_" + teamId + ".csv"

## launch the createSubmissionCsvFile.py to generate in the Results folder the file to be set to the S3 bucket
team_exuberant_hippo_v8_f8afb85a-8f3f-4270-b0bd-10f9ba83adf4.csv 


## list of columns added in each step of the computation

## from challenge_set.csv and final_submission.csv

['flight_id', 'date', 'callsign', 'adep', 'name_adep', 'country_code_adep', 'ades', 'name_ades', 'country_code_ades', 'actual_offblock_time', 'arrival_time', 'aircraft_type', 'wtc', 'airline', 'flight_duration', 'taxiout_time', 'flown_distance', 'tow']

for each initial set, the DateTime string pattern is converted to 4 ISO integers ->  'date_year', 'date_month', 'date_week', 'date_week_day' -> added to the list of columns

## after converting datetime we got the following list of columns

['flight_id', 'callsign', 'adep', 'name_adep', 'country_code_adep', 'ades', 'name_ades', 'country_code_ades', 'actual_offblock_time', 'arrival_time', 'aircraft_type', 'wtc', 'airline', 'flight_duration', 'taxiout_time', 'flown_distance', 'tow', 'date_year', 'date_month', 'date_week', 'date_week_day']

## extend with airports data

['flight_id', 'callsign', 'adep', 'name_adep', 'country_code_adep', 'ades', 'name_ades', 'country_code_ades', 'actual_offblock_time', 'arrival_time', 'aircraft_type', 'wtc', 'airline', 'flight_duration', 'taxiout_time', 'flown_distance', 'tow', 'date_year', 'date_month', 'date_week', 'date_week_day', 'adep_elevation_meters', 'ades_elevation_meters', 'adep_latitude_degrees', 'adep_longitude_degrees', 'ades_latitude_degrees', 'ades_longitude_degrees', 'adep_ades_GC_Nm', 'adep_isa_temperature_degrees', 'ades_isa_temperature_degrees', 'adep_air_density', 'ades_air_density', 'adep_pressure', 'ades_pressure']

## extend with runways data
## number of runways for each airport is a way to add a parameter related to the taxi time

['flight_id', 'callsign', 'adep', 'name_adep', 'country_code_adep', 'ades', 'name_ades', 'country_code_ades', 'actual_offblock_time', 'arrival_time', 'aircraft_type', 'wtc', 'airline', 'flight_duration', 'taxiout_time', 'flown_distance', 'tow', 'date_year', 'date_month', 'date_week', 'date_week_day', 'adep_elevation_meters', 'ades_elevation_meters', 'adep_latitude_degrees', 'adep_longitude_degrees', 'ades_latitude_degrees', 'ades_longitude_degrees', 'adep_ades_GC_Nm', 'adep_isa_temperature_degrees', 'ades_isa_temperature_degrees', 'adep_air_density', 'ades_air_density', 'adep_pressure', 'ades_pressure', 'adep_nb_runways', 'ades_nb_runways']

## extend with aircraft data (from the FAA file)
## extend with parquet data -> this adds the following columns 

 'maxAltitudeFeet', 'timeStarttoTopOfDescentMin', 'maxClimbRateFeetMinutes', 'avgClimbRateFeetMinutes', 'maxDescentRateFeetMinutes', 'avgDescentRateFeetMinutes', 'avgGroundSpeedKnots', 'maxGroundSpeedKnots'

['flight_id', 'callsign', 'adep', 'name_adep', 'country_code_adep', 'ades', 'name_ades', 'country_code_ades', 'actual_offblock_time', 'arrival_time', 'aircraft_type', 'wtc', 'airline', 'flight_duration', 'taxiout_time', 'flown_distance', 'tow', 'date_year', 'date_month', 'date_week', 'date_week_day', 'adep_elevation_meters', 'ades_elevation_meters', 'adep_latitude_degrees', 'adep_longitude_degrees', 'ades_latitude_degrees', 'ades_longitude_degrees', 'adep_ades_GC_Nm', 'adep_isa_temperature_degrees', 'ades_isa_temperature_degrees', 'adep_air_density', 'ades_air_density', 'adep_pressure', 'ades_pressure', 'adep_nb_runways', 'ades_nb_runways', 'maxAltitudeFeet', 'timeStarttoTopOfDescentMin', 'maxClimbRateFeetMinutes', 'avgClimbRateFeetMinutes', 'maxDescentRateFeetMinutes', 'avgDescentRateFeetMinutes', 'avgGroundSpeedKnots', 'maxGroundSpeedKnots', 'aircraft_mtow_lb', 'aircraft_mlaw_lb', 'potential_energy', 'kinetic_energy', 'potential_power', 'kinetic_power', 'physicalClassEngine', 'NumEngines', 'approachSpeedKnots']

## add openap aircraft data -> this adds 'mtow', 'mlw', 'oew', 'mfc', 'vmo', 'ceiling'

['flight_id', 'callsign', 'adep', 'name_adep', 'country_code_adep', 'ades', 'name_ades', 'country_code_ades', 'actual_offblock_time', 'arrival_time', 'aircraft_type', 'wtc', 'airline', 'flight_duration', 'taxiout_time', 'flown_distance', 'tow', 'date_year', 'date_month', 'date_week', 'date_week_day', 'adep_elevation_meters', 'ades_elevation_meters', 'adep_latitude_degrees', 'adep_longitude_degrees', 'ades_latitude_degrees', 'ades_longitude_degrees', 'adep_ades_GC_Nm', 'adep_isa_temperature_degrees', 'ades_isa_temperature_degrees', 'adep_air_density', 'ades_air_density', 'adep_pressure', 'ades_pressure', 'adep_nb_runways', 'ades_nb_runways', 'maxAltitudeFeet', 'timeStarttoTopOfDescentMin', 'maxClimbRateFeetMinutes', 'avgClimbRateFeetMinutes', 'maxDescentRateFeetMinutes', 'avgDescentRateFeetMinutes', 'avgGroundSpeedKnots', 'maxGroundSpeedKnots', 'aircraft_mtow_lb', 'aircraft_mlaw_lb', 'potential_energy', 'kinetic_energy', 'potential_power', 'kinetic_power', 'physicalClassEngine', 'NumEngines', 'approachSpeedKnots', 'mtow', 'mlw', 'oew', 'mfc', 'vmo', 'ceiling']

## from openap add cruise height and cruise mach 

['flight_id', 'adep', 'name_adep', 'country_code_adep', 'ades', 'name_ades', 'country_code_ades', 'aircraft_type', 'wtc', 'airline', 'flight_duration', 'taxiout_time', 'flown_distance', 'tow', 'date_year', 'date_month', 'date_week', 'date_week_day', 'adep_elevation_meters', 'ades_elevation_meters', 'adep_latitude_degrees', 'adep_longitude_degrees', 'ades_latitude_degrees', 'ades_longitude_degrees', 'adep_ades_GC_Nm', 'adep_isa_temperature_degrees', 'ades_isa_temperature_degrees', 'adep_air_density', 'ades_air_density', 'adep_pressure', 'ades_pressure', 'adep_nb_runways', 'ades_nb_runways', 'maxAltitudeFeet', 'timeStarttoTopOfDescentMin', 'maxClimbRateFeetMinutes', 'avgClimbRateFeetMinutes', 'maxDescentRateFeetMinutes', 'avgDescentRateFeetMinutes', 'avgGroundSpeedKnots', 'maxGroundSpeedKnots', 'aircraft_mtow_lb', 'aircraft_mlaw_lb', 'potential_energy', 'kinetic_energy', 'potential_power', 'kinetic_power', 'physicalClassEngine', 'NumEngines', 'approachSpeedKnots', 'mtow', 'mlw', 'oew', 'mfc', 'vmo', 'ceiling', 'height', 'mach']

## encode the airlines

['flight_id', 'adep', 'name_adep', 'country_code_adep', 'ades', 'name_ades', 'country_code_ades', 'aircraft_type', 'wtc', 'flight_duration', 'taxiout_time', 'flown_distance', 'tow', 'date_year', 'date_month', 'date_week', 'date_week_day', 'adep_elevation_meters', 'ades_elevation_meters', 'adep_latitude_degrees', 'adep_longitude_degrees', 'ades_latitude_degrees', 'ades_longitude_degrees', 'adep_ades_GC_Nm', 'adep_isa_temperature_degrees', 'ades_isa_temperature_degrees', 'adep_air_density', 'ades_air_density', 'adep_pressure', 'ades_pressure', 'adep_nb_runways', 'ades_nb_runways', 'maxAltitudeFeet', 'timeStarttoTopOfDescentMin', 'maxClimbRateFeetMinutes', 'avgClimbRateFeetMinutes', 'maxDescentRateFeetMinutes', 'avgDescentRateFeetMinutes', 'avgGroundSpeedKnots', 'maxGroundSpeedKnots', 'aircraft_mtow_lb', 'aircraft_mlaw_lb', 'potential_energy', 'kinetic_energy', 'potential_power', 'kinetic_power', 'physicalClassEngine', 'NumEngines', 'approachSpeedKnots', 'mtow', 'mlw', 'oew', 'mfc', 'vmo', 'ceiling', 'height', 'mach', 'airline_0', 'airline_1', 'airline_2', 'airline_3', 'airline_4', 'airline_5', 'airline_6', 'airline_7', 'airline_8', 'airline_9', 'airline_10', 'airline_11', 'airline_12', 'airline_13', 'airline_14', 'airline_15', 'airline_16', 'airline_17', 'airline_18', 'airline_19', 'airline_20', 'airline_21', 'airline_22', 'airline_23', 'airline_24', 'airline_25', 'airline_26', 'airline_27', 'airline_28', 'airline_29']

## encode the aircraft_type

['flight_id', 'adep', 'name_adep', 'country_code_adep', 'ades', 'name_ades', 'country_code_ades', 'wtc', 'flight_duration', 'taxiout_time', 'flown_distance', 'tow', 'date_year', 'date_month', 'date_week', 'date_week_day', 'adep_elevation_meters', 'ades_elevation_meters', 'adep_latitude_degrees', 'adep_longitude_degrees', 'ades_latitude_degrees', 'ades_longitude_degrees', 'adep_ades_GC_Nm', 'adep_isa_temperature_degrees', 'ades_isa_temperature_degrees', 'adep_air_density', 'ades_air_density', 'adep_pressure', 'ades_pressure', 'adep_nb_runways', 'ades_nb_runways', 'maxAltitudeFeet', 'timeStarttoTopOfDescentMin', 'maxClimbRateFeetMinutes', 'avgClimbRateFeetMinutes', 'maxDescentRateFeetMinutes', 'avgDescentRateFeetMinutes', 'avgGroundSpeedKnots', 'maxGroundSpeedKnots', 'aircraft_mtow_lb', 'aircraft_mlaw_lb', 'potential_energy', 'kinetic_energy', 'potential_power', 'kinetic_power', 'physicalClassEngine', 'NumEngines', 'approachSpeedKnots', 'mtow', 'mlw', 'oew', 'mfc', 'vmo', 'ceiling', 'height', 'mach', 'airline_0', 'airline_1', 'airline_2', 'airline_3', 'airline_4', 'airline_5', 'airline_6', 'airline_7', 'airline_8', 'airline_9', 'airline_10', 'airline_11', 'airline_12', 'airline_13', 'airline_14', 'airline_15', 'airline_16', 'airline_17', 'airline_18', 'airline_19', 'airline_20', 'airline_21', 'airline_22', 'airline_23', 'airline_24', 'airline_25', 'airline_26', 'airline_27', 'airline_28', 'airline_29', 'aircraft_type_0', 'aircraft_type_1', 'aircraft_type_2', 'aircraft_type_3', 'aircraft_type_4', 'aircraft_type_5', 'aircraft_type_6', 'aircraft_type_7', 'aircraft_type_8', 'aircraft_type_9', 'aircraft_type_10', 'aircraft_type_11', 'aircraft_type_12', 'aircraft_type_13', 'aircraft_type_14', 'aircraft_type_15', 'aircraft_type_16', 'aircraft_type_17', 'aircraft_type_18', 'aircraft_type_19', 'aircraft_type_20', 'aircraft_type_21', 'aircraft_type_22', 'aircraft_type_23', 'aircraft_type_24', 'aircraft_type_25', 'aircraft_type_26', 'aircraft_type_27', 'aircraft_type_28', 'aircraft_type_29']

### encode wake turbulence wtc

['flight_id', 'adep', 'name_adep', 'country_code_adep', 'ades', 'name_ades', 'country_code_ades', 'flight_duration', 'taxiout_time', 'flown_distance', 'tow', 'date_year', 'date_month', 'date_week', 'date_week_day', 'adep_elevation_meters', 'ades_elevation_meters', 'adep_latitude_degrees', 'adep_longitude_degrees', 'ades_latitude_degrees', 'ades_longitude_degrees', 'adep_ades_GC_Nm', 'adep_isa_temperature_degrees', 'ades_isa_temperature_degrees', 'adep_air_density', 'ades_air_density', 'adep_pressure', 'ades_pressure', 'adep_nb_runways', 'ades_nb_runways', 'maxAltitudeFeet', 'timeStarttoTopOfDescentMin', 'maxClimbRateFeetMinutes', 'avgClimbRateFeetMinutes', 'maxDescentRateFeetMinutes', 'avgDescentRateFeetMinutes', 'avgGroundSpeedKnots', 'maxGroundSpeedKnots', 'aircraft_mtow_lb', 'aircraft_mlaw_lb', 'potential_energy', 'kinetic_energy', 'potential_power', 'kinetic_power', 'physicalClassEngine', 'NumEngines', 'approachSpeedKnots', 'mtow', 'mlw', 'oew', 'mfc', 'vmo', 'ceiling', 'height', 'mach', 'airline_0', 'airline_1', 'airline_2', 'airline_3', 'airline_4', 'airline_5', 'airline_6', 'airline_7', 'airline_8', 'airline_9', 'airline_10', 'airline_11', 'airline_12', 'airline_13', 'airline_14', 'airline_15', 'airline_16', 'airline_17', 'airline_18', 'airline_19', 'airline_20', 'airline_21', 'airline_22', 'airline_23', 'airline_24', 'airline_25', 'airline_26', 'airline_27', 'airline_28', 'airline_29', 'aircraft_type_0', 'aircraft_type_1', 'aircraft_type_2', 'aircraft_type_3', 'aircraft_type_4', 'aircraft_type_5', 'aircraft_type_6', 'aircraft_type_7', 'aircraft_type_8', 'aircraft_type_9', 'aircraft_type_10', 'aircraft_type_11', 'aircraft_type_12', 'aircraft_type_13', 'aircraft_type_14', 'aircraft_type_15', 'aircraft_type_16', 'aircraft_type_17', 'aircraft_type_18', 'aircraft_type_19', 'aircraft_type_20', 'aircraft_type_21', 'aircraft_type_22', 'aircraft_type_23', 'aircraft_type_24', 'aircraft_type_25', 'aircraft_type_26', 'aircraft_type_27', 'aircraft_type_28', 'aircraft_type_29', 'wtc_0', 'wtc_1']

## encode physical class engine - jet or turboprop

['flight_id', 'adep', 'name_adep', 'country_code_adep', 'ades', 'name_ades', 'country_code_ades', 'flight_duration', 'taxiout_time', 'flown_distance', 'tow', 'date_year', 'date_month', 'date_week', 'date_week_day', 'adep_elevation_meters', 'ades_elevation_meters', 'adep_latitude_degrees', 'adep_longitude_degrees', 'ades_latitude_degrees', 'ades_longitude_degrees', 'adep_ades_GC_Nm', 'adep_isa_temperature_degrees', 'ades_isa_temperature_degrees', 'adep_air_density', 'ades_air_density', 'adep_pressure', 'ades_pressure', 'adep_nb_runways', 'ades_nb_runways', 'maxAltitudeFeet', 'timeStarttoTopOfDescentMin', 'maxClimbRateFeetMinutes', 'avgClimbRateFeetMinutes', 'maxDescentRateFeetMinutes', 'avgDescentRateFeetMinutes', 'avgGroundSpeedKnots', 'maxGroundSpeedKnots', 'aircraft_mtow_lb', 'aircraft_mlaw_lb', 'potential_energy', 'kinetic_energy', 'potential_power', 'kinetic_power', 'NumEngines', 'approachSpeedKnots', 'mtow', 'mlw', 'oew', 'mfc', 'vmo', 'ceiling', 'height', 'mach', 'airline_0', 'airline_1', 'airline_2', 'airline_3', 'airline_4', 'airline_5', 'airline_6', 'airline_7', 'airline_8', 'airline_9', 'airline_10', 'airline_11', 'airline_12', 'airline_13', 'airline_14', 'airline_15', 'airline_16', 'airline_17', 'airline_18', 'airline_19', 'airline_20', 'airline_21', 'airline_22', 'airline_23', 'airline_24', 'airline_25', 'airline_26', 'airline_27', 'airline_28', 'airline_29', 'aircraft_type_0', 'aircraft_type_1', 'aircraft_type_2', 'aircraft_type_3', 'aircraft_type_4', 'aircraft_type_5', 'aircraft_type_6', 'aircraft_type_7', 'aircraft_type_8', 'aircraft_type_9', 'aircraft_type_10', 'aircraft_type_11', 'aircraft_type_12', 'aircraft_type_13', 'aircraft_type_14', 'aircraft_type_15', 'aircraft_type_16', 'aircraft_type_17', 'aircraft_type_18', 'aircraft_type_19', 'aircraft_type_20', 'aircraft_type_21', 'aircraft_type_22', 'aircraft_type_23', 'aircraft_type_24', 'aircraft_type_25', 'aircraft_type_26', 'aircraft_type_27', 'aircraft_type_28', 'aircraft_type_29', 'wtc_0', 'wtc_1', 'physicalClassEngine_0', 'physicalClassEngine_1']

## encode adep and ades

## use challenge set with tow not null and split it in 80 / 20 %
## train using challenge

## compute RMSE
The root mean squared error (MSE) on test set: 2939.7507
add median instead of average
The root mean squared error (MSE) on test set: 2870.2141
add durations of climb descent and cruise
The root mean squared error (MSE) on test set: 2955.6551
The root mean squared error (MSE) on test set: 2907.8136
add openap pax data high low max
The root mean squared error (MSE) on test set: 2919.5714
add isDomestic 
The root mean squared error (MSE) on test set: 2914.5551


## isolate the Y_to_predict based upon tow is null
## launch the Y_prediction and build the "submission" CSV file
## as this CSV submission file has only the TOW value, launch create Submission.py to obtain a file with the flight_ids and the tow

## correct the script "createSubmissionCsvFile.py" in order to reference the latest Results file created by AllInOneTrainTest.py
## this script merges the list of flight_ids with the "tow" results

## send the team_exuberant_hippo_v8_f8afb85a-8f3f-4270-b0bd-10f9ba83adf4.csv to the S3 submission bucket.