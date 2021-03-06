#!/usr/bin/env python

import os, sys, time
import httplib, json

def get_twitter_id(username, api):
  api.request('GET', '/1/users/show.json?screen_name='+username)
  t0 = time.clock
  while True:
    try:
      res = api.getresponse()
      break
    except:
      if time.clock() - t0 < 30:
        print "Response not yet ready"
      else:
        print "Timeout"
        break
  if res.status == 200:
    return json.loads(res.read())['id']
  else:
    return None

def main():
  artist_twitterid = []
  api = httplib.HTTPConnection('api.twitter.com')

  for line in sys.stdin:
      line = line.strip()
      id1, id2, artist, profile = line.split('\t')
      username = profile.split('/')[-1]
      tid = get_twitter_id(username, api)
      artist_twitterid.append((artist, username, tid))

  for artist, username, tid in artist_twitterid:
      print '%s\t%s\t%s'% (artist, username, tid)

if __name__ == '__main__':
  main()
