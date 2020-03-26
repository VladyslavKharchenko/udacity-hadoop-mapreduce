#!/usr/bin/python

import sys
import calendar

total_cost = 0
counter = 0
prev_day = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    curr_day, curr_cost = data_mapped
    curr_day, curr_cost = int(curr_day), float(curr_cost)

    if curr_day and prev_day != curr_day:
        print("{}\t{}".format(calendar.day_name[prev_day], total_cost/counter))
        total_cost = 0
        counter = 0

    prev_day = curr_day
    total_cost += curr_cost
    counter += 1

if prev_day is not None:
    print("{}\t{}".format(calendar.day_name[prev_day], total_cost/counter))

