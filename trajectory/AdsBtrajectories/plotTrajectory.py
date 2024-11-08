'''
Created on 24 oct. 2024

@author: robert
'''

import os
import warnings
from tqdm import TqdmExperimentalWarning

warnings.filterwarnings("ignore", category=TqdmExperimentalWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
import matplotlib.pyplot as plt
from traffic.core import Traffic

def plotTrajectory():
    current_dir = os.getcwd()
    fileName = "2022-01-01.parquet"

    filePath = os.path.join( os.path.dirname(__file__) ,  "AnsPerformanceChallenge" ,'competition-data' , fileName)

    print ( filePath )
    traj = (Traffic.from_file(filePath)
            # smooth vertical glitches
            .filter()
            # resample at 1s
            .resample('1s')
            # execute all
            .eval()
            )
    print ( traj )
    flight_id = "248763780"
    flight_id = "248763775" # 7 minutes between Top of climb and top of descent
    flight_id = "248753286"
    for t in traj:
        if ( t['flight_id'] == int(str(flight_id)) ):
            
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7))

            flight = t
            ''' altitude and groundspeed are keys in the dataset '''
            flight.plot_time(ax=ax1, y="altitude")
            flight.plot_time(ax=ax2, y="groundspeed")
            plt.show()
    
    
if __name__ == '__main__':
    plotTrajectory()
    print ("--- it's finished ---")