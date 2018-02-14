result = {'id': '6485987159', 'name': 'Cozy 1 Bdr 1 Bth Apt', 'url': 'https://losangeles.craigslist.org/sgv/apa/d/cozy-1-bdr-1-bth-apt/6485987159.html', 'datetime': '2018-02-05 16:39', 'price': '$1300', 'where': '300 N Holliston Ave', 'has_image': True, 'has_map': True, 'geotag': (34.150845, -118.122811), 'bedrooms': '1', 'area': '600ft2'}

template = { "type": "Feature", "properties": { "id": result["id"], "name": result["name"], "url": result["url"], "datetime": result["datetime"], "price": result["price"] , "where": result["where"], "bedrooms": result['bedrooms'], "area": result['area'], "LAT": result['geotag'][0], "LONG": result['geotag'][1], "geometry": { "type": "Point", "coordinates": [ result['geotag'][1], result['geotag'][0] ] } }

print(template)
             
