def binary_insertion_sort(new_element, array=None):
    if not array:
        return [new_element]
    
    mid = len(array)//2
        
    if array[mid] == new_element:
        array.insert(mid+1, new_element)
        return array
        
    elif array[mid] > new_element:
        if mid == 0:
            array.insert(0, new_element)
            return array

        array = binary_insertion_sort(new_element, array[:mid]) + array[mid:]

    elif array[mid] < new_element:
        if mid == 0:
            array.append(new_element)
            return array

        array = array[:mid] + binary_insertion_sort(new_element, array[mid:])

    return array

if __name__ == "__main__":
    input = [37, 23, 0, 17, 12, 72, 31, 37, 46, 100, 37, 88, 54]
    sorted_array = None
    for i in input:
        sorted_array = binary_insertion_sort(i, sorted_array)

    print (sorted_array)

    sorted_input = sorted(input)
    print (sorted_input)