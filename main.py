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
    if len(d[0]['rows']) == 0:
        return None
    return d[0]['rows'][0]['doc']['twitter_id']

def get_screenname(twitter_id):
    url_str = 'https://thierrybm.cloudant.com/twitterrecommend/_search?q=twitter_id:%s&include_docs=true' % twitter_id
    res = urllib2.urlopen(url_str)
    d = json.loads(res.read())
    return d['rows'][0]['doc']['screen_name']

def get_similars(twitter_id):
    url_str = 'https://thierrybm.cloudant.com/twitterrecommend/_search?q=twitter_id:%s&include_docs=true' % twitter_id
    print "URL WOULD BE", url_str
    res = urllib2.urlopen(url_str)
    d = json.loads(res.read())
    if isinstance(d, list):
        return None
    return d['rows'][0]['doc']['close'][1:]

 
urls = (
    '/similar/(.*)', 'similar',
    '/twittersimilar/(.*)', 'twittersimilar'
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

class twittersimilar:
    def GET(self, twitter_id):
        if len(twitter_id) == 0:
            twitter_id = 14400000
        # twitter_id = get_twitter_id(screen_name)
        return json.dumps(get_similars(twitter_id))

if __name__ == "__main__":
    app.run()
