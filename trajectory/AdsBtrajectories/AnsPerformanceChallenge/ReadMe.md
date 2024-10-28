## how to download the parquet files

## et the current dir into AnsPRCDataChallenge\trajectory\AdsBtrajectories\AnsPerformanceChallenge

open command lines window -> not a power shell -> only a cmd

Microsoft Windows [version 10.0.22631.4317]
(c) Microsoft Corporation. Tous droits réservés.

C:\Users\rober>

## launch following commands minio commands

mc.exe alias set dc24   https://s3.opensky-network.org/   ACCESS_KEY SECRET_KEY

## download parquet files

mc.exe cp --recursive dc24/competition-data/  .

this will create a subfolder called competition-data and download the parquet files into