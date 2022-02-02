""" Abstract module for factory pattern implementation.
"""

from abc import ABCMeta, abstractmethod

class Car(metaclass=ABCMeta):
    """ Abstract class for Car.
    """
    @abstractmethod
    def info(self):
        """ abstract moethod for info.
        This method should be implemented in all child concrete classes
        """
        pass

class SedanCar(Car):
    """ Concrete class for sedan car.
    """
    def info(self):
        """ Implementation of info for Sedan car.
        """
        print("Sedan car is ready to drive")


class SUVCar(Car):
    """ Concrete class for SUV car.
    """
    def info(self):
        """ Implementation of info for SUV car.
        """
        print("SUV car is ready to drive")


class PartsFactory(metaclass=ABCMeta):
    """ Abstract class for parts factory
    """
    @abstractmethod
    def info(self):
        """ Abstract method for info of parts factory.
        """
        pass

    @abstractmethod
    def build_parts(self):
        """Abstract method for build parts.
        """
        pass

class SedanParts(PartsFactory):
    """ Concrete class for Sedan parts
    """
    def info(self):
        return "Maufactured in Sedan Parts Factory"

    def build_parts(self):
        print("Sedan parts built")


class SUVParts(PartsFactory):
    """ Concrete class for SUV parts.
    """
    def info(self):
        return "Maufactured in SUV Parts Factory"

    def build_parts(self):
        print("SUV parts built")


class CarFactory(metaclass=ABCMeta):
    @abstractmethod
    def build(self):
        pass

    @abstractmethod
    def assemble(self):
        pass


class SedanFactory(CarFactory):
    def build(self):
        return SedanParts()

    def assemble(self, parts):
        print ("Sedan car assembled using: {}".format(parts.info()))
        return SedanCar()


class SUVFactory(CarFactory):
    def build(self):
        return SUVParts()

    def assemble(self, parts):
        print ("SUV car assembled using: {}".format(parts.info()))
        return SUVCar()

if __name__ == "__main__":
    sedan_factory = SedanFactory()
    sedan_parts = sedan_factory.build()
    sedan_parts.build_parts()
    sedan_car = sedan_factory.assemble(sedan_parts)
    sedan_car.info()