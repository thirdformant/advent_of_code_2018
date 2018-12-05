import os

def file_to_intlist(input_file):
    """
    Read input file to list of integers
    """
    list = []
    with open(input_file, "r") as f:
        for line in f:
            list.append(int(line.rstrip()))
    f.close()
    return list

def freq_addition(list):
    """
    Starting at 0, add value of each item in list and return final result.
    """
    init_freq = 0
    for freq in list:
        init_freq += freq
    return init_freq


if __name__ == "__main__":
    input_file = os.path.join(os.pardir, "input", "day1", "input.txt")
    freq_values = file_to_intlist(input_file)
    freq_addition_result = freq_addition(freq_values)
    print(freq_addition_result) #Print the final result
