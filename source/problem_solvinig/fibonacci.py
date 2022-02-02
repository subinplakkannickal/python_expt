def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n

if __name__ == "__main__":
    for i in range(20):
        print(fibonacci(i), end=" ")

    print(factorial(11))
