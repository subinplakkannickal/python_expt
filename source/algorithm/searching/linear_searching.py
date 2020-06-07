from random import randint, choice

def linear_searching(_list, element):
    for i in range(len(_list)):
        if _list[i] == element:
            return i

    return None


if __name__ == "__main__":
    input_list = [randint(0,50) for i in range(20)]

    print(input_list)
    element = choice(input_list)

    index = linear_searching(input_list, element)

    print("index of {}: {}".format(element, index))