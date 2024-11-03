





import os
from pathlib import Path
import pandas as pd


from utils import computeChallengeSubmission, readExtendedAirports
from Aircrafts.FAAaircraftDatabaseFile import FaaAircraftDatabase
from utils import computePotentialEnergy , computeKineticEnergy
from utils import computePotentialPower , computeKineticPower

from Countries.Countries import Country

if __name__ == '__main__':

    df = computeChallengeSubmission()
    print ( df.shape )
    print ( list ( df ))

    print("-"*80)

    df_adep_countries = pd.DataFrame ( df['country_code_adep'].unique() , columns= ['country_code_adep'])
    print ( type (df_adep_countries ))
    print ( list(df_adep_countries ))

    df_adep_countries.rename(columns={'country_code_adep': 'country_code'}, inplace=True)
    print ( list (df_adep_countries))

    print("-"*80)

    df_ades_countries = pd.DataFrame ( df['country_code_ades'].unique() , columns= ['country_code_ades'])
    print ( type (df_ades_countries ))
    print ( list(df_ades_countries ))

    df_ades_countries.rename(columns={'country_code_ades': 'country_code'}, inplace=True)
    print ( list (df_ades_countries))

    print("-"*80)

    df_countries = pd.concat([df_adep_countries,df_ades_countries], ignore_index=True)
    print ( list ( df_countries))
    print ( df_countries.shape )

    #df_unique_countries = pd.DataFrame ( df_countries['airport'].unique() , columns= ['airport'])

    df_countries.drop_duplicates(subset=['country_code'], inplace=True)
    print ( list ( df_countries))
    print ( df_countries.shape )

    countries = Country()
    ret = countries.read()

    print("-"*80)
    print ("Countries read correctly = {0}".format(ret))

    for country in df_countries['country_code']:
        print ( country )
        if countries.isCountryExisting(country):
            pass
        else:
            raise ValueError("country = " + country + " not in countries database")

    

