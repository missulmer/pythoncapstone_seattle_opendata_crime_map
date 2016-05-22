import json
import sqlite3
import time
import calendar
import sys

#data_file = raw_input("enter file name:")
if len(sys.argv) > 1:
    data_file = sys.argv[1]
    print 'Read file from arguments: {}'.format(data_file)
else:
    data_file = '/Users/lulmer/Pythonstudy/py4e/spd_data/spd_data_pg_0.json'

print 'Reading JSON file: {}'.format(data_file)
with open(data_file, "r") as my_file:
    cont_data = json.load(my_file)

conn = sqlite3.connect('spddata.sqlite')
cur = conn.cursor()

print 'Creating a hole in space time'
cur.execute('''
CREATE TABLE IF NOT EXISTS trouble_spots (event_clearance_description TEXT, event_clearance_date NUMERIC, latitude REAL, longitude REAL)
''')

#contains all the data parsed from the Json that will be put in the db.

trim_trouble = []

print 'Trimming your goods for later show & tell'
for entry in cont_data:
    actual_trbl = {}
    if 'event_clearance_description' in entry and 'event_clearance_date'in entry and 'latitude' in entry and 'longitude' in entry:
        actual_trbl['event_clearance_description'] = entry['event_clearance_description']
        str_time = entry['event_clearance_date'].split('.')[0] # example time 2012-12-23T13:59:00.000
        #Time is stored as Epoch
        time_gm = time.strptime(str_time, '%Y-%m-%dT%H:%M:%S') #https://docs.python.org/2/library/time.html#time.strptime
        actual_trbl['event_clearance_date'] = calendar.timegm(time_gm) #converts time to Epoch (long)
        actual_trbl['latitude'] = float(entry['latitude'])
        actual_trbl['longitude'] = float(entry['longitude'])
        trim_trouble.append(actual_trbl)

print 'Inserting you know where'
#insert into data base
for trouble in trim_trouble:

    cur.execute('''
        INSERT INTO trouble_spots
            (event_clearance_description, event_clearance_date, latitude, longitude)
            VALUES ( ?, ?, ?, ? )''',
            (
                trouble['event_clearance_description'],
                trouble['event_clearance_date'],
                trouble['latitude'],
                trouble['longitude']
            )
        )
    conn.commit()
conn.close()
print 'Now I am done, so good, oh yeah!'
