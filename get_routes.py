#!/usr/bin/python


import requests, sys, json, csv, os


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
routes = set()
destinations = set()

def get_routesatstopid(input_id):
  out_routes = []

  payload = {
    'locationServerActive': '1',
    'googleAnalytics': 'false',
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

  print json.dumps(root['servingLines']['lines'], sort_keys = False, indent = 2)

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
    out_routes.append(row)
    destinations.add((line['mode']['diva']['stateless'],line['mode']['destID']))
  return out_routes


# Main
with open('GTFS/stops.txt', 'rb') as f:
  for row in csv.reader(f, delimiter=',', quotechar='"'):
    stop_id = str(row[0])
    if stop_id == 'stop_id': next
    returned_routes = get_routesatstopid(stop_id)
    for returned_route in returned_routes:
      routes.add(tuple(returned_route))
    #os.system('clear')
    print "Getting routes at stop: " + stop_id
    print "Found " + str(len(returned_routes)) + " new routes, total: " + str(len(routes))
    #break

# Write routes to file
print "Writing routes to routes.txt..."
with open('GTFS/routes.txt', 'wb') as f:
  csvwrite = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  csvwrite.writerow(header)
  for row in routes:
    csvwrite.writerow(row)

# Write destinations to file
with open('GTFS/_dest.txt', 'wb') as f:
  csvwrite = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  for row in destinations:
    csvwrite.writerow(row)
