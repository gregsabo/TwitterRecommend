#!/usr/bin/env python

import os, sys, time

def main():
  artist_norm = []

  for line in sys.stdin:
      line = line.strip()
      id1, id2, artist, profile = line.split('\t')
      username = profile.split('/')[-1]
      artist_norm.append((artist, username))

  for artist, username in artist_norm:
      print '%s\t%s'% (artist, username)

if __name__ == '__main__':
  main()
