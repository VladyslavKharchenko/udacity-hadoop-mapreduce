#!/usr/bin/python

import sys
import csv


def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')

    prev_post_id = None
    average_answer_len = 0.0
    answers_count = 0
    question_len = None

    for line in reader:
        if len(line) == 3:

            curr_post_id, curr_post_len, type = line
            curr_post_id, curr_post_len = int(curr_post_id), int(curr_post_len)

            if prev_post_id and prev_post_id != curr_post_id:
                if answers_count is 0:
                    print("{0}\t{1}\t{2}".format(prev_post_id, question_len, average_answer_len))
                else:
                    print("{0}\t{1}\t{2}".format(prev_post_id, question_len, average_answer_len / answers_count))
                average_answer_len = 0.0
                answers_count = 0
                question_len = None

            if type == 'A':
                average_answer_len += curr_post_len
                answers_count += 1
            elif type == 'Q':
                question_len = curr_post_len

            prev_post_id = curr_post_id

    if prev_post_id is not None:
        if answers_count is 0:
            print("{0}\t{1}\t{2}".format(prev_post_id, question_len, average_answer_len))
        else:
            print("{0}\t{1}\t{2}".format(prev_post_id, question_len, average_answer_len / answers_count))


if __name__ == "__main__":
    reducer()
