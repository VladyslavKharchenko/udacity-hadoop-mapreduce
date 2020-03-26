import sys

prev_page = None
number_of_hits = 0

pop_page = None
max_hits = 0

for line in sys.stdin:
    curr_page = line.strip().split('\t')
    if len(curr_page) is not 1:
        # Something has gone wrong. Skip this line.
        continue

    if curr_page and curr_page != prev_page and prev_page is not None:
        if number_of_hits > max_hits:
            max_hits = number_of_hits
            pop_page = prev_page
        number_of_hits = 0

    prev_page = curr_page
    number_of_hits += 1

print('{0}\t{1}'.format(pop_page, max_hits))

