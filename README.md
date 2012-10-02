#Geo-Politi-Code

This side project was developed as part of a larger project, where a large number of addresses needed to be geocoded and the corresponding county found.  Later, legislative districts were needed and that functionality was added. 

This project utilizes the [Yahoo Placefinder API](http://developer.yahoo.com/geo/placefinder/) and [Mobile Commons Legislative Lookup](http://www.mobilecommons.com/mobile-commons-api/legislative-lookup/)

##Using

When run from console, ```geopoliticode.py``` takes a CSV file of street addresses, "addresses.csv", as input and returns a csv "addressesupdated.csv" containing street address, county, federal house districts, and state house and senate districts.
