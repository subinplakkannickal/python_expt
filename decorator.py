def dec_function(func):
    def _func(*args, **kwargs):
        k =  func(*args, **kwargs)
        return k * 10

    return _func

@dec_function
def func(k):
    return k


if __name__ == "__main__":
    val = func(k=10)
    print(val)
