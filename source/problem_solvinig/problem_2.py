"""
Write a function to determine the number of bits you would need to flip to convert integer A to integer B
Ex:
Input: 29 (or: 11101), 15 (or: 01111)
Output: 2
"""
def make_bytes_same_size(number, req_len):
    return '{}{}'.format('0' * (req_len-len(number)), number)

if __name__ == "__main__":
    first_input = int(input())
    second_input = int(input())
    bytes_of_first_number = bin(first_input).replace('0b', "")
    bytes_of_second_number = bin(second_input).replace('0b', "")
    len_of_first_number = len(bytes_of_first_number)
    len_of_second_number = len(bytes_of_second_number)
    max_of_len = max(len_of_first_number, len_of_second_number)
    bytes_of_first_number = make_bytes_same_size(bytes_of_first_number, max_of_len)
    bytes_of_second_number = make_bytes_same_size(bytes_of_second_number, max_of_len)
    print(bytes_of_first_number, bytes_of_second_number)