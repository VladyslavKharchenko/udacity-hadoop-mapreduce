import sys

prev_page = None
number_of_hits = 0

for line in sys.stdin:
    curr_page = line.strip().split('\t')
    if len(curr_page) is not 1:
        # Something has gone wrong. Skip this line.
        continue

    if curr_page and curr_page != prev_page and prev_page is not None:
        print('{0}\t{1}'.format(prev_page, number_of_hits))
        number_of_hits = 0

    prev_page = curr_page
    number_of_hits += 1

if prev_page is not None:
    print('{0}\t{1}'.format(prev_page, number_of_hits))

