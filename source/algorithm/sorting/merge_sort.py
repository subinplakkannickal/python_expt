def merge_sort(input_list):
    len_of_list = len(input_list)
    if len_of_list > 1:
        mid = len_of_list // 2
        left = merge_sort(input_list[:mid])
        right = merge_sort(input_list[mid:])
        
        if len(left) == 0 or len(right) == 0:
            return left or right

        i, j = 0, 0
        result = []
        while i + j >= len(result):
            if left[i] > right[j]:
                result.append(right[j])
                j += 1
            
            else:
                result.append(left[i])
                i += 1

            if i == len(left):
                result.extend(right[j:])

            elif j == len(right):
                result.extend(left[i:])

        return result

    else:
        return input_list


if __name__ == "__main__":
    input_list = [6,8,3,9,0,4,2,7,1,5]
    sorted_list = merge_sort(input_list)
    print (sorted_list)
