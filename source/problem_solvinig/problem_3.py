"""
Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""

def string_compression(input_string):
    unique_chars = sorted(set(input_string))
    compressed_string = ''
    for i in unique_chars:
        compressed_string += "{}{}".format(i, input_string.count(i))
    
    return compressed_string

if __name__ == "__main__":
    user_input = input()
    if user_input.isalpha():
        compressed_string = string_compression(user_input)
        print (compressed_string)
    else:
        print ("Invalid input")