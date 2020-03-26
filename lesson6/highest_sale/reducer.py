import sys

highest_sale = 0
old_store = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    this_store, this_sale = data_mapped
    this_sale = float(this_sale)

    if old_store and old_store != this_store:
        print("{0}\t{1}".format(old_store, highest_sale))
        highest_sale = 0

    old_store = this_store
    if this_sale > highest_sale:
        highest_sale = this_sale

if old_store is not None:
    print("{0}\t{1}".format(old_store, highest_sale))

