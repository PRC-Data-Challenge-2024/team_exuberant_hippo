rober@RobertPastor MINGW64 ~
$ cd "C:\Users\rober\git\AnsPRCDataChallenge"

rober@RobertPastor MINGW64 ~/git/AnsPRCDataChallenge (master)
$ python trajectory/AdsBtrajectories/findMissingAirports.py
Read airports database
True
 ---------- read the challenge train dataset with True TOW values
--- read challenge set CSV file ---
it is a directory - C:\Users\rober\git\flight-profile\trajectory\AdsBtrajectories\AnsPerformanceChallenge
C:\Users\rober\git\flight-profile\trajectory\AdsBtrajectories\AnsPerformanceChallenge\challenge_set.csv
<class 'pandas.core.frame.DataFrame'>
['flight_id', 'date', 'callsign', 'adep', 'name_adep', 'country_code_adep', 'ades', 'name_ades', 'country_code_ades', 'actual_offblock_time', 'arrival_time', 'aircraft_type', 'wtc', 'airline', 'flight_duration', 'taxiout_time', 'flown_distance', 'tow']
(369013, 18)
unique ADEPs  =     airport
0      EGLL
1      LEBL
2      ESSA
3      LSZH
4      EIDW
..      ...
455    EFRO
456    LDRI
457    HAAB
458    OPKC
459    VTSG

[460 rows x 1 columns]
unique ADESs  =     airport
0      EICK
1      KMIA
2      KORD
3      KPHL
4      EGLL
..      ...
362    FAOR
363    OPLA
364    EFRO
365    OKBK
366    OMSJ

[367 rows x 1 columns]
    airport
0      EGLL
1      LEBL
2      ESSA
3      LSZH
4      EIDW
..      ...
822    FAOR
823    OPLA
824    EFRO
825    OKBK
826    OMSJ

[827 rows x 1 columns]
 ------------- read the submission dataset with empty TOW values ----
--- Read submission set CSV file-> final_submission_set.csv
it is a directory - C:\Users\rober\git\flight-profile\trajectory\AdsBtrajectories\AnsPerformanceChallenge
C:\Users\rober\git\flight-profile\trajectory\AdsBtrajectories\AnsPerformanceChallenge\final_submission_set.csv
['flight_id', 'date', 'callsign', 'adep', 'name_adep', 'country_code_adep', 'ades', 'name_ades', 'country_code_ades', 'actual_offblock_time', 'arrival_time', 'aircraft_type', 'wtc', 'airline', 'flight_duration', 'taxiout_time', 'flown_distance', 'tow']
(158149, 18)
unique ADEPs  =     airport
0      LTFJ
1      EBBR
2      KMIA
3      LSZH
4      EGCN
..      ...
415    EFET
416    LFBH
417    DIAP
418    VTSG
419    EFRO

[420 rows x 1 columns]
unique ADESs  =     airport
0      LTFJ
1      EBBR
2      KMIA
3      LSZH
4      EGCN
..      ...
415    EFET
416    LFBH
417    DIAP
418    VTSG
419    EFRO

[420 rows x 1 columns]
    airport
0      LTFJ
1      EBBR
2      KMIA
3      LSZH
4      EGCN
..      ...
782    FAOR
783    OPLA
784    EFRO
785    OKBK
786    OMSJ

[787 rows x 1 columns]
 ------------ all unique airports -----------
(1614, 1)
['airport']
(499, 1)
['airport']
all airports Adep and Ades of the challenge set and the final submission set are in the Airports database

rober@RobertPastor MINGW64 ~/git/AnsPRCDataChallenge (master)
