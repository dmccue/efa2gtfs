#!/usr/bin/python

import requests, sys, json, csv, os

# http://journeyplanner.translink.co.uk/android/XML_DM_REQUEST?
# mergeDep=1&
# maxTimeLoop=1&
# canChangeMOT=0&
# imparedOptionsActive=1&
# googleAnalytics=false&
# excludedMeans=checkbox&
# itOptionsActive=1&
# trITMOTvalue100=15&
# lineRestriction=400&
# changeSpeed=normal&
# routeType=LEASTINTERCHANGE&
# ptOptionsActive=1&
# snapHouseNum=1
    # 'changeSpeed': 'normal',

route_paths = set()

payload = {
    'depType': 'stopEvents',
    'useProxFootSearch': '0',
    'useAllStops': '1',
    'appCache': 'true',
    'mode': 'direct',
    'includeCompleteStopSeq': '1',
    'locationServerActive': '1',
    'useRealtime': '0',
    'type_dm': 'stop',
    'limit': '999999',
    'outputFormat': 'JSON',
    'coordOutputFormat': 'WGS84',
    'language': 'en',
    'googleAnalytics': 'false',
    'name_dm': '10003969'
}

response = requests.get('http://journeyplanner.translink.co.uk/android/XML_DM_REQUEST', params=payload).text.encode('utf-8')
root = json.loads(response)
#print json.dumps(root, sort_keys = False, indent = 2)


for item in root['departureList']:
    sequence = []
    route_id = item['servingLine']['stateless']
    print 'ID:', route_id
    if 'prevStopSeq' in item and item['prevStopSeq']:
        for val in item['prevStopSeq']:
            sequence.append(val['ref']['id'])
    if 'stopID' in item and item['stopID']:
        sequence.append(item['stopID'])
    if 'onwardStopSeq' in item and item['onwardStopSeq']:
        for val in item['onwardStopSeq']:
            sequence.append(val['ref']['id'])
    sequence.append(item['servingLine']['destID'])
    print 'Sequence:', str(sequence)
    route_paths.add((route_id, "|".join(sequence)))


with open('GTFS/_paths.txt', 'wb') as f:
    csvwrite = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in route_paths:
        csvwrite.writerow(row)
