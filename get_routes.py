#!/usr/bin/python

import requests, sys, json, csv


def get_routesatstopid(input_id):

    payload = {
        'locationServerActive': '1',
        'type_dm': 'stop',
        'limit': '999999',
        'outputFormat': 'JSON',
        'coordOutputFormat': 'WGS84',
        'language': 'en',
        'name_dm': input_id
    #     ,
    #     'outputFormat': 'JSON',
    #     'mode': 'direct',
    #     'mergeDep': '1',
    #     'useAllStops': '1',
    #     'maxTimeLoop': '1',
    #     'canChangeMOT': '0',
    #     'useRealtime': '1',
    #     'depType': 'stopEvents',
    #     'includeCompleteStopSeq': '0',
    #     'name_dm': '10005183',
    #     'type_dm': 'stop',
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

    routes = []
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

def write_headertofile():
    header = ['route_id','agency_id','route_short_name','route_long_name','route_desc','route_type','route_url','route_color','route_text_color']
    with open('GTFS/routes.txt', 'wb') as f:
        csvwrite = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvwrite.writerow(header)

def write_routestofile(input_routes):
    with open('GTFS/routes.txt', 'wb') as f:
        csvwrite = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in input_routes:
            csvwrite.writerow(row)


# Main
write_headertofile()
with open('GTFS/stops.txt', 'rb') as csvfile:
    csvread = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csvread:
        stopid = str(row[0])
        print "Getting routes at stop: " + stopid
        returned_routes = get_routesatstopid(stopid)
        print "Found " + str(len(returned_routes)) + " routes"
        write_routestofile(returned_routes)


#(' + line['mode']['destID'] + ', ' + line['mode']['destination'] + ')'
#    print json.dumps(line)


# for key,val in root.items():
#     if key and val:
#       print str(key) + ' = ' + str(len(str(val)))
#     elif key:
#       print str(key)
#
# #print json.dumps(root, sort_keys = False, indent = 4)
# sys.exit(1)
#
#
# print 'arr: not needed'
# print 'parameters: not needed'
# print 'dateTime: ' + str(root['dateTime'].keys())
# for item in root['dateRange']:
#     print str(item)
