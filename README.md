#Geo-Politi-Code

This side project was developed as part of a larger project, where a large number of addresses needed to be geocoded and the corresponding county found.  Later, legislative districts were needed and that functionality was added. 

Initially, Yahoo Placefinder API was the best solution to geocode 1000+ addresses at a time, but with the discontinuation of the service a new free bulk geocoding solution will be needed after November 17, 2012.

This project utilizes the [Yahoo Placefinder API](http://developer.yahoo.com/geo/placefinder/) and [Mobile Commons Legislative Lookup](http://www.mobilecommons.com/mobile-commons-api/legislative-lookup/)

##Using

When run from console, ```geopoliticode.py``` takes a CSV file of street addresses, "addresses.csv", as input and returns a csv "addressesupdated.csv" containing street address, county, latitude, longitude, federal house districts, and state house and senate districts.


##Special Note
This will likely stop working on November 17, 2012 when Yahoo discontinues the free versions of the Placefinder API.  Check for an updated app as I try to migrate the code to another geocoding API.