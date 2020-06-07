from random import randint, choice

def jump_searching(_list, element, step):
    idx = None
    for i in range(0, len(_list), step):
        if _list[i] > element:
            idx = i - step
            break
    
    if not idx: idx = len(_list) - step
    if idx < 0: return None

    for j in range(step):
        if _list[idx + j] == element: return idx + j 

    return None

if __name__ == "__main__":
    input_list = [randint(0,50) for i in range(20)]
    input_list.sort()
    print(input_list)

    element, step = choice(input_list), randint(1,5)
    index = jump_searching(input_list, element, step)

    print ("index of {}: {}".format(element, index))