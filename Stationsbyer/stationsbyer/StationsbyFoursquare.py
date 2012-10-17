'''
Created on Oct 9, 2012

@author: besn

    http://www.infochimps.com/datasets/foursquare-places

'''

import urllib2
import simplejson as json
import pprint

CITIES = [ {'id':6,
           'name': 'Hurup',
           'geo' : '56.749880,8.422464'
           }, 
          
          {'id':7,
            'name' : 'Koebenhavn',
            'geo' : '55.693098,12.58296'
            },      
          
          
          {'id':1,
           'name': 'Skaevinge',
           'geo' : '55.908874,12.153129'
           },
          {'id':2,
           'name': 'Oerbaek',
           'geo' : '55.257153,10.669954'
           },
          {'id':3,
           'name': 'Holeby',
           'geo' : '54.711930,11.465784'
           },          
          {'id':4,
           'name': 'Kolind',
           'geo' : '56.357984,10.582423'
           }, 
           {'id':5,
           'name': 'Langaa',
           'geo' : '56.394259,9.896584'
           },     
          
           
          ]

def search(q='',lat='', lon=''):
    """ use search api to find tweets matching a query string and/or 
        location as string of "lat,lon,radius", see api documentation"""
    # query = 'http://search.twitter.com/search?q=%s&format=json&rpp=100&result_type=recent&geocode=%s' % (q,geo)
    query = 'http://api.infochimps.com/geo/location/foursquare/places/search?g.radius=5000&g.latitude=%s&g.longitude=%s&apikey=api_test-W1cipwpcdu9Cbd9pmm8D4Cjc469' % (lat, lon)
    print query
    f = urllib2.urlopen(query)
    r = json.loads(f.read())
    return r["results"]

def parse(res, id='', name=''):
    """ take the relevant parts of the result"""
    #list of tuples (user,time,geo)
    
    #pprint.pprint(res)
    
    print str(id) + " : " + name + " : " + str(len(res))
    
    # return [(r['from_user'],r['created_at'],r['geo']) 
    #        for r in res if r['geo'] != None]


if __name__ == "__main__":
    tag = '%23fail' 
    
    for city in CITIES:
    
        geo = '%s,5km' % city.get('geo')
        id = city.get('id')
        name = city.get('name')
        lat = city.get('geo').split(",")[0]
        lon = city.get('geo').split(",")[1]

        #query Search API
        parse(search(q=tag,lat=lat, lon=lon), id=id, name=name)