#!/usr/bin/python

import sys
import csv


def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')

    prev_post_id = None
    students = []

    for line in reader:
        if len(line) == 2:

            curr_post_id, student_id = line
            curr_post_id, student_id = int(curr_post_id), int(student_id)

            if prev_post_id and prev_post_id != curr_post_id:
                print("{0}\t{1}".format(prev_post_id, students))
                students.clear()

            students.append(student_id)
            prev_post_id = curr_post_id

    if prev_post_id is not None:
        print("{0}\t{1}".format(prev_post_id, students))


if __name__ == "__main__":
    reducer()
