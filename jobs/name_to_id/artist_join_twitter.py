#!/usr/bin/env python

import os, sys, time

def main():
  artists = {}

  for line in sys.stdin:
      line = line.strip()
      twittername, val = line.split('\t')
      artists.setdefault(twittername, [])
      artists[twittername].append(val)

  for tname, vals in artists:
    if vals[0].isdigit():
      name = vals[1]
      tid = vals[0]
    else:
      name = vals[0]
      tid = vals[1]

    print "%s\t%s\t%s\t"%(name,tname,tid)

if __name__ == '__main__':
  main()

