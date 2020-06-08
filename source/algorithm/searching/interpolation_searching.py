from random import randint, choice

def interpolation_searching(_list, element):
    len_of_list = len(_list)
    if len_of_list == 0: return None
    if len_of_list == 1: return 0 if _list[0] == element else None
    else:
        pos = (len_of_list-1) // (_list[len_of_list-1] - _list[0]) * (element - _list[0])
        if pos == 0: pos = 1
        print (_list, pos)
        if _list[pos] == element: return pos
        elif _list[pos] > element: return interpolation_searching(_list[:pos], element)
        elif _list[pos] < element: idx = interpolation_searching(_list[pos:], element); return idx + pos if idx else None

if __name__ == "__main__":
    input_list = [randint(0, 50) for i in range(20)]
    input_list.sort()

    element = choice(input_list)

    print(input_list, element)

    index = interpolation_searching(input_list, element)
    print ("index of {}: {}".format(element, index))