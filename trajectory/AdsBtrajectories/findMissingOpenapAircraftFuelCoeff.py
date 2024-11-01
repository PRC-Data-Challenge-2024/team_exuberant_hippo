

import sys
import os
sys.path.insert( 0 , os.path.abspath('C:/Users/rober/git/openap/'))
print (sys.path)

from openap import FuelFlow, prop
import pandas as pd
import math

from utils import computeChallengeSubmission, readExtendedAircrafts, readExtendedAirports
from utils import readAircraftOpenapData
from Environment.Constants import Meter2Feet
from pathlib import Path


if __name__ == '__main__':

    df = computeChallengeSubmission()
    print ( df.shape )
    print ( list ( df ))


    df_unique_aircrafts = pd.DataFrame ( df['aircraft_type'].unique() , columns= ['aircraft_type'])
    print ( df_unique_aircrafts.shape )
    print ( list ( df_unique_aircrafts ))
        
    count = 0
    for aircraft_type in df_unique_aircrafts['aircraft_type']:
        print ( aircraft_type )
        try:
            fuelflow = FuelFlow(ac=str(aircraft_type).lower() , eng=None )
        except:
            print("-"*80)
            print(" no fuel data for aircraft {0} in openap ".format(aircraft_type))
