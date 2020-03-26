import sys

prev_word = None
nodes = set()
used_counter = 0

for line in sys.stdin:
    data_mapped = line.strip().split('\t')
    if len(data_mapped) is not 2:
        # Something has gone wrong. Skip this line.
        continue

    curr_word, node_id = data_mapped

    if curr_word and curr_word != prev_word and prev_word is not None:
        print('{0}\t{1}\t{2}'.format(prev_word, nodes, used_counter))
        nodes = set()
        used_counter = 0

    prev_word = curr_word
    nodes.add(int(node_id))
    used_counter += 1

if prev_word is not None:
    print('{0}\t{1}'.format(prev_word, nodes))

