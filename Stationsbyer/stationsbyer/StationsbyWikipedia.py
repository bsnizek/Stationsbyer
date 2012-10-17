'''
Created on Oct 9, 2012

@author: besn
'''

import urllib2
import simplejson as json
import pprint

CITIES = [{'id':1,
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
           {'id':6,
           'name': 'Hurup',
           'geo' : '56.749880,8.422464'
           }, 
           {'id':7,
            'name' : 'Koebenhavn',
            'geo' : '55.693098,12.58296'
            }
          
          
          ]

def search(geo='', id='', name=''):
    coords = geo.split(',')
    query = "http://api.wikilocation.org/articles?lat=%s&lng=%s&radius=5000&locale=de" % (coords[0], coords[1])
    f = urllib2.urlopen(query)
    r = json.loads(f.read())    
    articles = r.get('articles')
    print str(name) +" : " + str(id) + " : " + str(len(articles))
    # pprint.pprint(r)


    

if __name__ == '__main__':
    for city in CITIES:
    
        geo = city.get('geo')
        id = city.get('id')
        name = city.get('name')
    
        #query Search API
        search(geo=geo, id=id, name=name)
        
    print "====="