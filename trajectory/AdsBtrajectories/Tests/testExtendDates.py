

from utils import readSubmissionSet
from utils import extendDataSetWithDates


if __name__ == '__main__':

    print (''' ------------- read the submission dataset with empty TOW values ----''')
    fileName = "final_submission_set.csv"
    df = readSubmissionSet(fileName)
    print ( list ( df ) )
    print( df.shape )
    
    ''' extend dates in submission dataset because date format in challenge and in submission is not the same '''
    df = extendDataSetWithDates ( df )
    print ( df.shape )
    print ( list ( df ) )

    for index, row in df.iterrows():
        if ( index < 10 ):
            print("-----------")
            print(index, row['flight_id'] , row['date_year'] , row["date_month"] , row["date_week"] , row['date_week_day'], row['date_quarter'])



