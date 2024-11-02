





import os
from pathlib import Path
import pandas as pd


from utils import computeChallengeSubmission, readExtendedAirports
from Aircrafts.FAAaircraftDatabaseFile import FaaAircraftDatabase
from utils import computePotentialEnergy , computeKineticEnergy
from utils import computePotentialPower , computeKineticPower

if __name__ == '__main__':

    df = computeChallengeSubmission()
    print ( df.shape )
    print ( list ( df ))

    unique_countries_adep = df['country_code_adep'].unique()
    print ( type (unique_countries_adep ))
    print ( unique_countries_adep )


    unique_countries_ades = df['country_code_ades'].unique()
    print ( type ( unique_countries_ades ))
    print ( unique_countries_ades )