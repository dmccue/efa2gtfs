# efa2gtfs


### Description

This is a project to extract GTFS data from MDV EFA

MDV (Mentz Datenverarbeitung) is a german software company that makes transport and timetable software

Their product known as Elektronische Fahrplanauskunft (EFA) provides an XML/JSON based API
https://de.wikipedia.org/wiki/Elektronische_Fahrplanauskunft
https://www.mentzdv.de

GTFS is the open General Transit Feed Specification, commonly used by google maps:
https://github.com/google/transitfeed/wiki

Please feel free to contribute, accepting pull requests

This project is in no way affiliated with any of the companies or products mentioned

### Related projects

EFA was previously known as diva and some projects exist for converting the previous format to gtfs
https://github.com/stkdiretto/diva2gtfs

OpenEFA has some documentation relating to the API
https://code.google.com/p/openefa

Golang client for EFA
https://github.com/michiwend/goefa

### API documentation

http://data.linz.gv.at/katalog/linz_ag/linz_ag_linien/fahrplan/LINZ_AG_Linien_Schnitstelle_EFA_v7_Echtzeit.pdf
http://content.tfl.gov.uk/journey-planner-api-documentation.pdf

### How to run

1. ./load_data.py 10000000 10013000
2. (Optional) ./create_map.py

### Progress

From: https://developers.google.com/transit/gtfs/reference

| Filename        | Required          | Status          |
| --------------- |:-----------------:| ---------------:|
| agency.txt | y | Static - Complete |
| stops.txt | y | Complete |
| routes.txt | y | Complete |
| trips.txt | y | In progress |
| stop_times.txt | y | todo |
| calendar.txt | y | todo |
| calendar_dates.txt | n |  |
| fare_attributes.txt | n |  |
| fare_rules.txt | n |  |
| shapes.txt | n |  |
| frequencies.txt | n |  |
| transfers.txt | n |  |
| feed_info.txt | n |  |

Planning to migrate to using the pygtfs python library
