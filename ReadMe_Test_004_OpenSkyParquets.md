python trajectory/AdsBtrajectories/extendOpenSkyParquet.py

...

2022-06-23
--- Read parquet file ---
C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\AnsPerformanceChallenge\competition-data
it is a directory - C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\AnsPerformanceChallenge\competition-data
C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\AnsPerformanceChallenge\competition-data\2022-06-23.parquet
['flight_id', 'timestamp', 'latitude', 'longitude', 'altitude', 'groundspeed', 'track', 'vertical_rate', 'icao24', 'u_component_of_wind', 'v_component_of_wind', 'temperature', 'specific_humidity']
number of unique flight ids = 3259
number of rows = 21382440
number of unique flight ids = 1736
number of rows = 12344614
--- max Altitude feet ---
--- timestamp start ---
--- compute high and low outliers
--- filter outliers ---
--- get max of the timestamp - Top of Descent ---
--- start to top of descent ---
--- max Climb Rate Feet Minutes ---
--- avg climb rate feet minutes---
--- max descent rate feet minutes ---
--- avg descent rate feet minutes---
--- filter not a number in final dataframe
['flight_id', 'maxAltitudeFeet', 'timeStarttoTopOfDescentMin', 'maxClimbRateFeetMinutes', 'avgClimbRateFeetMinutes', 'maxDescentRateFeetMinutes', 'avgDescentRateFeetMinutes', 'avgGroundSpeedKnots', 'maxGroundSpeedKnots']
2022-06-24


...

2022-12-30
--- Read parquet file ---
C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\AnsPerformanceChallenge\competition-data
it is a directory - C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\AnsPerformanceChallenge\competition-data
C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\AnsPerformanceChallenge\competition-data\2022-12-30.parquet
['flight_id', 'timestamp', 'latitude', 'longitude', 'altitude', 'groundspeed', 'track', 'vertical_rate', 'icao24', 'u_component_of_wind', 'v_component_of_wind', 'temperature', 'specific_humidity']
number of unique flight ids = 2102
number of rows = 13986810
number of unique flight ids = 601
number of rows = 5138223
--- max Altitude feet ---
--- timestamp start ---
--- compute high and low outliers
--- filter outliers ---
--- get max of the timestamp - Top of Descent ---
--- start to top of descent ---
--- max Climb Rate Feet Minutes ---
--- avg climb rate feet minutes---
--- max descent rate feet minutes ---
--- avg descent rate feet minutes---
--- filter not a number in final dataframe
['flight_id', 'maxAltitudeFeet', 'timeStarttoTopOfDescentMin', 'maxClimbRateFeetMinutes', 'avgClimbRateFeetMinutes', 'maxDescentRateFeetMinutes', 'avgDescentRateFeetMinutes', 'avgGroundSpeedKnots', 'maxGroundSpeedKnots']
2022-12-31
--- Read parquet file ---
C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\AnsPerformanceChallenge\competition-data
it is a directory - C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\AnsPerformanceChallenge\competition-data
C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\AnsPerformanceChallenge\competition-data\2022-12-31.parquet
['flight_id', 'timestamp', 'latitude', 'longitude', 'altitude', 'groundspeed', 'track', 'vertical_rate', 'icao24', 'u_component_of_wind', 'v_component_of_wind', 'temperature', 'specific_humidity']
number of unique flight ids = 1601
number of rows = 9718322
number of unique flight ids = 424
number of rows = 3506905
--- max Altitude feet ---
--- timestamp start ---
--- compute high and low outliers
--- filter outliers ---
--- get max of the timestamp - Top of Descent ---
--- start to top of descent ---
--- max Climb Rate Feet Minutes ---
--- avg climb rate feet minutes---
--- max descent rate feet minutes ---
--- avg descent rate feet minutes---
--- filter not a number in final dataframe
['flight_id', 'maxAltitudeFeet', 'timeStarttoTopOfDescentMin', 'maxClimbRateFeetMinutes', 'avgClimbRateFeetMinutes', 'maxDescentRateFeetMinutes', 'avgDescentRateFeetMinutes', 'avgGroundSpeedKnots', 'maxGroundSpeedKnots']
C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\Results
it is a directory - C:\Users\rober\git\AnsPRCDataChallenge\trajectory\AdsBtrajectories\Results
--- its all finished ---
(527162, 9)
['flight_id', 'maxAltitudeFeet', 'timeStarttoTopOfDescentMin', 'maxClimbRateFeetMinutes', 'avgClimbRateFeetMinutes', 'maxDescentRateFeetMinutes', 'avgDescentRateFeetMinutes', 'avgGroundSpeedKnots', 'maxGroundSpeedKnots']
    flight_id  maxAltitudeFeet  ...  avgGroundSpeedKnots  maxGroundSpeedKnots
0   248763780          31975.0  ...           317.680733                390.0
1   248760618          33025.0  ...           422.276898                495.0
2   248753821          33975.0  ...           397.074774                445.0
3   248753822          39975.0  ...           386.886045                454.0
4   248753824          35975.0  ...           360.673250                470.0
..        ...              ...  ...                  ...                  ...
95  248753295          36975.0  ...           456.725447                538.0
96  248752828          37975.0  ...           266.962029                419.0
97  248751332          32075.0  ...           386.337765                520.0
98  248753258          23900.0  ...           275.047989                378.0
99  248753260          35975.0  ...           373.189859                413.0

[100 rows x 9 columns]

rober@RobertPastor MINGW64 ~/git/AnsPRCDataChallenge (master)
$ 

