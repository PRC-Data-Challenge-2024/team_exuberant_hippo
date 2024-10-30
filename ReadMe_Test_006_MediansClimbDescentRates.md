rober@RobertPastor MINGW64 ~/git/AnsPRCDataChallenge (master)
$ python trajectory/AdsBtrajectories/extendOpenSkyParquetMedians.py
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
2022-01-01
--- Read parquet file ---
C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\AnsPerformanceChallenge\competition-data
it is a directory - C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\AnsPerformanceChallenge\competition-data
C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\AnsPerformanceChallenge\competition-data\2022-01-01.parquet
['flight_id', 'timestamp', 'latitude', 'longitude', 'altitude', 'groundspeed', 'track', 'vertical_rate', 'icao24', 'u_component_of_wind', 'v_component_of_wind', 'temperature', 'specific_humidity']
['flight_id', 'medianClimbRateFeetMinutes', 'medianDescentRateFeetMinutes']
2022-01-02
--- Read parquet file ---
C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\AnsPerformanceChallenge\competition-data
it is a directory - C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\AnsPerformanceChallenge\competition-data
C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\AnsPerformanceChallenge\competition-data\2022-01-02.parquet
['flight_id', 'timestamp', 'latitude', 'longitude', 'altitude', 'groundspeed', 'track', 'vertical_rate', 'icao24', 'u_component_of_wind', 'v_component_of_wind', 'temperature', 'specific_humidity']
['flight_id', 'medianClimbRateFeetMinutes', 'medianDescentRateFeetMinutes']
2022-01-03
--- Read parquet file ---
C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\AnsPerformanceChallenge\competition-data
it is a directory - C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\AnsPerformanceChallenge\competition-data
C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\AnsPerformanceChallenge\competition-data\2022-01-03.parquet
['flight_id', 'timestamp', 'latitude', 'longitude', 'altitude', 'groundspeed', 'track', 'vertical_rate', 'icao24', 'u_component_of_wind', 'v_component_of_wind', 'temperature', 'specific_humidity']
['flight_id', 'medianClimbRateFeetMinutes', 'medianDescentRateFeetMinutes']
2022-01-04
--- Read parquet file ---


.......


2022-12-29
--- Read parquet file ---
C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\AnsPerformanceChallenge\competition-data
it is a directory - C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\AnsPerformanceChallenge\competition-data
C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\AnsPerformanceChallenge\competition-data\2022-12-29.parquet
['flight_id', 'timestamp', 'latitude', 'longitude', 'altitude', 'groundspeed', 'track', 'vertical_rate', 'icao24', 'u_component_of_wind', 'v_component_of_wind', 'temperature', 'specific_humidity']
['flight_id', 'medianClimbRateFeetMinutes', 'medianDescentRateFeetMinutes']
2022-12-30
--- Read parquet file ---
C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\AnsPerformanceChallenge\competition-data
it is a directory - C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\AnsPerformanceChallenge\competition-data
C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\AnsPerformanceChallenge\competition-data\2022-12-30.parquet
['flight_id', 'timestamp', 'latitude', 'longitude', 'altitude', 'groundspeed', 'track', 'vertical_rate', 'icao24', 'u_component_of_wind', 'v_component_of_wind', 'temperature', 'specific_humidity']
['flight_id', 'medianClimbRateFeetMinutes', 'medianDescentRateFeetMinutes']
2022-12-31
--- Read parquet file ---
C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\AnsPerformanceChallenge\competition-data
it is a directory - C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\AnsPerformanceChallenge\competition-data
C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\AnsPerformanceChallenge\competition-data\2022-12-31.parquet
['flight_id', 'timestamp', 'latitude', 'longitude', 'altitude', 'groundspeed', 'track', 'vertical_rate', 'icao24', 'u_component_of_wind', 'v_component_of_wind', 'temperature', 'specific_humidity']
['flight_id', 'medianClimbRateFeetMinutes', 'medianDescentRateFeetMinutes']
C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\Results
it is a directory - C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\Results
C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\Results\extendedOpenSkyMedians.csv
--- its all finished ---
(527162, 3)
['flight_id', 'medianClimbRateFeetMinutes', 'medianDescentRateFeetMinutes']
    flight_id  medianClimbRateFeetMinutes  medianDescentRateFeetMinutes
0   248763780                        64.0                         -64.0
1   248760618                         0.0                           0.0
2   248753821                         0.0                           0.0
3   248753822                         0.0                           0.0
4   248753824                         0.0                           0.0
..        ...                         ...                           ...
95  248753295                         0.0                           0.0
96  248752828                        64.0                        -576.0
97  248751332                       128.0                        -960.0
98  248753258                        64.0                        -448.0
99  248753260                         0.0                           0.0

[100 rows x 3 columns]

rober@RobertPastor MINGW64 ~/git/AnsPRCDataChallenge (master)
$

