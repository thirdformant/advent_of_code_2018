import os
from itertools import cycle
import numpy as np

def freq_addition(freq_changes):
    """
    Starting at 0, add value of each item in list and return final result.
    """
    init_freq = 0
    for freq in freq_changes:
        init_freq += freq
    return init_freq

def repeat_freq(freq_changes):
    observed_freqs = {0}
    current_freq = 0
    for n in cycle(freq_changes):
        current_freq += n
        if current_freq in observed_freqs:
            return current_freq
        observed_freqs.add(current_freq)


if __name__ == "__main__":
    INPUT_PATH = os.path.join(os.pardir, "input", "day1", "input.txt")
    freq_changes = [int(x) for x in open(INPUT_PATH).readlines()]
    freq_addition_result = freq_addition(freq_changes)
    print(freq_addition_result) #Print the final result
    part_2 = repeat_freq(freq_changes)
    print(part_2)
