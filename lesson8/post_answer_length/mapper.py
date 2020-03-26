#!/usr/bin/python

"""
We are interested to see if there is a correlation between the length of a post and the length of answers.

Write a MapReduce program that would process the forum_node data and output the length of the post
and the average length of an answer (just answer, not comment) for each post.
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
                    writer.writerow([id, len(body), 'Q'])
                elif node_type == 'answer':
                    writer.writerow([abs_parent_id, len(body), 'A'])

        except ValueError:
            raise


if __name__ == "__main__":
    mapper()
