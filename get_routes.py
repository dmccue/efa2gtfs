#!/usr/bin/python


import requests, sys, json, csv


header = [
  'route_id',
  'agency_id',
  'route_short_name',
  'route_long_name',
  'route_desc',
  'route_type',
  'route_url',
  'route_color',
  'route_text_color'
]


def get_routesatstopid(input_id):
  routes = []

  payload = {
    'locationServerActive': '1',
    'type_dm': 'stop',
    'limit': '999999',
    'outputFormat': 'JSON',
    'coordOutputFormat': 'WGS84',
    'language': 'en',
    'name_dm': input_id
    #     'mode': 'direct',
    #     'mergeDep': '1',
    #     'useAllStops': '1',
    #     'maxTimeLoop': '1',
    #     'canChangeMOT': '0',
    #     'useRealtime': '1',
    #     'depType': 'stopEvents',
    #     'includeCompleteStopSeq': '0',
    #     'imparedOptionsActive': '1',
    #     'googleAnalytics': 'false',
    #     'excludedMeans': 'checkbox',
    #     'useProxFootSearch': '0',
    #     'itOptionsActive': '1',
    #     'trITMOTvalue100': '15',
    #     'lineRestriction': '400',
    #     'appCache': 'true',
    #     'changeSpeed': 'normal',
    #     'routeType': 'LEASTINTERCHANGE',
    #     'ptOptionsActive': '1',
    #     'limit': '30',
    #     'snapHouseNum': '1'
  }
  response = requests.get('http://journeyplanner.translink.co.uk/android/XML_DM_REQUEST', params=payload).text.encode('utf-8')
  root = json.loads(response)

  # print json.dumps(root['servingLines']['lines'], sort_keys = False, indent = 2)

  if not root['servingLines']['lines']:
    return []

  if len(root['servingLines']['lines']) == 1:
    root['servingLines']['lines'] = [root['servingLines']['lines']['line']]

  for line in root['servingLines']['lines']:
    row = [
      line['mode']['diva']['stateless'],
      '',
      line['mode']['number'],
      line['mode']['name'],
      line['mode']['desc'],
      line['mode']['code'],
      '',
      '',
      ''
    ]
    routes.append(row)
  return routes


def write_headertofile(in_csvwrite, in_header):
  in_csvwrite.writerow(in_header)


def write_rowstofile(in_csvwrite, in_rows):
  for row in in_rows:
    in_csvwrite.writerow(row)


# Main
with open('GTFS/routes.txt', 'wb') as f:
  csvwrite = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  write_headertofile(csvwrite)

  with open('GTFS/stops.txt', 'rb') as csvfile:
    for row in csv.reader(csvfile, delimiter=',', quotechar='"'):
      stopid = str(row[0])
      print "Getting routes at stop: " + stopid
      returned_routes = get_routesatstopid(stopid)
      print "Found " + str(len(returned_routes)) + " routes"
      write_rowstofile(csvwrite, returned_routes)
