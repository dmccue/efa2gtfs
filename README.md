# translink

Dependencies:

Install Chrome Browser manually
> brew install python
> pip install --upgrade selenium scrapy


1. Run ./1_get_pdf_links.py which will store pdf_links.json in tmp
2. Run ./2_spider_pdfs.sh which will download all pdfs to tmp




https://github.com/google/transitfeed/wiki

#http://journeyplanner.translink.co.uk/android/XML_TRIP_REQUEST2?
# language=en&
# calcNumberOfTrips=2&
# coordListOutputFormat=STRING&
# coordOutputFormat=ITMR&
# coordOutputFormatTail=0&
# useRealtime=1&
# locationServerActive=1&
# itdTime=0906&
# itdDate=20151002&
# name_origin=10001090&
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
# calcOneDirection=1&
# appCache=true&
# ptOptionsActive=1&
# snapHouseNum=1

# http://journeyplanner.translink.co.uk/android/XML_STOPFINDER_REQUEST?
# language=en&
# coordOutputFormat=ITMR&
# locationServerActive=1&
# stateless=1&
# name_sf=castlereagh&
# type_sf=any&

# http://journeyplanner.translink.co.uk/android/XML_COORD_REQUEST?
# language=en&
# coord=736626.0%3A127825.0%3AITMR%3A&
# coordListOutputFormat=STRING&
# max=5&
# inclFilter=1&
# coordOutputFormat=ITMR&
# type_1=STOP&
# radius_1=1000


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
