"""

Python wrapper for the Yahoo Placemaker API 
    http://developer.yahoo.com/geo/placemaker/

It's based on https://github.com/bycoffe/python-placemaker
This version uses json as an output type.

Requires an API key from the Yahoo:
    http://developer.yahoo.com/wsregapp/

Yahoo Placemaker API Documentation:
    http://developer.yahoo.com/geo/placemaker/guide/web-service.html


"""

__author__ = "Marcin Grotomirski (grotos@gmail.com)"
__version__ = "0.1"
__license__ = "BSD"

import urllib
import urllib2
import simplejson as json

class Scope(object):
    
    def __init__(self,document):
        self.woeId = document['woeId']
        self.name = document['name']
        self.type = document['type']
        self.latitude = float(document['centroid']['latitude'])
        self.longitude = float(document['centroid']['longitude'])
    
    def __str__(self):
        return self.name    

    def __repr__(self):
        return u"<Placemaker Scope: '%s'>" % self.name
    
    
class Place(object):
    
    def __init__(self,document):
        self.confidence = document['confidence']
        self.woeId = document['place']['woeId']
        self.name = document['place']['name']
        self.type = document['place']['type']
        self.latitude = float(document['place']['centroid']['latitude'])
        self.longitude = float(document['place']['centroid']['longitude'])

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return u"<Placemaker Place: '%s'>" % self.name

class placemaker(object):
    
    def __init__(self,api_key):
        self.api_key = api_key 
        self.url = 'http://wherein.yahooapis.com/v1/document'
        
    def find_places(self, text):
        self.values = {'appid': self.api_key,
          'documentType': 'text/plain',
          'inputLanguage': 'en-US',
          'outputType': 'json',
          'documentTitle': '',
          'autoDisambiguate': 'true',
          'focusWoeid': '',
          'documentContent':text}
       
        self.data = urllib.urlencode(self.values)
        self.trial=self.url,self.data
        self.req = urllib2.Request(self.url, self.data)
        self.response = urllib2.urlopen(self.req)
        self.response_json = json.loads(self.response.read())
        self.doc = self.response_json['document']
        
        self.administrative_scope = Scope(self.doc['administrativeScope'])
        self.geographic_scope = Scope(self.doc['geographicScope'])
        
        self.place_details = {}
        if 'placeDetails' in self.doc:
            self.place_details = {'0': {'placeDetails': self.doc['placeDetails']}}
        else:
            self.place_details = {key: value for key, value in self.doc.iteritems() 
                                  if key not in ('extents','administrativeScope', 'geographicScope','localScopes','referenceList')}
        
        self.places = [Place(value['placeDetails']) for key, value in self.place_details.iteritems()]
        return self.places