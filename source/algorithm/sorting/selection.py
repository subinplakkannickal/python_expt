def selection_sorting(array):
    len_of_array = len(array)

    for i in range(len_of_array):
        k = i
        k_ = array[i]
        for j in range(i+1, len_of_array):
            if k_ > array[j]:
                k = j
                k_ = array[j]

        array[i], array[k] = array[k], array[i]

    return array


if __name__ == "__main__":
    """ time complexity: O(n^2)
        space complexity: O(1)
    """
    input = ["paper", "true", "soap", "floppy", "flower"]
    sorted_list = selection_sorting(input)
    print (sorted_list)
    sorted_input = sorted(input)
    print (sorted_input)
