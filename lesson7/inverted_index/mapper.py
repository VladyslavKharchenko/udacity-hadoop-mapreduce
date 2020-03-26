import csv
import sys
import re

# Task:
# Write a MapReduce program that creates an index of all words that can be find in the body of a forum post
# and node id they can be found in.
# Make sure to create a case-insensitive index
# (e.g. "FANTASTIC" and "fantastic" should both count towards the same word).


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')

    for line in reader:
        try:
            id = int(line[0].strip())
            body = line[4]
            words = filter(bool, [word.strip() for word in re.split('[^a-zA-Z0-9\']+', body)])

            for word in words:
                print('{0}\t{1}'.format(word.lower(), id))
        except ValueError:
            continue


if __name__ == "__main__":
    mapper()
