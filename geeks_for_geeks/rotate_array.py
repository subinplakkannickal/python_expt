tests = int(input())

for test in range(tests):
    n, d = map(int, (input().split(' ')))
    _input = input()
    array = list(map(int, _input.split()))
        
    print(*array[d:] + array[:d])
        