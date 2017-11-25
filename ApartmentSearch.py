	
from craigslist import CraigslistHousing
from rtree import index

#Creating Index
idx = index.Index()

#Adding Giant Box to index
idx.insert(1, (-118.156726, 34.083989, -117.950682, 34.211280))

cl_h = CraigslistHousing(site='losangeles', area='sgv', category='apa',
                         filters={'max_price': 1300, 'zip_code': 91106, 'search_distance': 10, 'max_bedrooms': 1})

for result in cl_h.get_results(sort_by='newest', geotagged=True):
    try:
        location = result['geotag']
        latitude = location[0]
        #print(latitude)
        longitude = location[1]
        #print(longitude)
    except:
        continue

    query = list(idx.intersection((longitude, latitude, longitude, latitude)))
    print(query)
    if not query:
        print("Outside Search Area")
    else:
        print(result['geotag'])
    
