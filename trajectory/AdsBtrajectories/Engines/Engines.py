
'''
Created on 20 oct. 2024

@author: robert

'''

import sys
import os
sys.path.insert( 0 , os.path.abspath('C:/Users/rober/git/openap/'))
print (sys.path)

from openap import FuelFlow, prop
import os
import pandas as pd
from pathlib import Path

class Engines(object):
    
    inputFileName = "edb-emissions-databank_v30__web_.xlsx"
    directoryPath = ""

    dataframe = None
    sheetName = "Gaseous Emissions and Smoke"
    filePath = os.path.dirname(os.path.abspath(__file__))


    def __init__(self):
        
        self.inputFolder = os.path.dirname(os.path.abspath(__file__))
        self.directoryPath = Path(self.inputFolder)
        
        if self.directoryPath.is_dir():
            print ( "it is a directory - {0}".format(self.directoryPath))
            filePath = os.path.join(self.directoryPath, self.inputFileName)
            
            print ( filePath )

    def getFilePath(self):
        return self.filePath

    def read(self):

        if self.directoryPath.is_dir():
            self.filePath = os.path.join(self.directoryPath, self.inputFileName)
            print ( self.filePath)

            self.df_engines = pd.read_excel( self.filePath , sheet_name=self.sheetName)
            print ( self.df_engines.shape )
            print ( list ( self.df_engines ) )
            print ( self.df_engines.head() )
            
            return True
        return False

    def getListOfEngines(self):

        columnName = 'Engine Identification'
        #df_filtered = self.df_engines[[columnName]]

        df_unique = pd.DataFrame ( self.df_engines[columnName].unique())
        print ( type ( df_unique ))
        for index, row in df_unique.iterrows():
            print(index, row.iloc[0])

    def isEngineInEmissionDatabase(self, engineName):
        columnName = 'Engine Identification'
        #df_filtered = self.df_engines[[columnName]]

        df_unique = pd.DataFrame ( self.df_engines[columnName].unique())
        #print ( type ( df_unique ))
        for index, row in df_unique.iterrows():
            #print(index, row.iloc[0])
            if ( row.iloc[0] == engineName):
                return True
            else:
                if ( str(row.iloc[0]).startswith ( engineName )):
                    print ("{0} - {1}".format( str(row.iloc[0]) , engineName))
                    return True
            
        return False

    def getFuelFlowAtClimbOutKgPerSeconds(self, engineName):
        columnName = 'Engine Identification'
        columnNameOut = 'Fuel Flow C/O (kg/sec)'

        df_unique = pd.DataFrame ( self.df_engines[columnName].unique())
        #print ( type ( df_unique ))
        for index, row in df_unique.iterrows():
            #print(index, row.iloc[0])
            if ( row.iloc[0] == engineName):
                return self.df_engines[self.df_engines[columnName].isin([row.iloc[0]])][columnNameOut].iloc[0]
            else:
                if ( str(row.iloc[0]).startswith ( engineName )):
                    print ("{0} - {1}".format( str(row.iloc[0]) , engineName))
                    return self.df_engines[self.df_engines[columnName].isin([row.iloc[0]])][columnNameOut].iloc[0]
            
        return 0.0



if __name__ == '__main__':
    print ( "--- read Engines database ---")

    engines = Engines()
    df = engines.read()
    print("{0} - read correctly = {1}".format( engines.getFilePath(), df.shape ))

    engines.getListOfEngines()