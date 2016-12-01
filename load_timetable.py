#!/usr/bin/python
import ConfigParser, sqlite3, json, requests

def init_db():
    db.row_factory = sqlite3.Row


def get_trip(baseurl,from_id,to_id):
    payload = {
        'locationServerActive': '1',
        'appCache': 'true',
        'googleAnalytics': 'false',
        'limit': '999999',
        'outputFormat': 'JSON',
        'coordListOutputFormat': 'STRING',
        'coordOutputFormat': 'WGS84',
        'language': 'en',
        'useRealtime': '1',
        'calcNumberOfTrips': '100',
        'calcOneDirection': '1',
        'routeType': 'LEASTINTERCHANGE',
        'idtDate': '20151019',
        'idtTime': '0000',
        'type_origin': 'any',
        'type_destination': 'stopID',
        'name_origin': str(from_id),
        'name_destination': str(to_id)
        # 'depType': 'stopEvents',
        # 'mode': 'direct',
        # 'includeCompleteStopSeq': '1',
        # 'name_dm': str(id)
    }
# calcNumberOfTrips=2&
# coordOutputFormatTail=0&
# excludedMeans=checkbox&
# itOptionsActive=1&
# changeSpeed=normal&
# routeType=LEASTINTERCHANGE&
# imparedOptionsActive=1&
# noAlt=1&
# useProxFootSearch=true&
# calcMonoTrip=0&
# calcMonoPTTrip=0&
# trITMOTvalue100=15&
# lineRestriction=400&
# calcOneDirection=1&
# ptOptionsActive=1&
# snapHouseNum=1

# -------------------test------------
# coordOutputFormatTail=0
# imparedOptionsActive=1&
# excludedMeans=checkbox&
# useProxFootSearch=false&
# itOptionsActive=1&
# trITMOTvalue100=15&
# changeSpeed=normal&
# ptOptionsActive=1&
# snapHouseNum=1


    response = requests.get(baseurl + 'XSLT_TRIP_REQUEST2', params=payload).text.encode('utf-8')
    #print json.dumps(json.loads(response), sort_keys = False, indent = 2)
    try:
        returnval = json.loads(response)['trips']
    except TypeError:
        return []
    return returnval


Config = ConfigParser.ConfigParser()
Config.read('config.ini')
db = sqlite3.connect(Config.get('default','DatabaseFile'))
init_db()

cur = db.cursor()
cur.execute("select * from route_path")

for route in cur:

    #route = {"route_id":"", "route_seq":"10007686,10003969"}

    print "route:", route['route_id']
    route_stops = route['route_seq'].split(',')
    #print "route_stops:", route_stops
    route_stops_len = len(route_stops)
    print "start:", route_stops[0]
    #print "mid:  ", route_stops[route_stops_len/2]
    print "end:  ", route_stops[-1]
    #print "len:  ", str(route_stops_len)

    for trip in get_trip(Config.get('default','BaseURL'), route_stops[0], route_stops[-1]):
        try:
            lineID = trip['legs'][0]['mode']['diva']['stateless']
        except TypeError:
            continue
        if trip['interchange'] != '0' or not lineID.split(":")[0]: continue
        #for keyval in trip.keys():
        #    print keyval, trip[keyval]
        #print "Leg keys:", trip['legs'][0].keys()
        #print "Duration:", trip['legs'][0]['timeMinute'], "minutes"

        #print "LineDesc:", trip['legs'][0]['mode']['desc']
        # for point in trip['legs'][0]['points']:
        #     print "ID:", point['ref']['id']
        #     print "point", point['dateTime']

        print "LineID:", lineID
        # List out stop times
        stoptime = []
        stoptime.append((trip['legs'][0]['points'][0]['ref']['id'],trip['legs'][0]['points'][0]['dateTime']['rtTime']))
        for stop in trip['legs'][0]['stopSeq'][1:]:
            if 'arrDateTime' in stop['ref'].keys():
                stoptime.append((stop['ref']['id'],stop['ref']['arrDateTime'].split(" ")[-1]))
        print stoptime

        print "-----------------"

    #break
