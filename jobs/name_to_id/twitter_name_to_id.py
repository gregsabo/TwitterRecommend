#!/usr/bin/env python

import os, sys
from mrjob.job import MRJob

sys.path.append("deps/httplib2-0.7.1")
sys.path.append("deps/python-oauth2")
sys.path.append("deps/simplejson-2.1.6")
sys.path.append("deps/python-twitter-0.8.2")

from deps.python_twitter import twitter

class MRNameToId(MRJob):
  def run(self):
    return[self.mr(self.get_ids, self.reduce),]

  def get_ids():
    api = twitter.Api()
    artist_twitterid = []

    for line in sys.stdin:
        line = line.strip()
        id, artist, profile = line.split('\t')
        username = profile.split('/')[-1]
        tid = api.GetUser(username).id
        artist_twitterid.append((artist, username, tid))

    for artist, username, tid in artist_twitterid:
        print '%s\t%s\t%s'% (artist, username, tid)

if __name__ == '__main__':
  MRNameToId.run()
