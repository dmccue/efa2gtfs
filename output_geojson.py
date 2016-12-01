#!/usr/local/bin/python
import sys, csv, random, sqlite3, geojson, json

# Main
db = sqlite3.connect('data/db.db')
db.row_factory = sqlite3.Row
cur = db.cursor()
cur2 = db.cursor()

output = []
cur.execute("select * from stop")
for i in cur:
    obj_feature = geojson.Feature()
    obj_point = geojson.Point((i['stop_lon'], i['stop_lat']))
    obj_feature.geometry = obj_point
    output.append(obj_feature)

#print json.dumps(output, indent=4, sort_keys=True)
print output
