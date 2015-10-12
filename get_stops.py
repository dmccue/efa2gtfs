#!/usr/bin/python

import requests, sys, json, csv

places = set()
errorcount = 0

header = [
  'stop_id',
  'stop_name',
  'stop_desc',
  'stop_lat',
  'stop_lon',
  'stop_url',
  'location_type',
  'parent_station'
]

def show_help():
    print "Please provide a start and end id as arg1/arg2"
    sys.exit(1)

if len(sys.argv) < 3:
    show_help()

if not int(sys.argv[1]) or not int(sys.argv[2]):
    show_help()

incrementer = int(sys.argv[1])
incrementer_limit = int(sys.argv[2])

def get_stopid(id):
    payload = {
        'language': 'en',
        'googleAnalytics': 'false',
        'coordOutputFormat': 'WGS84',
        'locationServerActive': '1',
        'stateless': '1',
        'type_sf': 'stop',
        'outputFormat': 'JSON',
        'name_sf': str(id)
    }
    response = requests.get('http://journeyplanner.translink.co.uk/android/XML_STOPFINDER_REQUEST', params=payload).text.encode('utf-8')

    root = json.loads(response)

    rec_coords =        root['stopFinder']['points']['point']['ref']['coords'].split(',')
    rec_coords[0] =     str(float(rec_coords[0]) / 1000000.0)
    rec_coords[1] =     str(float(rec_coords[1]) / 1000000.0)
    #rec_omc =           root['stopFinder']['points']['point']['ref']['omc']

    row = [
        root['stopFinder']['points']['point']['ref']['id'],
        root['stopFinder']['points']['point']['name'],
        '',
        rec_coords[1],
        rec_coords[0],
        '',
        '',
        ''
    ]

    places.add((root['stopFinder']['points']['point']['ref']['placeID'], root['stopFinder']['points']['point']['ref']['place']))
    return row



with open('GTFS/stops.txt', 'wb') as f:
    csvwrite = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csvwrite.writerow(header)
    while incrementer < incrementer_limit:
      try:
        csvwrite.writerow(get_stopid(incrementer))
      except:
        errorcount += 1
        print >> sys.stderr, "Error: " + str(incrementer)
      incrementer += 1


with open('GTFS/places.txt', 'a') as f:
    csvwrite = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for place in places:
        csvwrite.writerow(place)

print 'Encountered ' + str(errorcount) + ' errors'
