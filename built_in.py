class BuiltIn(object):
    def __init__(self):
        print ('__init__ called')

    def __new__(cls):
        print ('__new__ called')
        return super(BuiltIn, cls).__new__(cls)

    def __call__(self):
        print ('__call__ called')

    def __repr__(self):
        return '__repr__ called'

    def __len__(self):
        print ('__len__ called')
        return 0

    def __del__(self):
        print ('__del__ called')

