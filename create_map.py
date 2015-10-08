#!/usr/bin/python

import pygmaps, sys

if len(sys.argv) < 2:
    print "Please provide a file to read from as arg1"
    sys.exit(1)

mymap = pygmaps.maps(54.5825668303, -5.93652799127, 14)
#mymap.setgrids(54.59, 54.58, 0.001, -5.94, -5.93, 0.001)
#mymap.addpoint(37.427, -122.145, "#0000FF")
#mymap.addradpoint(37.429, -122.145, 95, "#FF0000")
#path = [(37.429, -122.145),(37.428, -122.145),(37.427, -122.145),(37.427, -122.146),(37.427, -122.146)]
#mymap.addpath(path,"#00FF00")

with open(sys.argv[1], "r") as f:
    for line in f:
        items = line.rstrip().split(':')
        print str(items)
        mymap.addpoint(float(items[2]), float(items[3]), "#FF0000")

mymap.draw('./mymap.draw.html')
