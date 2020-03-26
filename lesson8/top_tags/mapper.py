#!/usr/bin/python

"""
We are interested seeing what are the top tags used in posts.

Write a MapReduce program that would output Top 10 tags, ordered by the number of questions they appear in.

Please note that you should only look at tags appearing in questions themselves
(i.e. nodes with node_type "question"), not on answers or comments.
"""

import sys
import csv


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    headers = ['id', 'title', 'tagnames', 'author_id',
               'body', 'node_type', 'parent_id', 'abs_parent_id', 'added_at',
               'score', 'state_string', 'last_edited_id', 'last_activity_by_id',
               'last_activity_at', 'active_revision_id', 'extra', 'extra_ref_id',
               'extra_count', 'marked']
    for line in reader:
        if line == headers:
            continue  # skip line with headers
        try:
            if (len(line)) == 19:
                id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, \
                state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, \
                extra_ref_id, extra_count, marked = line
                if node_type == 'question':
                    tags = tagnames.strip().split(' ')
                    for tag in tags:
                        writer.writerow([tag])

        except ValueError:
            raise


if __name__ == "__main__":
    mapper()
