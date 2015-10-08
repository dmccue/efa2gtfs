#!/usr/bin/python

import requests, sys, json

places = set()
errorcount = 0

def show_help:
    print "Please provide a start and end id as arg1/arg2"
    sys.exit(1)

if len(sys.argv) < 3:
    show_help()

if not int(sys.argv[1]) or not int(sys.argv[2]):
    show_help()

def get_stopid(id):
    payload = {
        'language': 'en',
        'coordOutputFormat': 'WGS84',
        'locationServerActive': '1',
        'stateless': '1',
        'type_sf': 'stop',
        'outputFormat': 'JSON',
        'name_sf': str(id)
    }
    response = requests.get('http://journeyplanner.translink.co.uk/android/XML_STOPFINDER_REQUEST', params=payload).text.encode('utf-8')

    root = json.loads(response)

    rec_name =          root['stopFinder']['points']['point']['name']
    rec_id =            root['stopFinder']['points']['point']['ref']['id']
    rec_coords =        root['stopFinder']['points']['point']['ref']['coords'].split(',')
    rec_coords[0] =     str(float(rec_coords[0]) / 1000000.0)
    rec_coords[1] =     str(float(rec_coords[1]) / 1000000.0)
    rec_placeid =       root['stopFinder']['points']['point']['ref']['placeID']
    rec_place =         root['stopFinder']['points']['point']['ref']['place']
    rec_omc =           root['stopFinder']['points']['point']['ref']['omc']

    places.add((rec_placeid, rec_place))
    #stop_id,stop_name,stop_desc,stop_lat,stop_lon,stop_url,location_type,parent_station
    return rec_id + ',' + rec_name + ',' + '' + rec_coords[1] + ',' + rec_coords[0] + ',' + '' + ',' + '' + ',' + ''

def write_places(input_arr):
    with open('GTFS/places.txt', 'a') as f:
        for place in input_arr:
            f.write(str(place[0]) + ',' + str(place[1]) + '\n')

while incrementer < int(sys.argv[2]):
  try:
    line = get_stopid(incrementer)
    incrementer = incrementer + 1

  except:
    errorcount = errorcount + 1
    print >> sys.stderr, "Error: " + str(incrementer)
    next

write_places(places)
