#seattle_crime_api
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
#instead of calling sqlite, I am going to call the api.  Find the filters, key all that jazz
#may need to translate out of epoch to whatever the api wants