#!/usr/bin/env python

import os, sys
import httplib, json

def get_twitter_id(username, api):
  api.request('GET', '/1/users/show.json?screen_name='+username)
  res = api.getresponse().read()
  return json.loads(res)['id']

def main():
  artist_twitterid = []
  api = httplib.HTTPConnection('api.twitter.com')

  for line in sys.stdin:
      line = line.strip()
      id, artist, profile = line.split('\t')
      username = profile.split('/')[-1]
      tid = get_twitter_id(username, api)
      artist_twitterid.append((artist, username, tid))

  for artist, username, tid in artist_twitterid:
      print '%s\t%s\t%s'% (artist, username, tid)

if __name__ == '__main__':
  main()
