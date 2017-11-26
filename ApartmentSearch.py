	
##Resource https://www.dataquest.io/blog/apartment-finding-slackbot/
##Resource https://suhas.org/sqlalchemy-tutorial/


from craigslist import CraigslistHousing
from rtree import index
import json

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
                         filters={'max_price': 1500, 'max_bedrooms': 1})

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
        print(result['url'])
        print(data['features'][query[0]]['properties']['STATION'])
    
