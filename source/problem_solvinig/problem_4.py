"""
You have 2 sorted arrays A and B, where A has large enough buffer at end to hold B.
Write a method to merge B into A in sorted order
"""

def binary_insertion_sort(array, new_element):
    if not len(array):
        return [new_element]

    mid = len(array) //2

    if array[mid] == new_element:
        array.insert(mid+1, new_element)
        return array

    elif array[mid] < new_element:
        if mid == 0:
            array.append(new_element)
            return array

        return array[:mid] + binary_insertion_sort(array[mid:], new_element)

    else:
        if mid == 0:
            array.insert(0, new_element)
            return array
        
        return binary_insertion_sort(array[:mid], new_element) + array[mid:]
        


if __name__ == "__main__":
    first_array = list(map(int, input().split()))
    second_array = list(map(int, input().split()))

    for i in second_array:
        first_array = binary_insertion_sort(first_array, i)

    print (first_array)