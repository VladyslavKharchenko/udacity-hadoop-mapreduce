#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys
import csv


def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    id = title = tagnames = prev_author_id = node_type = parent_id = \
        abs_parent_id = added_at = score = reputation = gold = silver = bronze = ""

    for line in reader:
        if len(line) < 6 or len(line) > 10:
            # Something has gone wrong. Skip this line.
            continue

        if line[1] is 'A':  # users file
            curr_author_id, source, reputation, gold, silver, bronze = line
        elif line[1] is 'B':  # posts file
            curr_author_id, source, id, title, tagnames, node_type, \
            parent_id, abs_parent_id, added_at, score = line
        else:
            continue

        if prev_author_id and prev_author_id != curr_author_id:
            writer.writerow(
                [id, title, tagnames, prev_author_id, node_type, parent_id, abs_parent_id,
                 added_at, score, reputation, gold, silver, bronze])

        prev_author_id = curr_author_id

        if prev_author_id is not None:
            writer.writerow(
                [id, title, tagnames, prev_author_id, node_type, parent_id, abs_parent_id,
                 added_at, score, reputation, gold, silver, bronze])


if __name__ == "__main__":
    reducer()
