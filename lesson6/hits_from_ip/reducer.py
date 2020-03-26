import sys

prev_ip = None
number_of_hits = 0

for line in sys.stdin:
    current_ip = line.strip().split('\t')
    if len(current_ip) is not 1:
        # Something has gone wrong. Skip this line.
        continue

    if current_ip and current_ip != prev_ip and prev_ip is not None:
        print('{0}\t{1}'.format(prev_ip, number_of_hits))
        number_of_hits = 0

    prev_ip = current_ip
    number_of_hits += 1

if prev_ip is not None:
    print('{0}\t{1}'.format(prev_ip, number_of_hits))

