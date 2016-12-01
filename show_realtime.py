#!/usr/bin/python
import ConfigParser, sqlite3, sys, requests, json

# Main
Config = ConfigParser.ConfigParser()
Config.read('config.ini')


def get_route(baseurl,id):

    payload = {
        'locationServerActive': '1',
        'appCache': 'true',
        'googleAnalytics': 'false',
        'type_dm': 'stop',
        'limit': '999',
        'outputFormat': 'JSON',
        #'coordListOutputFormat': 'STRING',
        'coordOutputFormat': 'WGS84',
        'language': 'en',
        'depType': 'stopEvents',
        'mode': 'direct',
        'includeCompleteStopSeq': '1',
        'name_dm': str(id),
        #'useProxFootSearch': '0',
        #'useAllStops': '1',
        'useRealtime': '1'
        #     'mergeDep': '1',
        #     'useAllStops': '1',
        #     'maxTimeLoop': '1',
        #     'canChangeMOT': '0',
        #     'useRealtime': '1',
        #     'imparedOptionsActive': '1',
        #     'excludedMeans': 'checkbox',
        #     'useProxFootSearch': '0',
        #     'itOptionsActive': '1',
        #     'trITMOTvalue100': '15',
        #     'lineRestriction': '400',
        #     'changeSpeed': 'normal',
        #     'routeType': 'LEASTINTERCHANGE',
        #     'ptOptionsActive': '1',
        #     'snapHouseNum': '1'
    }
    response = requests.get(baseurl + 'XML_DM_REQUEST', params=payload).text.encode('utf-8')
    return json.loads(response)


x = get_route(Config.get('default','BaseURL'),10003781)
# for item in x.keys():
#     for item2 in item.keys():
#         print str(item2)
    # print item, str(item[item].keys())
x = x["servingLines"]["lines"]
for item in x:
    print item["mode"]["diva"]["stateless"]
#print json.dumps(x, indent=2, sort_keys=True)
