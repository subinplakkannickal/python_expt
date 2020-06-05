def dec_function(func, *args, **kwargs):
    def _func(*args, **kwargs):
        return func(*args, **kwargs) ** 2

    return _func

@dec_function
def func(k):
    return k


if __name__ == "__main__":
    val = func(k=2)
    print(val)
