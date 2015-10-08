#!/usr/bin/python

import xml.etree.ElementTree as ET
import requests, sys


if len(sys.argv) < 3:
    print "Please provide a start and end id as arg1/arg2"
    sys.exit(1)

DEBUG = 0

errorcount = 0
incrementer = sys.argv[0]
while incrementer < sys.argv[1]:
  try:
    incrementer = incrementer + 1
    payload = {
        'language': 'en',
        'coordOutputFormat': 'WGS84',
        'locationServerActive': '1',
        'stateless': '1',
        'type_sf': 'any',
        'name_sf': str(incrementer)
    }
    response = requests.get('http://journeyplanner.translink.co.uk/android/XML_STOPFINDER_REQUEST', params=payload).text.encode('utf-8')

    root = ET.fromstring(response)

    #for child in root.iter('p'):
    sub_sf = root.find('sf')
    sub_p = sub_sf.find('p')
    #if DEBUG: print ET.dump(child)
    rec_name = sub_p.find('n').text
    #   rec_uuu = child[1].text
    #   rec_type = child.find('ty').text
    sub_r = sub_p.find('r')
    #   rec_id = child[3][0].text
    #   rec_stateless = child.find('stateless').text
    #   rec_omc = child[3][2].text
    #   rec_pc = child[3][3].text
    #   rec_pid = child[3][4].text
    rec_c = sub_r.find('c').text
    #   #rec_qal = child[4].text


    #Format location
    (lon,lat) = rec_c.split(',')
    lat = float(lat) / 1000000.0
    lon = float(lon) / 1000000.0


    #print rec_name+':'+rec_uuu+':'+rec_type+':'+rec_id+':'+rec_stateless+':'+rec_omc+':'+rec_pc+':'+rec_pid+':'+rec_c+':'+rec_qal
    print str(incrementer) + ':' + rec_name + ':' + str(lat) + ':' + str(lon)

  except:
    errorcount = errorcount + 1
    next




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

# http://journeyplanner.translink.co.uk/android/XML_COORD_REQUEST?
# language=en&
# coord=736626.0%3A127825.0%3AITMR%3A&
# coordListOutputFormat=STRING&
# max=5&
# inclFilter=1&
# coordOutputFormat=ITMR&
# type_1=STOP&
# radius_1=1000
