## dependencies
openap -> used to get aircrafts characteristics


## to improve the performance a set of CSV files are computed before hand


## pre requesite

download all the 2022 parquet files in the AnsPerformanceChallenge folder

## to improve performances, all 2023 parquet files are read one by one and analysed
## only the flights ids found in the challengeSet and in the final submission set are considered

execute "extendOpenSkyParquet.py" file to analyse all the parquet files and generate a final parquet file with only the flight_ids from the challenge and the submission set

execute "extendChallengeSetAircrafts.py" should produce "extendedAircrafts.csv" in the "Results" folder
execute "extendChallengeSetAirports.py" should produce "extendedAirports.csv" in the "Results" folder
execute "extendChallengeSetRunways.py" should produce ""extendedAirportsRunways.csv" in the "Results" folder

execute "RunWaysDatabase_test.py" in order to check access to the Runways database located in Runways folder

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
