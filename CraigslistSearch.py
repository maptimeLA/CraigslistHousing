from craigslist import CraigslistHousing

clh = CraigslistHousing(site='losangeles', area='sgv', category='apa', filters={'search_distance': 10,'zip_code': 91106 ,'posted_today' : True,'max_price' : 1500, 'laundry' : [u'w/d in unit', u'w/d hookups', u'laundry in bldg', u'laundry on site'] })

print "Searching"

for result in clh.get_results(sort_by='newest', geotagged=True):
    print result

print "Done"

    
