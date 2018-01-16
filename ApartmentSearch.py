##Resources
##https://www.dataquest.io/blog/apartment-finding-slackbot/
##https://opensource.com/article/17/10/set-postgres-database-your-raspberry-pi
##https://suhas.org/sqlalchemy-tutorial/
##https://stackoverflow.com/questions/15736995/how-can-i-quickly-estimate-the-distance-between-two-latitude-longitude-points


from craigslist import CraigslistHousing
import json
from math import radians, cos, sin, asin, sqrt
#from slackclient import SlackClient
import time

SLACK_TOKEN = "SlackTokenHere"
SLACK_CHANNEL = "#craigslist"

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

# Function to search features in the GeoJson and return the nearest
def findNearest(data, lat, lon):
    nearStation = []
    nearDist = []
    for feature in data['features']:
        point = feature['geometry']['coordinates']
        latitude = point[1]
        longitude = point[0]
        station = feature['properties']['STATION']
        #calculate distance between apartment and station
        dist = coord_distance(lon, lat, longitude, latitude)
        if len(nearDist) == 0:
            nearDist.insert(0, dist)
            nearStation.insert(0, station)
        elif dist < nearDist[0]:
            nearDist[0] = dist
            nearStation[0] = station
    result = [nearStation[0], nearDist[0]]
    return result
        

with open('GoldLineStations.geojson') as f:
    data = json.load(f)

cl_h = CraigslistHousing(site='losangeles', area='sgv', category='apa',
                         filters={'max_price': 1500, 'min_price': 1000, 'min_bedrooms':1, 'max_bedrooms': 1})

#sc = SlackClient(SLACK_TOKEN)
var = 1
posted = []
while var == 1:
    for result in cl_h.get_results(sort_by='newest', geotagged=True):
        try:
            location = result['geotag']
            latitude = location[0]
            longitude = location[1]
            #print(str(latitude) + ', ' + str(longitude))
        except:
            continue

        closestStation = findNearest(data, latitude, longitude)
        closestStationName = closestStation[0]
        print(closestStation)
        closestStationDist = float(closestStation[1])
        print(closestStationDist)
        
        if float(closestStationDist) > 0.5:
            continue
            #print("Outside Search Area")
        else:
            if result['id'] in posted:
                continue
            else:
                print(result['geotag'])
                print(result['url'])
                print('Only ' + str(closestStationDist) + 'mi from ' + closestStationName)
                desc = "{0} | {1} mi from {2} | {3} | <{4}>".format(result["price"], str(closestStationDist), closestStationName, result["name"], result["url"])
                #sc.api_call(
                #"chat.postMessage", channel=SLACK_CHANNEL, text=desc,
                #username='pybot', icon_emoji=':robot_face:'
                #)
                posted.append(result['id'])
    print("Pausing for 5min")
    print(posted)
    time.sleep(300)
