from random import randint


def find_ones(value):
    ones_count = 0
    while value:
        ones_count += value & 1
        value >>= 1

    return ones_count

if __name__ == "__main__":
    value = randint(0,50)
    once_count = find_ones(value)    
    print ("Count of ones in {}({}): {}".format(value, bin(value), once_count))