"""
Implement an algo to determine if a string has all unique characters
INPUT: "abcd"
Output: True
INPUT: "aaaaaa"
Output: False
"""

def unique_char_check(input_string):
    if len(set(input_string)) == len(input_string):
        return True
    
    return False

if __name__ == "__main__":
    user_input = input()
    result = unique_char_check(user_input)
    print (result)