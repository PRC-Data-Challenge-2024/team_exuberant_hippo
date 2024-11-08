import pandas as pd

import sys
import os
sys.path.insert( 0 , os.path.abspath('C:/Users/rober/git/openap/'))
print (sys.path)

from openap import FuelFlow, prop, FlightPhase

from utils import readParquet
from datetime import date



if __name__ == '__main__':
    pass
    fileName = "2022-01-01.parquet"
    df  = readParquet(fileName)

    unique_flight_ids = df['flight_id'].unique()
    print("unique flight ids  = {0}".format((unique_flight_ids)))
    print("number of unique flight ids = {0}".format(len(unique_flight_ids)))

    for flight_id in unique_flight_ids:
        
        #print ( flight_id )
        #print (  )
        if ( flight_id != int("248753286")):
            continue

        print ( flight_id )
        df_filtered = df[df['flight_id'] == flight_id]
        df_filtered = df_filtered.reset_index()

        ts = (df_filtered.timestamp - df_filtered.timestamp.iloc[0]).dt.total_seconds()  # second
        alt = df_filtered.altitude.values  # ft
        spd = df_filtered.groundspeed.values  # kts
        roc = df_filtered.vertical_rate.values  # ft/min

        fp = FlightPhase()
        fp.set_trajectory(ts, alt, spd, roc)

        labels = fp.phaselabel()
        #print(labels)

        '''
        GND: on-ground  
        CL:  climb
        DE:  descend
        LVL: level flight
        CR:  cruise
        NA:  unlabeled
        ''' 
        phase_duration_in_seconds = {}
        for phase in ['GND','CL','DE','LVL','CR']:
            phase_duration_in_seconds[phase] = len(list(filter(lambda x: x == phase, labels)))

        print(phase_duration_in_seconds)
        print ( "-"*80)
