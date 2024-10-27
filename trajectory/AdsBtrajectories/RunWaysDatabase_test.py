'''
Created on 26 oct. 2024

@author: rober
'''

'''
Created on 21 déc. 2020

@author: rober
'''

import time
import unittest

from Airports.AirportDatabaseFile  import AirportsDatabase
from Runways.RunWaysDatabaseFile import RunWayDataBase


class Test_Main(unittest.TestCase):

    def test_main_one(self):
    
        print ( '==================== run-ways====================' )
        t0 = time.time()
    
        runWaysDatabase = RunWayDataBase()
        if runWaysDatabase.read():
            print ( 'runways DB correctly read' )
        
        t1 = time.time()
        print ( 'time spent= {0:.2f} seconds'.format(t1-t0) )
        
        print ( '==================== run-ways find airport ====================' )
    
        print ( runWaysDatabase.findAirportRunWays('LFPG') )
        t2 = time.time()
        print ('time spent= {0:.2f} seconds'.format(t2-t1) )
        
    
        print ( '==================== run-ways get filtered run ways====================' )
        print ( runWaysDatabase.getFilteredRunWays('LFML') )
        
        print ( '==================== run-ways get filtered run ways====================' )
        print ( runWaysDatabase.getFilteredRunWays('LFBO') )
        
        print ( '==================== run-ways get filtered run ways====================' )
        print ( runWaysDatabase.findAirportRunWays('LFBO') )
        
        
        print ( '==================== run-ways get filtered run ways====================' )
        runway = runWaysDatabase.getFilteredRunWays('EGLL') 
        print ( runway )
        
        print ( '====================r un-ways get filtered run ways====================' )
        #print 'number of runways: ' + str(len(runWaysDatabase.getRunWays('LFPG')))
        runway = runWaysDatabase.getFilteredRunWays(airportICAOcode = 'LFPG', runwayName  = '27L')
        print ( runway )
        
        print ( '==================== run-ways get filtered run ways====================' )
        runway = runWaysDatabase.getFilteredRunWays(airportICAOcode = 'KJFK', runwayName  = '31L')
        print ( runway )
        
        print ( '==================== run-ways get filtered run ways====================' )
    
        runway = runWaysDatabase.getFilteredRunWays(airportICAOcode = 'KLAX', runwayName  = '06L')
        print ( runway )
        
        for ICAOcode in ['LFPG', 'LFPO', 'LFBO', 'LFML', 'LFST', 'KJFK', 'SBGL', 'LFBD']:
            
            print ( '====================run-ways get filtered run ways====================' )
    
            tStart = time.time()
            print ( runWaysDatabase.findAirportRunWays(ICAOcode) )
            tEnd = time.time()
            print ( 'icao= {0} - duration= {1:.2f} seconds'.format(ICAOcode, (tEnd-tStart)) )
    #     print '====================run-ways===================='
    #     for runway in runWaysDatabase.getRunWays():
    #         print runway.getAirportICAOcode() + '-' + runway.getName()
            
        print ( '====================run-ways====================' )
    #     for runway in runWaysDatabase.getRunWays():
    #         print runway
    
        print ( '====================run-ways get filtered run ways====================' )
    
        print ( runWaysDatabase.findAirportRunWays('LPPT') )
    
    
    def test_main_two(self):
        
        print ( '==================== run-ways test two ====================' )

        runWaysDatabase = RunWayDataBase()
        self.assertTrue( runWaysDatabase.read() )
            
        airportICAOcode = 'LPPT'
        self.assertTrue ( runWaysDatabase.hasRunWays(airportICAOcode) )
        
    def test_main_three(self):
        
        print ( '==================== run-ways test three ====================' )

        runWaysDatabase = RunWayDataBase()
        self.assertTrue( runWaysDatabase.read() )
        
        airportICAOcode = 'LFPG'
        for runway in runWaysDatabase.getRunWaysAsDict(airportICAOcode) :
            print ( runway )

    def test_main_four(self):

        print ( '==================== run-ways test four ====================' )
    
        runWaysDatabase = RunWayDataBase()
        self.assertTrue( runWaysDatabase.read() )
        
        airportICAOcode = 'LFPG'
        for runway in runWaysDatabase.getRunWays(airportICAOcode) :
            print ( runway )
            
            
    def test_main_five(self):
        
        print ( '==================== run-ways test five ====================' )

        airportsDb = AirportsDatabase()
        self.assertTrue (airportsDb.read())
        
        CharlesDeGaulleRoissy = airportsDb.getAirportFromICAOCode('LFPG')
        print ( CharlesDeGaulleRoissy )
        
        runWaysDatabase = RunWayDataBase()
        self.assertTrue( runWaysDatabase.read() )
        
        airportICAOcode = 'LFPG'
        runwayName = "08L"
        runway = runWaysDatabase.getFilteredRunWays(airportICAOcode = airportICAOcode, runwayName  = runwayName)
        print ( runway )
        
        latitudeDegrees , longitudeDegrees = runway.getGeoPointAtDistanceHeading(runway.getLengthMeters(), runway.getTrueHeadingDegrees())
        
    def test_main_six(self):
        
        print ( '==================== run-ways test six ====================' )
        
        runWaysDatabase = RunWayDataBase()
        self.assertTrue( runWaysDatabase.read() )
        
        airportICAOcode = 'LFPG'
        print ("number of runways = {0}".format(runWaysDatabase.getNumberOfRunways(airportICAOcode)))
        
        airportICAOcode = "XXXX"
        print ("number of runways = {0}".format(runWaysDatabase.getNumberOfRunways(airportICAOcode)))

if __name__ == '__main__':
    unittest.main()