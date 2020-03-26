#!/usr/bin/python

import sys
import csv


def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')

    prev_author_id = None
    posts = []

    for line in reader:
        if len(line) == 2:

            curr_author_id, hour = line
            hour = int(hour)

            if prev_author_id and prev_author_id != curr_author_id:
                result = sorted(posts, key=posts.count, reverse=True)
                prev_counter = 0
                for _ in range(len(set(result))):
                    curr_counter = result.count(result[prev_counter])
                    if curr_counter < prev_counter:
                        break
                    else:
                        prev_counter += curr_counter
                print("{0}\t{1}".format(prev_author_id, set(result[:prev_counter])))
                posts.clear()

            posts.append(hour)
            prev_author_id = curr_author_id

    if prev_author_id is not None and posts:
        result = sorted(posts, key=posts.count, reverse=True)
        prev_counter = 0
        for _ in range(len(set(result))):
            curr_counter = result.count(result[prev_counter])
            if curr_counter < prev_counter:
                break
            else:
                prev_counter += curr_counter
        print("{0}\t{1}".format(prev_author_id, set(result[:prev_counter])))


if __name__ == "__main__":
    reducer()
