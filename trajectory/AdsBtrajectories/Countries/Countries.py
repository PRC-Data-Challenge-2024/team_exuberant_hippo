
import os
import pandas as pd
from pathlib import Path

class Country(object):

    df = None

    def __init__(self):
        
        self.className = self.__class__.__name__
        self.fileName = "Countries.csv"

        self.delimiter = ","
        self.filePath = os.path.dirname(__file__)
        directoryPath = os.path.dirname(__file__)

        directory = Path(directoryPath)
        if directory.is_dir():
            print ( "it is a directory - {0}".format(directoryPath))
            self.filePath = os.path.join(directory, self.fileName)
            print ( self.filePath )
 
    def read(self):
        self.filePath = Path(self.filePath)
        if self.filePath.is_file():
            print ("{0} is a file".format(self.filePath))
            self.df = pd.read_csv( self.filePath , sep = self.delimiter)
            print ( list ( self.df ) )
            for countryCode in self.df['alpha-2']:
                pass
                #print ( countryCode)
            return True
        return False


    def isCountryExisting(self, twoCharactersCountryCode):
        if twoCharactersCountryCode in list(self.df['alpha-2']):
            filtered_df = self.df[self.df['alpha-2'] ==  twoCharactersCountryCode ]
            print(filtered_df)
            return True
        return False
    
    def getCountryRegion(self, twoCharactersCountryCode):
        if twoCharactersCountryCode in list(self.df['alpha-2']):
            filtered_df = self.df[self.df['alpha-2'] ==  twoCharactersCountryCode ]
            print(filtered_df)
            return filtered_df['region'].iloc[0]  
        return ""


if __name__ == '__main__':

    countries = Country()
    ret = countries.read()

    print ("Countries read correctly = {0}".format(ret))

    ret = countries.isCountryExisting("FR")
    print("Country is existing = {0}".format(ret))

    countryCode = "FR"
    region = countries.getCountryRegion(countryCode)
    print( type ( region ))
    print("{0} in region -> {1}".format( countryCode, region))