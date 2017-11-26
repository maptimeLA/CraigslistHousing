##Resources
##https://www.dataquest.io/blog/apartment-finding-slackbot/
##https://opensource.com/article/17/10/set-postgres-database-your-raspberry-pi
##https://suhas.org/sqlalchemy-tutorial/
##https://stackoverflow.com/questions/15736995/how-can-i-quickly-estimate-the-distance-between-two-latitude-longitude-points


from craigslist import CraigslistHousing
from rtree import index
import json
from math import radians, cos, sin, asin, sqrt

def coord_distance(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    # Radius of earth in kilometers is 6371
    km = 6371* c
    mi = km * 0.621371
    return mi

#Creating Index
idx = index.Index()

with open('GoldLineStations.geojson') as f:
    data = json.load(f)

#Conversion of Half Mile to Latitude and Longitude approximated for Los Angeles, CA
halfMileLat = 0.006955
halfMileLong = 0.009119
featureIndex = 0

for feature in data['features']:
    point = feature['geometry']['coordinates']
    latitude = point[1]
    longitude = point[0]
    #print(str(latitude) + ', ' + str(longitude))
    idx.insert(featureIndex, ((longitude - halfMileLong), (latitude - halfMileLat), (longitude + halfMileLong), (latitude + halfMileLat)))
    featureIndex += 1
    
print("Index Complete")


cl_h = CraigslistHousing(site='losangeles', area='sgv', category='apa',
                         filters={'max_price': 1500, 'min_price': 1000, 'min_bedrooms':1, 'max_bedrooms': 1})

for result in cl_h.get_results(sort_by='newest', geotagged=True):
    try:
        location = result['geotag']
        latitude = location[0]
        longitude = location[1]
        #print(str(latitude) + ', ' + str(longitude))
    except:
        continue

    query = list(idx.intersection((longitude, latitude, longitude, latitude)))
    #print(query)
    if not query:
        continue
        #print("Outside Search Area")
    else:
        print(result['geotag'])
        stationLat = data['features'][query[0]]['properties']['LAT']
        stationLong = data['features'][query[0]]['properties']['LONG']
        dist = coord_distance(stationLong, stationLat, result['geotag'][1], result['geotag'][0])
        print(result['url'])
        print('Only ' + str(round(dist, 2)) + 'mi from ' + data['features'][query[0]]['properties']['STATION'])
    
