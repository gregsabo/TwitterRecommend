'''
REST server for the similarity data
'''

import web
import json
from pyechonest import artist, util
  
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