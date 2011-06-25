'''
REST server for the similarity data
'''

import web
import json
from pyechonest import artist
  
urls = (
    '/similar/(.*)', 'similar'
)
app = web.application(urls, globals())

class similar:        
    def GET(self, name):
        out_names = []
        for a in artist.similar(name):
            out_names.append(a.name)
        return json.dumps(out_names)

if __name__ == "__main__":
    app.run()