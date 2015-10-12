#!/usr/bin/python

import pygmaps, sys, csv, random


mymap = pygmaps.maps(54.5825668303, -5.93652799127, 14)
#mymap.setgrids(54.59, 54.58, 0.001, -5.94, -5.93, 0.001)
#mymap.addpoint(37.427, -122.145, "#0000FF")
#mymap.addradpoint(37.429, -122.145, 95, "#FF0000")
#path = [(37.429, -122.145),(37.428, -122.145),(37.427, -122.145),(37.427, -122.146),(37.427, -122.146)]
#mymap.addpath(path,"#00FF00")

stops = {}

with open("GTFS/stops.txt", "rb") as f:
    lines = csv.reader(f, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    for line in lines:
        if 'stop_id' in line[0]: continue
        stop_id = line[0]
        stop_lat = float(line[3])
        stop_lon = float(line[4])
        stops[stop_id] = [stop_lat,stop_lon]
        mymap.addpoint(stop_lat, stop_lon, "#FF0000")

with open("GTFS/_paths.txt", "rb") as f:
    lines = csv.reader(f, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    for line in lines:
        path_coords = []
        path_id = line[0]
        path_stops = line[1].split('|')
        #for item in path_stops: print item
        #print path_id, len(path_stops)
        for stop in path_stops:
            #print stops[stop]
            path_coords.append((stops[stop]))
        #print path_id, path_coords
        color_val = "#%06x" % random.randint(0, 0xFFFFFF)
        mymap.addpath(path_coords, color_val)


mymap.draw('./mymap.draw.html')
