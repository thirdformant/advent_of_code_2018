import os
from itertools import cycle

def freq_addition(freq_changes):
    return sum(freq_changes)

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
    print(f"Final frequency: {freq_addition(freq_changes)}")
    print(f"First repeated frequency: {repeat_freq(freq_changes)}")
