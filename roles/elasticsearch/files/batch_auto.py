#!/usr/bin/env python3
import sys

passwords = (line[:-1].split(" ")
             for line in sys.stdin if line.startswith('PASSWORD'))
kv = ['"%s" : "%s"' % (l[1], l[3]) for l in passwords]
print('{', ', '.join(kv), '}')
