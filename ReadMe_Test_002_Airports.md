$ python trajectory/AdsBtrajectories/extendChallengeSetAirports.py
 ---------- read the challenge train dataset with True TOW values
--- read challenge set CSV file ---
it is a directory - C:\Users\rober\git\flight-profile\trajectory\AdsBtrajectories\AnsPerformanceChallenge
C:\Users\rober\git\flight-profile\trajectory\AdsBtrajectories\AnsPerformanceChallenge\challenge_set.csv
['flight_id', 'date', 'callsign', 'adep', 'name_adep', 'country_code_adep', 'ades', 'name_ades', 'country_code_ades', 'actual_offblock_time', 'arrival_time', 'aircraft_type', 'wtc', 'airline', 'flight_duration', 'taxiout_time', 'flown_distance', 'tow']
(369013, 18)
--- Read submission set CSV file-> final_submission_set.csv
it is a directory - C:\Users\rober\git\flight-profile\trajectory\AdsBtrajectories\AnsPerformanceChallenge
C:\Users\rober\git\flight-profile\trajectory\AdsBtrajectories\AnsPerformanceChallenge\final_submission_set.csv
['flight_id', 'date', 'callsign', 'adep', 'name_adep', 'country_code_adep', 'ades', 'name_ades', 'country_code_ades', 'actual_offblock_time', 'arrival_time', 'aircraft_type', 'wtc', 'airline', 'flight_duration', 'taxiout_time', 'flown_distance', 'tow']
(158149, 18)
--- concat challenge and submission ---
(527162, 18)
['flight_id', 'date', 'callsign', 'adep', 'name_adep', 'country_code_adep', 'ades', 'name_ades', 'country_code_ades', 'actual_offblock_time', 'arrival_time', 'aircraft_type', 'wtc', 'airline', 'flight_duration', 'taxiout_time', 'flown_distance', 'tow']
(527162, 18)
['flight_id', 'date', 'callsign', 'adep', 'name_adep', 'country_code_adep', 'ades', 'name_ades', 'country_code_ades', 'actual_offblock_time', 'arrival_time', 'aircraft_type', 'wtc', 'airline', 'flight_duration', 'taxiout_time', 'flown_distance', 'tow']
--- read Atmosphere ---
--- atmosphere read correctly = True
Read airports database
--- airports database read correctly = True
Read challenge set file
['flight_id', 'date', 'callsign', 'adep', 'name_adep', 'country_code_adep', 'ades', 'name_ades', 'country_code_ades', 'actual_offblock_time', 'arrival_time', 'aircraft_type', 'wtc', 'airline', 'flight_duration', 'taxiout_time', 'flown_distance', 'tow']
number of rows = 527162
--- start adding adep ades informations ----
------- end adding adep ades informations ----------
-----------
0 248763780 EGLL 25.2984
0 248763780 EICK 153.0096
0 248763780 EGLL 51.4775 -0.461389
0 248763780 EICK 51.841269 -8.491111
0 248763780 EGLL 14.786825320000048
0 248763780 EICK 13.963088080000034
-----------
1 248760618 LEBL 3.6576000000000004
1 248760618 KMIA 2.4384
1 248760618 LEBL 41.297078 2.078464
1 248760618 KMIA 25.79325 -80.290556
1 248760618 LEBL 14.92640848000002
1 248760618 KMIA 14.934272320000048
-----------
2 248753824 ESSA 41.757600000000004
2 248753824 KORD 203.6064
2 248753824 ESSA 59.651944 17.918611
2 248753824 KORD 41.978603 -87.904842
2 248753824 ESSA 14.680663480000021
2 248753824 KORD 13.63673872000004
-----------
3 248753852 LSZH 431.59680000000003
3 248753852 KPHL 10.972800000000001
3 248753852 LSZH 47.464722 8.549167
3 248753852 KPHL 39.871944 -75.241139
3 248753852 LSZH 12.166200640000056
3 248753852 KPHL 14.879225440000027
-----------
4 248755934 EIDW 73.7616
4 248755934 EGLL 25.2984
4 248755934 EIDW 53.421333 -6.270075
4 248755934 EGLL 51.4775 -0.461389
4 248755934 EIDW 14.474237680000044
4 248755934 EGLL 14.786825320000048
-----------
5 248762583 ENGM 207.5688
5 248762583 LEAL 43.281600000000005
5 248762583 ENGM 60.193917 11.100361
5 248762583 LEAL 38.282169 -0.558156
5 248762583 ENGM 13.611181240000064
5 248762583 LEAL 14.670833680000044
-----------
6 248758528 EGAC 4.572
6 248758528 EGLL 25.2984
6 248758528 EGAC 54.618056 -5.8725
6 248758528 EGLL 51.4775 -0.461389
6 248758528 EGAC 14.920510600000057
6 248758528 EGLL 14.786825320000048
-----------
7 248752667 LTFM 99.06
7 248752667 LYBE 102.108
7 248752667 LTFM 41.28004 28.72507
7 248752667 LYBE 44.818444 20.309139
7 248752667 LTFM 14.311063000000047
7 248752667 LYBE 14.291403400000036
-----------
8 248762188 KLAX 38.4048
8 248762188 LTFM 99.06
8 248762188 KLAX 33.942536 -118.408075
8 248762188 LTFM 41.28004 28.72507
8 248762188 KLAX 14.70228904000004
8 248762188 LTFM 14.311063000000047
-----------
9 248753189 LTFM 99.06
9 248753189 LTAC 952.5
9 248753189 LTFM 41.28004 28.72507
9 248753189 LTAC 40.128082 32.995083
9 248753189 LTFM 14.311063000000047
9 248753189 LTAC 8.806375000000003
['flight_id', 'adep', 'ades', 'adep_elevation_meters', 'ades_elevation_meters', 'adep_latitude_degrees', 'adep_longitude_degrees', 'ades_latitude_degrees', 'ades_longitude_degrees', 'adep_ades_GC_Nm', 'adep_isa_temperature_degrees', 'ades_isa_temperature_degrees', 'adep_air_density', 'ades_air_density', 'adep_pressure', 'ades_pressure']
it is a directory - C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\Results

rober@RobertPastor MINGW64 ~/git/AnsPRCDataChallenge (master)
$
