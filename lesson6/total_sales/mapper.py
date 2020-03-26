import sys

# Task:
# Find the total sales value across all the stores, and the total number of sales. Assume there is only one reducer.

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print("{0}\t{1}".format(store, cost))

