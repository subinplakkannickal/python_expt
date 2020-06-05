def bubble_sort(array):
    len_of_array = len(array)

    for i in range(len_of_array):
        _swapped = False
        for j in range(0, len_of_array-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                _swapped = True
            
        if not _swapped:
            break

    return array

def recursive_bubble_sort(array):
    len_of_array = len(array)
    _swapped = False
    for i in range(len_of_array-1):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
            _swapped = True

        if  _swapped:
            recursive_bubble_sort(array)
            break

    return array

if __name__ == "__main__":
    input_1 = [64, 82, 100, 34, 25, 12, 22, 11, 90]
    sorted_list_1 = bubble_sort(input_1)
    print (sorted_list_1)

    sorted_list_2 = recursive_bubble_sort(input_1)
    print (sorted_list_2)

    sorted_input = sorted(input_1)
    print (sorted_input)
