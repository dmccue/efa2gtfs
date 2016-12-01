#!/usr/local/bin/python
import sys, csv, random, sqlite3

from lxml import etree
from pykml.factory import KML_ElementMaker as KML
from pykml.factory import ATOM_ElementMaker as ATOM
from pykml.factory import GX_ElementMaker as GX


# Create kml doc tree
kmldoc = KML.Document(KML.name('Translink'))

# Create colors
COLOR_VARIATIONS=40
for i in range(1,COLOR_VARIATIONS):
    color_val = "#%06xFF" % random.randint(0, 0xFFFFFF)
    kmldoc.append(KML.Style(KML.LineStyle(KML.color(color_val), KML.width(3)),id="linecolor"+str(i)))

# Alter default icon for placemark, labelsize
kmldoc.append(KML.Style(
                KML.IconStyle(KML.scale(0.2),KML.Icon(KML.href("http://dagik.org/kml_intro/E/ball.png"))),
                KML.LabelStyle(KML.scale(0.45)),
                id="pushpin"))


# Main
db = sqlite3.connect('data/db.db')
db.row_factory = sqlite3.Row
cur = db.cursor()
cur2 = db.cursor()

cur.execute("select * from stop")
for i in cur:
    point = KML.Placemark(
        KML.name(str(int(i['stop_id'])-10000000)),
        KML.description(i['stop_name']),
        KML.styleUrl("#pushpin"),
        KML.Point(KML.coordinates(str(i['stop_lon']) + ',' + str(i['stop_lat']) + ',10'))
    )
    kmldoc.append(point)


cur.execute("select * from route_path")
for i in cur:
    coordinates = []
    for stop_id in i['route_seq'].split(","):
        cur2.execute("""select * from stop where stop_id = ?""", (stop_id,))
        row = cur2.fetchone()
        coordinates.append([row['stop_lon'],row['stop_lat'],0])

    snapUrl = "https://roads.googleapis.com/v1/snapToRoads?interpolate=true&key=AIzaSyADYWIGFSnn3DHlJblK0hntz5KQiwbD0hk&path="
    pathstring = ""
    for item in coordinates:
        pathstring = pathstring + str(item[1]) + '%2C' + str(item[0]) + '%7C'
    print snapUrl + pathstring.rstrip('%7C') + '-' +str(i['route_id'])
    #print()
    #print ""

    color_id = random.randint(1, COLOR_VARIATIONS)
    placemark = KML.Placemark(
        KML.name(i['route_id']),
        KML.styleUrl("#linecolor" + str(color_id)),
        KML.LineString(
            KML.coordinates(
                ' '.join([str(item).strip('[]').replace(' ', '') for item in coordinates])
            )
        )
    )
    kmldoc.append(placemark)

sys.exit(1)
#print etree.tostring(etree.ElementTree(KML.kml(kmldoc)), pretty_print=True)








# stops = {}
# with open("GTFS/stops.txt", "rb") as f:
#     lines = csv.reader(f, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
#     for line in lines:
#         if 'stop_id' in line[0]: continue
#         stop_id = line[0]
#         stop_lat = float(line[3])
#         stop_lon = float(line[4])
#         stops[stop_id] = [stop_lat,stop_lon]
#         #mymap.addpoint(stop_lat, stop_lon, "#FF0000")
#         point = KML.Placemark(
#             KML.name(str(int(stop_id)-10000000)),
#             KML.description(line[1]),
#             KML.styleUrl("#pushpin"),
#             KML.Point(KML.coordinates(str(stop_lon) + ',' + str(stop_lat)))
#         )
#         kmldoc.append(point)

# with open("GTFS/_paths.txt", "rb") as f:
#     lines = csv.reader(f, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
#     for line in lines:
#         path_coords = []
#         path_id = line[0]
#         path_stops = line[1].split('|')
#         #for item in path_stops: print item
#         #print path_id, len(path_stops)
#         for stop in path_stops:
#             #print stops[stop]
#             path_coords.append((stops[stop]))
#         #print path_id, path_coords
#         color_val = "#%06x" % random.randint(0, 0xFFFFFF)
#         #mymap.addpath(path_coords, color_val)
#KML.Style(KML.Style(KML.color(color_val), KML.width(5))),
#color_val = "%06xff" % random.randint(0, 0xFFFFFF)
