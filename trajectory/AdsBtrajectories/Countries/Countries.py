
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
        if str(twoCharactersCountryCode).upper() in list(self.df['alpha-2']):
            filtered_df = self.df[self.df['alpha-2'] ==  str(twoCharactersCountryCode).upper() ]
            #print(filtered_df['alpha-2'].iloc[0])
            return True
        return False
    

    def getCountryRegion(self, twoCharactersCountryCode):
        if str(twoCharactersCountryCode).upper() in list(self.df['alpha-2']):
            filtered_df = self.df[self.df['alpha-2'] ==  str(twoCharactersCountryCode).upper() ]
            print(filtered_df)
            return filtered_df['region'].iloc[0]  
        return ""


    def isDomestic( self, adepCountryCode, adesCountryCode , region):
        adepRegion = "Europe"
        if str(adepCountryCode).upper() in list(self.df['alpha-2']):
            filtered_df = self.df[self.df['alpha-2'] ==  str(adepCountryCode).upper() ]
            print(filtered_df)
            adepRegion = filtered_df['region'].iloc[0] 
        if str(adesCountryCode).upper() in list(self.df['alpha-2']):
            filtered_df = self.df[self.df['alpha-2'] ==  str(adesCountryCode).upper() ]
            print(filtered_df)
            adesRegion = filtered_df['region'].iloc[0]
        if adepRegion == region and adesRegion == region:
            return True
        else:
            return False
        


if __name__ == '__main__':

    countries = Country()
    ret = countries.read()

    print("-"*80)
    print ("Countries read correctly = {0}".format(ret))

    print("-"*80)

    ret = countries.isCountryExisting("FR")
    print("Country is existing = {0}".format(ret))

    print("-"*80)

    ret = countries.isCountryExisting("Fr")
    print("Country is existing = {0}".format(ret))

    print("-"*80)

    countryCode = "FR"
    region = countries.getCountryRegion(countryCode)
    print( type ( region ))
    print("{0} in region -> {1}".format( countryCode, region))

    print("-"*80)

    countryCode = "fr"
    region = countries.getCountryRegion(countryCode)
    print( type ( region ))
    print("{0} in region -> {1}".format( countryCode, region))

    print("-"*80)

    ret = countries.isDomestic( "FR" , "DE" , "Europe")
    print("{0} - {1} are both in region {2} -> results -> {3}".format("FR","DE", "Europe" , ret))

    ret = countries.isDomestic( "FR" , "US" , "Europe")
    print("{0} - {1} are both in region {2} -> results -> {3}".format("FR","US", "Europe" , ret))