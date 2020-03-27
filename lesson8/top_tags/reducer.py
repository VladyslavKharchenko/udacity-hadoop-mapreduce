#!/usr/bin/python

import sys
import csv


def reducer():

    def check_len(dictionary):
        dictionary = dict(list(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))[:10])
        return dictionary

    reader = csv.reader(sys.stdin, delimiter='\t')
    prev_tag = None
    tags_count = 0
    result = {}

    for line in reader:
        if len(line) == 1:
            curr_tag = line[0]

            if prev_tag and prev_tag != curr_tag:
                result[prev_tag] = tags_count
                result = check_len(result)
                tags_count = 0

            tags_count += 1
            prev_tag = curr_tag

    if prev_tag is not None:
        result[prev_tag] = tags_count
        result = check_len(result)

    for tag, counter in result.items():
        print(tag, counter)


if __name__ == "__main__":
    reducer()
