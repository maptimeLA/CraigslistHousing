	
from craigslist import CraigslistHousing
from rtree import index

cl_h = CraigslistHousing(site='losangeles', area='sgv', category='apa',
                         filters={'max_price': 1300, 'zip_code': 91106, 'search_distance': 10, 'max_bedrooms': 1})

#for result in cl_h.get_results(sort_by='newest', geotagged=True):
#    print (result['geotag'])

idx = index.Index()

idx.insert(1, (34.113318, -118.071612, 34.112352, -118.073473)

for result in cl_h.get_results(sort_by='newest', geotagged=True):
    test = list(idx.intersection(result['geotag']))
        if 1 in test:
            print(result['name'])

