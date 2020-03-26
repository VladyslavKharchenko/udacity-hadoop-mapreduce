#!/usr/bin/python

# Task:
# Instead of breaking the sales down by store,
# instead give us a sales breakdown by product category across all of our stores.

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print("{0}\t{1}".format(item, cost))

