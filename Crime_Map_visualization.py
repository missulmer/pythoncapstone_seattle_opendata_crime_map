"""

https://maps.googleapis.com/maps/api/staticmap?center=Williamsburg,Brooklyn,NY&zoom=13&size=400x400&
markers=color:blue%7Clabel:S%7C11211%7C11206%7C11222&key=YOUR_API_KEY
(47.571703908, -122.33419792, u'THEFT - MISCELLANEOUS')

https://maps.googleapis.com/maps/api/staticmap?size=640x640&markers=color:blue%7Clabel:S%7C47.571703908,-122.33419792&key=AIzaSyDDuDDANt1DyLbdjGNqZCa1_K74sfQqzC8

"""

MARKER_SPEC = 'markers=color:blue%7Clabel:S'
API_KEY = 'AIzaSyDDuDDANt1DyLbdjGNqZCa1_K74sfQqzC8'
LAT_LONG_TMPL = '%7C{lat},{long}'
URL_TMPL = 'https://maps.googleapis.com/maps/api/staticmap?size=640x640&{marker}{lat_long_lst}&{key}'

def get_trouble_spot_map(trouble_spot_lst):
    """
    trouble_spot_lst = [
    (lat, long, event_clearance_description)
    ]
    return = url for google static maps
    """
    lat_long_lst = []
    for item in trouble_spot_lst:
        latitude = item[0]
        longitude = item[1]
        married_lat_long = LAT_LONG_TMPL.format(lat=latitude, long=longitude)
        lat_long_lst.append(married_lat_long)

    lat_long_lst_str = ''.join(lat_long_lst)

    result = URL_TMPL.format(key=API_KEY, marker=MARKER_SPEC, lat_long_lst=lat_long_lst_str)
    return result
