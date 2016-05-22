import sqlite3
import time
import calendar

def get_event_geoloc_lst_by_date_range(date_range):
    """
    Returns a list of lat_longs with a event description within the given date range.
    Note that date_time is stored as epoch.
    date_range = (gmtime(), gmtime())
    return = [
    (lat, long, event_clearance_description)
    ]
    """
    start_date = date_range[0]
    end_date = date_range[1]
    epoch_start_date = calendar.timegm(start_date) #converts time to Epoch (long)
    epoch_end_date = calendar.timegm(end_date)
    return _query_db(epoch_start_date, epoch_end_date)

def _query_db(epoch_start_date, epoch_end_date):
    """
    return = [
    (lat, long, event_clearance_description)
    ]
    """
    conn = sqlite3.connect('spddata.sqlite')
    cur = conn.cursor()
    cur.execute('''
    SELECT latitude, longitude, event_clearance_description
        FROM trouble_spots
        WHERE event_clearance_date
            BETWEEN ?
            AND ?
    ''', (epoch_start_date, epoch_end_date))
    date_range_fetched_results = []
    for row in cur:
        latitude = row[0]
        longitude = row[1]
        event_clearance_description = row[2]
        entry = (latitude, longitude, event_clearance_description)
        date_range_fetched_results.append(entry)

    return date_range_fetched_results


