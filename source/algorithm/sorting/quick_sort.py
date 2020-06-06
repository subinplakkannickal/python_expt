def quick_sort(input_list):

    if len(input_list) <= 1: return input_list

    lesser, equal, greater = [], [], []

    pivot = input_list[0]
    for i in input_list:
        if i < pivot: lesser.append(i)
        elif i == pivot: equal.append(i)
        else: greater.append(i)


    return quick_sort(lesser) + equal + quick_sort(greater)
    
if __name__ == "__main__":
    input_list = [6,8,3,9,0,4,2,7,1,5]
    sorted_list = quick_sort(input_list)
    print (sorted_list)