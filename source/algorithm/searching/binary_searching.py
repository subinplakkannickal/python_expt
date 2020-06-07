from random import randint, choice

def binary_searching(_list, element):
    len_of_list = len(_list)
    if len_of_list == 0: return None
    if len_of_list == 1: return 0 if _list[0] == element else None
    else:
        mid = len_of_list // 2
        if _list[mid] == element: return mid
        elif _list[mid] > element: return binary_searching(_list[:mid], element)
        elif _list[mid] < element: index = binary_searching(_list[mid:], element); return index + mid if index else None

if __name__ == "__main__":
    input_list = sorted([randint(i, 50) for i in range(20)])
    print(input_list)
    element = choice(input_list)
    index = binary_searching(input_list, element)
    print("index of {}: {}".format(element, index))