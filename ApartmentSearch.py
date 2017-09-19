	
from craigslist import CraigslistHousing
from rtree import index

cl_h = CraigslistHousing(site='losangeles', area='sgv', category='apa',
                         filters={'max_price': 1300, 'zip_code': 91106, 'search_distance': 10, 'max_bedrooms': 1})

#for result in cl_h.get_results(sort_by='newest', geotagged=True):
#    print (result['geotag'])

result = {'id': '6301716374', 'name': 'Beautiful and spacious 1bd in central area', 'url': 'https://losangeles.craigslist.org/sgv/apa/d/beautiful-and-spacious-1bd-in/6301716374.html', 'datetime': '2017-09-11 10:28', 'price': '$1795', 'where': '85 N Holliston Ave. Pasadena', 'has_image': True, 'has_map': True, 'geotag': (34.147648, -118.123046), 'bedrooms': '1', 'area': None}

idx = index.Index()

idx.insert(1, (34.113318, -118.071612, 34.112352, -118.073473))

print(result['geotag'])
print(location)



