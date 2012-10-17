'''
Created on Oct 9, 2012

@author: besn
'''

import urllib2
import simplejson as json
import pprint

CITIES = [{'id':1,
           'name': 'Skaevinge',
           'geo' : '55.908874,12.153129',
           'xmin' : '55.863998',
           'ymin' : '12.073194',
           'xmax' : '55.9538',
           'ymax':'12.233065'
           },
          {'id':2,
           'name': 'Oerbaek',
           'geo' : '55.257153,10.669954',
           'xmin' : '55.2122',
           'ymin' : '10.591332',
           'xmax' : '55.302101',
           'ymax' : '10.748576'
           },
          {'id':3,
           'name': 'Holeby',
           'geo' : '54.711930,11.465784',
           'xmin' : '54.667',
           'ymin' : '11.38822',
           'xmax' : '54.756802',
           'ymax' : '11.543347'
           },          
          {'id':4,
           'name': 'Kolind',
           'geo' : '56.357984,10.582423',
           'xmin' : '56.313099',
           'ymin' : '10.501551',
           'xmax' : '56.402901',
           'ymax' : '10.663296'
           
           }, 
           {'id':5,
           'name': 'Langaa',
           'geo' : '56.394259,9.896584',
           'xmin' : '56.3494',
           'ymin' : '9.815635',
           'xmax' : '56.439201',
           'ymax' : '9.977534'
           
           
           },           
           {'id':6,
           'name': 'Hurup',
           'geo' : '56.749880,8.422464',
            'xmin' : '56.705002',
            'ymin' : '8.340751',
            'xmax' : '56.7948',
            'ymax' : '8.504177'
           }, 
           {'id':7,
            'name' : 'Koebenhavn',
            'geo' : '55.693098,12.58296',
            'ymin':'12.5035',
            'xmin': '55.648201',
            'ymax':'12.6625',
            'xmax' : '55.737999'
            } 
          ]

def search(geo='', id='',name='', xmin='',ymin='',xmax='',ymax=''):
    # coords = geo.split(',')
    # query = "http://api.wikilocation.org/articles?lat=%s&lng=%s&radius=5000" % (coords[0], coords[1])
    query = "http://www.panoramio.com/map/get_panoramas.php?order=popularity&set=public&from=0&to=10&minx=%s&miny=%s&maxx=%s&maxy=%s" % (ymin,xmin,ymax,xmax)
    print query
    f = urllib2.urlopen(query)
    r = json.loads(f.read())
    #articles = r.get('articles')
    count = r.get("count")
    print str(id) + " : " + name + " : "+ str(count)
    #print str(id) + " : " + str(len(articles))
    #pprint.pprint(r)

if __name__ == '__main__':
    for city in CITIES:
    
        geo = city.get('geo')
        id = city.get('id')
        xmin = city.get('xmin')
        ymin = city.get('ymin')
        xmax = city.get('xmax')
        ymax = city.get('ymax')
        name = city.get('name')
    
        #query Search API
        search(geo=geo, id=id, name=name, xmin=xmin, ymin=ymin, xmax = xmax, ymax = ymax)
        
    print "====="