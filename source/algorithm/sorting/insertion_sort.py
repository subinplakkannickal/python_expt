def insertion_sort(new_element, array=None):
    if not array:
        return [new_element]

    if new_element >= array[-1]:
        array.append(new_element)

    else:
        array = insertion_sort(new_element, array[:len(array)-1]) + [array[-1]]

    return array

if __name__ == "__main__":
    input = [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
    sorted_array = None
    for i in input:
        sorted_array = insertion_sort(i, sorted_array)

    print (sorted_array)

    sorted_input = sorted(input)
    print (sorted_input)