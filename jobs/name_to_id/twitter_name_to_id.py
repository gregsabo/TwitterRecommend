#!/usr/bin/env python

import os, sys

sys.path.append("deps/httplib2-0.7.1")
sys.path.append("deps/python-oauth2")
sys.path.append("deps/simplejson-2.1.6")
sys.path.append("deps/python-twitter-0.8.2")

import twitter

api = twitter.Api()

# twitter url => twitter id

artist_twitterid = []

for line in sys.stdin:
    line = line.strip()
    id, artist, profile = line.split('\t')
    username = profile.split('/')[-1]
    tid = api.GetUser(username).id
    artist_twitterid.append((artist, username, tid))

for artist, username, tid in artist_twitterid:
    print '%s\t%s\t%s'% (artist, username, tid)

