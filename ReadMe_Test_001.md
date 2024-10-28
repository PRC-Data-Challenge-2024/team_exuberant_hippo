rober@RobertPastor MINGW64 ~/git/AnsPRCDataChallenge (master)
$ python trajectory/AdsBtrajectories/extendChallengeSetAircrafts.py
C:\Users\rober\git\AnsPRCDataChallenge
 ---------- read the challenge train dataset with True TOW values
--- read challenge set CSV file ---
C:\Users\rober\git\AnsPRCDataChallenge
C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\AnsPerformanceChallenge
it is a directory - C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\AnsPerformanceChallenge
C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\AnsPerformanceChallenge\challenge_set.csv
['flight_id', 'date', 'callsign', 'adep', 'name_adep', 'country_code_adep', 'ades', 'name_ades', 'country_code_ades', 'actual_offblock_time', 'arrival_time', 'aircraft_type', 'wtc', 'airline', 'flight_duration', 'taxiout_time', 'flown_distance', 'tow']
(369013, 18)
--- Read submission set CSV file-> final_submission_set.csv
it is a directory - C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\AnsPerformanceChallenge
C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\AnsPerformanceChallenge\final_submission_set.csv
['flight_id', 'date', 'callsign', 'adep', 'name_adep', 'country_code_adep', 'ades', 'name_ades', 'country_code_ades', 'actual_offblock_time', 'arrival_time', 'aircraft_type', 'wtc', 'airline', 'flight_duration', 'taxiout_time', 'flown_distance', 'tow']
(158149, 18)
--- concat challenge and submission ---
(527162, 18)
['flight_id', 'date', 'callsign', 'adep', 'name_adep', 'country_code_adep', 'ades', 'name_ades', 'country_code_ades', 'actual_offblock_time', 'arrival_time', 'aircraft_type', 'wtc', 'airline', 'flight_duration', 'taxiout_time', 'flown_distance', 'tow']
(527162, 18)
['flight_id', 'date', 'callsign', 'adep', 'name_adep', 'country_code_adep', 'ades', 'name_ades', 'country_code_ades', 'actual_offblock_time', 'arrival_time', 'aircraft_type', 'wtc', 'airline', 'flight_duration', 'taxiout_time', 'flown_distance', 'tow']
it is a directory - C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\Results
C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\Results\extendedAirports.csv
['flight_id', 'adep_elevation_meters', 'ades_elevation_meters', 'adep_latitude_degrees', 'adep_longitude_degrees', 'ades_latitude_degrees', 'ades_longitude_degrees', 'adep_ades_GC_Nm', 'adep_isa_temperature_degrees', 'ades_isa_temperature_degrees', 'adep_air_density', 'ades_air_density', 'adep_pressure', 'ades_pressure']
--- left join challenge and final submission with runways data ---
['flight_id', 'date', 'callsign', 'adep', 'name_adep', 'country_code_adep', 'ades', 'name_ades', 'country_code_ades', 'actual_offblock_time', 'arrival_time', 'aircraft_type', 'wtc', 'airline', 'flight_duration', 'taxiout_time', 'flown_distance', 'tow', 'adep_elevation_meters', 'ades_elevation_meters', 'adep_latitude_degrees', 'adep_longitude_degrees', 'ades_latitude_degrees', 'ades_longitude_degrees', 'adep_ades_GC_Nm', 'adep_isa_temperature_degrees', 'ades_isa_temperature_degrees', 'adep_air_density', 'ades_air_density', 'adep_pressure', 'ades_pressure']
--- read extended OpenSky parquet ---
it is a directory - C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\Results
C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\Results\extendedOpenSky.parquet
(979680, 9)
['flight_id', 'maxAltitudeFeet', 'timeStarttoTopOfDescentMin', 'maxClimbRateFeetMinutes', 'avgClimbRateFeetMinutes', 'maxDescentRateFeetMinutes', 'avgDescentRateFeetMinutes', 'avgGroundSpeedKnots', 'maxGroundSpeedKnots']
--- left join challenge and submission -> with parquet files data ---
--- Read aircrafts database
it is a directory - C:\Users\rober\git\flight-profile\trajectory\AdsBtrajectories\Aircrafts
C:\Users\rober\git\flight-profile\trajectory\AdsBtrajectories\Aircrafts\FAA-Aircraft-Char-DB-AC-150-5300-13B-App-2023-09-07.xlsx
(387, 56)
['ICAO_Code', 'FAA_Designator', 'Manufacturer', 'Model_FAA', 'Model_BADA', 'Physical_Class_Engine', 'Num_Engines', 'AAC', 'AAC_minimum', 'AAC_maximum', 'ADG', 'TDG', 'Approach_Speed_knot', 'Approach_Speed_minimum_knot', 'Approach_Speed_maximum_knot', 'Wingspan_ft_without_winglets_sharklets', 'Wingspan_ft_with_winglets_sharklets', 'Length_ft', 'Tail_Height_at_OEW_ft', 'Wheelbase_ft', 'Cockpit_to_Main_Gear_ft', 'Main_Gear_Width_ft', 'MTOW_lb', 'MALW_lb', 'Main_Gear_Config', 'ICAO_WTC', 'Parking_Area_ft2', 'Class', 'FAA_Weight', 'CWT', 'One_Half_Wake_Category', 'Two_Wake_Category_Appx_A', 'Two_Wake_Category_Appx_B', 'Rotor_Diameter_ft', 'SRS', 'LAHSO', 'FAA_Registry', 'Registration_Count', 'Total_IFR_Operations_2021_2022', 'Remarks', 'Unnamed: 40', 'Unnamed: 41', 'Unnamed: 42', 'Unnamed: 43', 'Unnamed: 44', 'Unnamed: 45', 'Unnamed: 46', 'Unnamed: 47', 'Unnamed: 48', 'Unnamed: 49', 'Unnamed: 50', 'Unnamed: 51', 'Unnamed: 52', 'Unnamed: 53', 'Unnamed: 54', 'Unnamed: 55']
  ICAO_Code FAA_Designator Manufacturer  ... Unnamed: 53 Unnamed: 54 Unnamed: 55
