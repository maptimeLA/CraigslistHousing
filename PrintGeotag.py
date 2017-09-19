from craigslist import CraigslistHousing

cl_h = CraigslistHousing(site='losangeles', area='sgv', category='apa',
                         filters={'max_price': 13000, 'zip_code': 91106, 'search_distance': 1, 'max_bedrooms': 1})

for result in cl_h.get_results(sort_by='newest', geotagged=True):
    print (result)
