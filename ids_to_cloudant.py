# Get the list of artist names, screennames, and ids into Thierry's cloudant.
# Assumes a text file as the source.  
# text file will be: artist\tscree name\ttwitter id, tab separated.

import hashlib
from couchdbkit import Server

s = Server("https://thierrybm.cloudant.com")
db = s.get_or_create_db(u"twitterrecommend")

f = open('reduced.txt', 'r')
for line in f:
    read_line = line.split('\t')
    if len(read_line) != 3:
        continue
    artist = read_line[0].strip()
    screen = read_line[1].strip()
    tid = read_line[2].strip()

    m = hashlib.md5()
    m.update(artist + screen + tid)
    key = m.hexdigest()
    try:
        db[key] = {'artist_name':artist, 'screen_name':screen, 'twitter_id':tid}
    except:
        print "Error:  could not create record for %s - %s" % (screen, tid)