0       A10            A10    FAIRCHILD  ...         NaN         NaN         NaN
1      A124           A124      ANTONOV  ...         NaN         NaN         NaN
2      A19N           A19N       AIRBUS  ...         NaN         NaN         NaN
3      A20N           A20N       AIRBUS  ...         NaN         NaN         NaN
4      A21N           A21N       AIRBUS  ...         NaN         NaN         NaN

[5 rows x 56 columns]
--- aircraft database read correctly
--- start adding aircraft informations ----
['flight_id', 'date', 'callsign', 'adep', 'name_adep', 'country_code_adep', 'ades', 'name_ades', 'country_code_ades', 'actual_offblock_time', 'arrival_time', 'aircraft_type', 'wtc', 'airline', 'flight_duration', 'taxiout_time', 'flown_distance', 'tow', 'adep_elevation_meters', 'ades_elevation_meters', 'adep_latitude_degrees', 'adep_longitude_degrees', 'ades_latitude_degrees', 'ades_longitude_degrees', 'adep_ades_GC_Nm', 'adep_isa_temperature_degrees', 'ades_isa_temperature_degrees', 'adep_air_density', 'ades_air_density', 'adep_pressure', 'ades_pressure', 'maxAltitudeFeet', 'timeStarttoTopOfDescentMin', 'maxClimbRateFeetMinutes', 'avgClimbRateFeetMinutes', 'maxDescentRateFeetMinutes', 'avgDescentRateFeetMinutes', 'avgGroundSpeedKnots', 'maxGroundSpeedKnots', 'aircraft_mtow_lb', 'aircraft_mlaw_lb', 'potential_energy', 'kinetic_energy', 'potential_power', 'kinetic_power', 'physicalClassEngine', 'NumEngines', 'approachSpeedKnots']
it is a directory - C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\Results

rober@RobertPastor MINGW64 ~/git/AnsPRCDataChallenge (master)
$
