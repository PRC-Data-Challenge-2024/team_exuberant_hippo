## dependencies
openap -> used to get aircrafts characteristics


## to improve the performance a set of CSV files are computed before hand


## pre requesite

download all the 2022 parquet files in the AnsPerformanceChallenge folder

## to improve performances, all 2023 parquet files are read one by one and analysed
## only the flights ids found in the challengeSet and in the final submission set are considered

execute "extendOpenSkyParquet.py" file to analyse all the parquet files and generate a final parquet file with only the flight_ids from the challenge and the submission set

