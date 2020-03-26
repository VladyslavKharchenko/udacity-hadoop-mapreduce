#!/usr/bin/python

"""
Students and Posting Time on Forums
We have a lot of passionate students that bring a lot of value to forums. Forums also sometimes need a watchful
eye on them, to make sure that posts are tagged in a way that helps to find them, that the tone on forums stays
positive, and in general - they need people who can perform some management tasks - forum moderators.
These are usually chosen from students who already have shown that they are active and helpful forum participants.

Our students come from all around the world, so we need to know both at what times of day the activity is the highest,
and to know which of the students are active at that time.

In this exercise your task is to find for each student what is the hour during which the student has posted
the most posts. Output from reducers should be:

author_id    hour
For example:

13431511\t13
54525254141\t21

If there is a tie: there are multiple hours during which a student has posted a maximum number of posts, please print
the student-hour pairs on separate lines. The order in which these lines appear in your output does not matter.

You can ignore the time-zone offset for all times - for example in the following line:
"2012-02-25 08:11:01.623548+00" - you can ignore the +00 offset.

In order to find the hour posted, please use the date_added field and NOT the last_activity_at field.


Hints for writing reducer code

Code should not use a data structure (e.g. a dictionary) in the reducer that stores a large number of keys.
Remember that Hadoop already sorts the mapper output based on key, such that key-value pairs with the same key will
appear consecutively as input to the reducer. Make sure you take advantage of this ordering when you write your reducer
code.

This is part of a more general principle connected with the Volume characteristic of Big Data. Mappers and reducers
read through very large amounts of data and we should be mindful, as we write mapper and reducer code, of how much data
we store in main memory.
"""

import sys
import csv
from datetime import datetime


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
                aa = added_at[:-3]
                hour = datetime.strptime(aa, '%Y-%m-%d %H:%M:%S.%f').time().hour
                writer.writerow(
                    [author_id, hour])
        except ValueError:
            raise


if __name__ == "__main__":
    mapper()
