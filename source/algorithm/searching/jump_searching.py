"""Jump search
"""
from random import sample, choice
from math import sqrt

def jump_searching(_list, element, step):
    """ Jump search
    """
    arr_len = len(_list)
    idx = 0

    for idx in range(0, len(_list) + step, step):
        idx = min(idx, len(_list)-1)
        if _list[idx] == element:
            return idx

        if _list[idx] > element:
            idx -= step
            break

    if idx < 0:
        idx = 0

    for j in range(step+1):
        if _list[idx + j] == element:
            return idx + j

    return None

if __name__ == "__main__":
    input_list = sample(range(50), 20)
    input_list.sort()
    print(input_list)

    element, step =  choice(input_list), int(sqrt(len(input_list)))
    index = jump_searching(input_list, element, step)

    print("index of {}: {}".format(element, index))
