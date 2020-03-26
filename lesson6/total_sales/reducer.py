import sys

value_of_sales = 0
number_of_sales = 0

for line in sys.stdin:

    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    this_store, this_sale = data_mapped
    this_sale = float(this_sale)

    value_of_sales += this_sale
    number_of_sales += 1

print('{0}\t{1}'.format(number_of_sales, value_of_sales))

