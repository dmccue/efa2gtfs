#!/usr/bin/python

import xml.etree.ElementTree as ET
import requests

import pygmaps
mymap = pygmaps.maps(54.5825668303, -5.93652799127, 14)
mymap.setgrids(54.59, 54.58, 0.001, -5.94, -5.93, 0.001)
#mymap.addpoint(37.427, -122.145, "#0000FF")
#mymap.addradpoint(37.429, -122.145, 95, "#FF0000")
#path = [(37.429, -122.145),(37.428, -122.145),(37.427, -122.145),(37.427, -122.146),(37.427, -122.146)]
#mymap.addpath(path,"#00FF00")




DEBUG = 0
#ITMR
payload = {
    'language': 'en',
    'coordOutputFormat': 'WGS84',
    'locationServerActive': '1',
    'stateless': '1',
    'type_sf': 'any',
    'name_sf': 'stranmillis'
}
response = requests.get('http://journeyplanner.translink.co.uk/android/XML_STOPFINDER_REQUEST', params=payload).text

root = ET.fromstring(response)

for child in root.iter('p'):
  if DEBUG: print ET.dump(child)
  rec_name = child[0].text
  rec_uuu = child[1].text
  rec_type = child[2].text
  rec_id = child[3][0].text
  rec_stateless = child[3][1].text
  rec_omc = child[3][2].text
  rec_pc = child[3][3].text
  rec_pid = child[3][4].text
  rec_c = child[3][5].text

  #Format location
  (lon,lat) = rec_c.split(',')
  lat = float(lat) / 1000000.0
  lon = float(lon) / 1000000.0
  mymap.addpoint(lat, lon, "#FF0000")

  rec_qal = child[4].text
  print rec_name+':'+rec_uuu+':'+rec_type+':'+rec_id+':'+rec_stateless+':'+rec_omc+':'+rec_pc+':'+rec_pid+':'+rec_c+':'+rec_qal
  print "lat,lon: " + str(lat) + ' ' + str(lon)


mymap.draw('./mymap.draw.html')


#http://journeyplanner.translink.co.uk/android/XML_TRIP_REQUEST2?
# language=en&
# calcNumberOfTrips=2&
# coordListOutputFormat=STRING&
# coordOutputFormat=ITMR&
# coordOutputFormatTail=0&
# useRealtime=1&
# locationServerActive=1&
# itdTime=0906&
# itdDate=20151002&
# name_origin=10001090&
# type_origin=any&
# name_destination=suburbID%3A31400030%3A240%3ABelfast+City+Centre%3A733755%3A125990%3AITMR&
# type_destination=any&
# excludedMeans=checkbox&
# itOptionsActive=1&
# changeSpeed=normal&
# routeType=LEASTINTERCHANGE&
# imparedOptionsActive=1&
# noAlt=1&
# googleAnalytics=false&
# useProxFootSearch=true&
# calcMonoTrip=0&
# calcMonoPTTrip=0&
# trITMOTvalue100=15&
# calcOneDirection=1&
# appCache=true&
# ptOptionsActive=1&
# snapHouseNum=1

# http://journeyplanner.translink.co.uk/android/XML_STOPFINDER_REQUEST?
# language=en&
# coordOutputFormat=ITMR&
# locationServerActive=1&
# stateless=1&
# name_sf=castlereagh&
# type_sf=any&
