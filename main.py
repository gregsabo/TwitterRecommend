'''
REST server for the similarity data
'''

import web
import json
import urllib2
from pyechonest import artist, util
 
#Ex: get_twitter_id('djfractal')
def get_twitter_id(screen_name):
    url_str = 'https://thierrybm.cloudant.com/twitterrecommend/_search?q=screen_name:%s&include_docs=true' % screen_name
    res = urllib2.urlopen(url_str)
    d = json.loads(res.read())
    return d['rows'][0]['doc']['twitter_id']

 
urls = (
    '/similar/(.*)', 'similar'
)
app = web.application(urls, globals())

class similar:        
    def GET(self, name):
        out_names = []
        try:
            similar = artist.similar(name)
        except util.EchoNestAPIError:
            return "error"
            
        for a in similar:
            out_names.append(a.name)
        return json.dumps(out_names)

if __name__ == "__main__":
    app.run()
