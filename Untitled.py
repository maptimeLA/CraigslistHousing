from craigslist import CraigslistHousing

clh = CraigslistHousing(site='losangeles', area='sgv', category='apa', filters={'max_price' : 1350})

for result in clh:
    print result

    
