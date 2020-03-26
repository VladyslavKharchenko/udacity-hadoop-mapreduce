#!/usr/bin/python

"""
We might want to help students form study groups. But first we want to see if there are already students
on forums that communicate a lot between themselves.

As the first step for this analysis we have been tasked with writing a MapReduce program that for each
forum thread (that is a question node with all it's answers and comments) would give us a list of students
that have posted there - either asked the question, answered a question or added a comment.
If a student posted to that thread several times, they should be added to that list several times as well,
to indicate intensity of communication.
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
                    writer.writerow([id, author_id])
                elif node_type == 'answer':
                    writer.writerow([abs_parent_id, author_id])

        except ValueError:
            raise


if __name__ == "__main__":
    mapper()
