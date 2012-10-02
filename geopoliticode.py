import urllib
import csv
import simplejson as json


YAHOO_APP_ID = 'INSERT PLACEFINDER APP ID HERE'

test = "629 E 51st St Savannah GA 31405"
yahoo = "http://where.yahooapis.com/geocode?"

class YahooException(Exception): 
  pass

def placefind(query): 
  file = urllib.urlopen("http://where.yahooapis.com/geocode?%s" % urllib.urlencode({ 
    'appid': YAHOO_APP_ID,
    'flags': 'j',
    'q': query[0]
  })) 
  try:
    result = json.loads(file.read()) 
    return result['ResultSet']['Result']['county'], result['ResultSet']['Result']['latitude'], result['ResultSet']['Result']['longitude']
  except: 
    print 'not found' 
  finally: 
    file.close() 
    
def findCongress(lat, lon):
    url = 'http://congress.mcommons.com/districts/lookup.json?lat=' + lat + '&lng=' + lon
    dom = json.loads(urllib.urlopen(url).read())
    districts = dom
    try:
     return districts['federal']['district'], districts['state_upper']['district'], districts['state_lower']['district']
    except:
     print 'not found'


file = 'addresses.csv'
ifile = open(file, "rU")
Reader = csv.reader(ifile)
Writer = csv.writer(open("addressesupdated.csv", "wb"), delimiter=',', quoting=csv.QUOTE_ALL)

Writer.writerow(['Street Address', 'County', 'Latitude', 'Longitude', 'Federal District', 'State Upper', 'State Lower'])
for row in Reader:
    entry = []
    entry.append(row[0])
    county = placefind(row)
    print county
    if (county):
        entry.append(county[0])
        entry.append(county[1])   
        entry.append(county[2])
        districts = findCongress(county[1], county[2])
        if (districts):
            entry.append(districts[0])
            entry.append(districts[1])
            entry.append(districts[2])
    Writer.writerow(entry)
    
ifile.close();