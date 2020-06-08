"""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

    Mat size must be N x M(N is an odd natural number, and M is 3 times.)
    The design should have 'WELCOME' written in the center.
    The design pattern should only use |, . and - characters.
"""

if __name__ == "__main__":
    n, m = map(int, input('N x M: ').split())

    for i in range(n//2):
        print('-'* (3 * (n//2 -i)) +'.|.' * (2*i+1) + '-' *(3*(n//2 -i)))
    print('-'*((m-7)//2)+'WELCOME'+'-'*((m-7)//2))
    for i in range(n//2):
        print('-'* (3 * (i+1)) +'.|.' * (n -(2*i)-2) + '-' *(3*(i+1)))