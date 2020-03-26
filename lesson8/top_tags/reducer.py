#!/usr/bin/python

import sys
import csv


def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')

    prev_tag = None
    tags_count = 0
    result = {}

    for line in reader:
        if len(line) == 1:

            curr_tag = line[0]
            if prev_tag and prev_tag != curr_tag:
                result[prev_tag] = tags_count
                tags_count = 0

            tags_count += 1
            prev_tag = curr_tag

    if prev_tag is not None:
        result[prev_tag] = tags_count

    result = list(sorted(result.items(), key=lambda x: x[1], reverse=True))[:10]
    for inner_tuple in result:
        for element in inner_tuple:
            print('{} '.format(element), end='')
        print()


if __name__ == "__main__":
    reducer()
