class Singleton(object):
    _instance = None

    def __new__(self):
        if not self._instance:
            self._instance = super(Singleton, self).__new__(self)
        
        return self._instance

class SingletonMeta(type):
    _instance = None
    def __call__(self):
        if not self._instance:
            self._instance = super(SingletonMeta, self).__call__()
        
        return self._instance

class MyClass(metaclass=SingletonMeta):
    pass

def singleton(class_):
    _instance = {}
    def create_instance(*args, **kwargs):
        if not class_ in _instance:
            _instance[class_] = class_(*args, **kwargs)

        return _instance[class_]
    
    return create_instance


@singleton
class MyAnotherClass(object):
    def __init__(self, a, b):
        print(a, b)


if __name__ == "__main__":
    inst = Singleton()
    inst_2 = Singleton()
    print (inst, inst_2)

    inst_3 = MyClass()
    inst_4 = MyClass()
    print (inst_3, inst_4)

    inst_5 = MyAnotherClass(1,2)
    inst_6 = MyAnotherClass(3,4)
    print (inst_5, inst_6)
