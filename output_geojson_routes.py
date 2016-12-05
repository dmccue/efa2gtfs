#!/usr/local/bin/python
import sys, csv, random, sqlite3, geojson, json

# Main
db = sqlite3.connect('data/db.db')
db.row_factory = sqlite3.Row
cur = db.cursor()
cur2 = db.cursor()
cur3 = db.cursor()


features = []
cur.execute("select route_id from route")
for i in cur:
    cur2.execute("select route_seq from route_path where route_id = '" + str(i[0]) + "'")
    rowresult = cur2.fetchone()
    if rowresult is None: continue
    obj_feature = geojson.Feature()
    obj_feature.properties['title'] = str(i[0])
    #obj_feature.properties['icon'] = 'crosshair'
    obj_point = geojson.MultiPoint()
    obj_point.coordinates = []
    for k in rowresult[0].split(','):
        cur3.execute("select stop_lat, stop_lon from stop where stop_id = " + k)
        stoploc = cur3.fetchone()
        if stoploc is None: stoploc = [0,0]
        obj_point.coordinates.append((stoploc[1], stoploc[0]))
    obj_feature.geometry = obj_point
    features.append(obj_feature)
obj_featurecollection = geojson.FeatureCollection(features)

cur.close()
cur2.close()
cur3.close()
db.close()
#print output
print json.dumps(obj_featurecollection, indent=4, sort_keys=True)
