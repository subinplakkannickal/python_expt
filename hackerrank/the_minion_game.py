from itertools import combinations

def minion_game(string):
    vowels = "AEIOU"
    # stuarts_score, kevins_score = 0, 0
    # for i,j in combinations(range(len(string) + 1), 2):
    #     if string[i:j][0] in vowels:
    #         kevins_score += 1
    #     else: 
    #         stuarts_score += 1
    string_length = len(string)
    totel = int(string_length * (string_length + 1) / 2)
    kevins_score = sum([1 for i,j in combinations(range(string_length + 1), 2) if string[i:j][0] in vowels])
    stuarts_score = totel - kevins_score

    if kevins_score > stuarts_score:
        print("{} {} ".format("Kevin", kevins_score))
    elif stuarts_score > kevins_score:
        print("{} {} ".format("Stuart", stuarts_score))
    elif stuarts_score == kevins_score:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)  