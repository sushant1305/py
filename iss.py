import ISS_Info
from datetime import datetime
import csv

def get_data():
    iss_details = dict(ISS_Info.iss_current_loc())
    latitude = iss_details['iss_position']['latitude']
    longitude = iss_details['iss_position']['longitude']
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    write_csv(dt_string,latitude,longitude)

def write_csv(dt_string,latitude,longitude):
    outputFile = open('output.csv', 'a', newline='')
    outputWriter = csv.writer(outputFile)
    outputWriter.writerow([dt_string,latitude,longitude])
    outputFile.close()
get_data()