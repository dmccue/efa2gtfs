

Dependencies:

Install Chrome Browser manually
> brew install python
> pip install --upgrade selenium scrapy


1. Run ./1_get_pdf_links.py which will store pdf_links.json in tmp
2. Run ./2_spider_pdfs.sh which will download all pdfs to tmp









# Get info about a stop
# http://journeyplanner.translink.co.uk/android/XML_STOPFINDER_REQUEST?
# language=en&
# coordOutputFormat=ITMR&
# locationServerActive=1&
# stateless=1&
# name_sf=castlereagh&
# type_sf=any&

# Get info about a coordinate
# http://journeyplanner.translink.co.uk/android/XML_COORD_REQUEST?
# language=en&
# coord=736626.0%3A127825.0%3AITMR%3A&
# coordListOutputFormat=STRING&
# max=5&
# inclFilter=1&
# coordOutputFormat=ITMR&
# type_1=STOP&
# radius_1=1000

# Get info about a trip
# http://journeyplanner.translink.co.uk/android/XML_TRIP_REQUEST2?
# language=en&
# calcNumberOfTrips=2&
# coordListOutputFormat=STRING&
# coordOutputFormat=ITMR&
# coordOutputFormatTail=0&
# useRealtime=1&
# locationServerActive=1&
# itdTime=1430&
# itdDate=20151008&
# name_origin=suburbID%3A31400030%3A224%3ACastlereagh%3A736626%3A127825%3AITMR&
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
# lineRestriction=400&
# calcOneDirection=1&
# appCache=true&
# ptOptionsActive=1&
# snapHouseNum=1

# Get route details
# http://journeyplanner.translink.co.uk/android/XML_DM_REQUEST?
# language=en&
# mode=direct&
# coordOutputFormat=ITMR&
# mergeDep=1&
# useAllStops=1&
# maxTimeLoop=1&
# canChangeMOT=0&
# useRealtime=1&
# locationServerActive=1&
# depType=stopEvents&
# includeCompleteStopSeq=1&
# name_dm=10005183&
# type_dm=stop&
# imparedOptionsActive=1&
# googleAnalytics=false&
# excludedMeans=checkbox&
# useProxFootSearch=0&
# itOptionsActive=1&
# trITMOTvalue100=15&
# lineRestriction=400&
# appCache=true&
# changeSpeed=normal&
# routeType=LEASTINTERCHANGE&
# ptOptionsActive=1&
# limit=30&
# snapHouseNum=1

