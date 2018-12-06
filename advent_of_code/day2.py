import os
from collections import Counter
from itertools import combinations, compress


def checksum(box_ids):
    checksum_counter = [0, 0]
    for id in box_ids:
        # Counter().most_common() returns (key, value) tuples
        # Only the value is needed here
        id_count = [values for key, values in Counter(id).most_common()]
        if 2 in id_count:
            checksum_counter[0] += 1
        if 3 in id_count:
            checksum_counter[1] += 1
    return checksum_counter[0] * checksum_counter[1]

def pairwise(box_ids):
    for i, j in combinations(box_ids, 2):
        comparisons = [str1 == str2 for str1, str2 in zip(i, j)]
        # Count of overlaps in comparisons must be equal to the original string -1
        if sum(comparisons) == len(i)-1:
            different_chars = ''.join(list(compress(i,comparisons)))
            return different_chars

if __name__ == '__main__':
    INPUT_PATH = os.path.join(os.pardir, "input", "day2", "input.txt")
    box_ids = [x.rstrip("\n") for x in open(INPUT_PATH).readlines()]
    print(f"Checksum for the box ids: {checksum(box_ids)}")
    print(f"Overlap in correct box ids: {pairwise(box_ids)}")
