def selection_sorting(array):
    """ Selection sorting.
    """
    len_of_array = len(array)

    for i in range(len_of_array):
        min_pos = i
        for j in range(i+1, len_of_array):
            if array[min_pos] > array[j]:
                min_pos = j

        array[i], array[min_pos] = array[min_pos], array[i]

    return array


if __name__ == "__main__":
    """ time complexity: O(n^2)
        space complexity: O(1)
    """
    input = ["paper", "true", "soap", "floppy", "flower"]
    sorted_list = selection_sorting(input)
    print(sorted_list)
    sorted_input = sorted(input)
    print(sorted_input)

