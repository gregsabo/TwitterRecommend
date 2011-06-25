#!/usr/bin/env python

import os, sys, time

def main():
  id_norm = []

  for line in sys.stdin:
      line = line.strip()
      tid, name = line.split('\t')
      print '%s\t%s'% (name, tid)

if __name__ == '__main__':
  main()

