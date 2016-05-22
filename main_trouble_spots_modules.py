import time

from seattle_crime_api import get_event_geoloc_lst_by_date_range
from Crime_Map_visualization import get_trouble_spot_map

def show_police_activity_seattle_map(date_range):
    location_results = get_event_geoloc_lst_by_date_range(date_range)
    map = get_trouble_spot_map(location_results[0:10])
    return map

input_start_time = raw_input('please provide start date (YYYY-MM-DD) >')
input_end_time = raw_input('please provide end date (YYYY-MM-DD) >')

try:
    start_time = time.strptime(input_start_time, '%Y-%m-%d')
    end_time = time.strptime(input_end_time, '%Y-%m-%d')
    if start_time > end_time:
        raise ValueError('start date cannot be greater than end date.')
    date_range = (start_time, end_time)
    location_results = show_police_activity_seattle_map(date_range)
    print location_results
except ValueError, error:
    print error.message



"""
example = [(47.660386558, -122.319777301, u'PROWLER'), (47.600012883, -122.317233402, u'CRISIS COMPLAINT - GENERAL'), (47.722957797, -122.304586201, u'SUSPICIOUS PERSON'), (47.600032635, -122.327664932, u'NOISE DISTURBANCE')]
blah = get_trouble_spot_map(example)
print blahs
"""

#write raw input
#call all required functions using pattern above
#Test
