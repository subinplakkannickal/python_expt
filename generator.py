"""
Generator: The function which can be behave as a iterator.
"""

def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

class FirstN(object):
    def __init__(self, n):
        self.n = n
        self.num = 0

    def __iter__(self):
        return self

    # Python 3 compatibility
    def __next__(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num+1
            return cur
        else:
            raise StopIteration()


if __name__ == "__main__":
    sum_of_first_n = sum(firstn(1000000))
    sum_of_first_n_cls = sum(FirstN(1000000))
    print("Output of generator.py")
    print(sum_of_first_n)
    print(sum_of_first_n_cls)