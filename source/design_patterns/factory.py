# Factory pattern
from abc import ABCMeta, abstractmethod

# Abstract concrete class
class Item(metaclass=ABCMeta):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def value(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# Concrete class for video
class Video(Item):
    def __init__(self, name, value, start, stop):
        self._name = name
        self._value = value
        self._start = start
        self._stop = stop

    def __repr__(self):
        return 'Video({},{},{},{})'.format(self._name, self._value, self._start, self._stop)
        
    def name(self):
        return self._name

    def value(self):
        return self._value

    def start(self):
        return self._start

    def stop(self):
        return self._stop


# Concrete class for audio
class Audio(Item):
    def __init__(self, name, value, start, stop):
        self._name = name
        self._value = value
        self._start = start
        self._stop = stop

    def __repr__(self):
        return 'Audio({},{},{},{})'.format(self._name, self._value, self._start, self._stop)
        
    def name(self):
        return self._name

    def value(self):
        return self._value

    def start(self):
        return self._start

    def stop(self):
        return self._stop


# Concrete class for reference
class Reference(Item):
    def __init__(self, name, value, start, stop):
        self._name = name
        self._value = value
        self._start = start
        self._stop = stop

    def __repr__(self):
        return 'Reference({},{},{},{})'.format(self._name, self._value, self._start, self._stop)
        
    def name(self):
        return self._name

    def value(self):
        return self._value

    def start(self):
        return self._start

    def stop(self):
        return self._stop


# factory class
class ItemFactory(object):

    @classmethod
    def get_item(cls, type, name, value, start, stop):
        return eval(type)(name, value, start, stop)

if __name__ == "__main__":
    video = ItemFactory.get_item('Video', 'vid_1', 100, 0, 200)
    print (video)
    audio = ItemFactory.get_item('Audio', 'aud_1', 100, 0, 200)
    print (audio)
    reference = ItemFactory.get_item('Reference', 'ref_1', 100, 0, 200)
    print (reference)
    video2 = ItemFactory.get_item('Video', 'vid_2', 100, 0, 200)
    print (video2)


