rober@RobertPastor MINGW64 ~/git/AnsPRCDataChallenge (master)
$ python trajectory/AdsBtrajectories/extendChallengeSetRunways.py

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
C:\Users\rober\git\AnsPRCDataChallenge
C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\Runways\RunWays.xls
C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\Runways\RunWays.xls
--- runways DB correctly read ---
(527162, 20)
['flight_id', 'date', 'callsign', 'adep', 'name_adep', 'country_code_adep', 'ades', 'name_ades', 'country_code_ades', 'actual_offblock_time', 'arrival_time', 'aircraft_type', 'wtc', 'airline', 'flight_duration', 'taxiout_time', 'flown_distance', 'tow', 'adep_nb_runways', 'ades_nb_runways']
(527162, 5)
['flight_id', 'adep', 'ades', 'adep_nb_runways', 'ades_nb_runways']
it is a directory - C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\Results

rober@RobertPastor MINGW64 ~/git/AnsPRCDataChallenge (master)
