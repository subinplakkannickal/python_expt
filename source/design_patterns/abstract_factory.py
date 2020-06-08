from abc import ABCMeta, abstractmethod

class Car(metaclass=ABCMeta):

    @abstractmethod
    def info(self):
        pass

class SedanCar(Car):
    def info(self):
        print("Sedan car is ready to drive")


class SUVCar(Car):
    def info(self):
        print("SUV car is ready to drive")


class PartsFactory(metaclass=ABCMeta):
    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def build_parts(self):
        pass

class SedanParts(PartsFactory):
    def info(self):
        return "Maufactured in Sedan Parts Factory"

    def build_parts(self):
        print("Sedan parts built")


class SUVParts(PartsFactory):
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

    def assemble(self):
        print ("SUV car assembled using: {}".format(parts.info()))
        return SUVCar()

if __name__ == "__main__":
    sedan_factory = SedanFactory()
    sedan_parts = sedan_factory.build()
    sedan_parts.build_parts()
    sedan_car = sedan_factory.assemble(sedan_parts)
    sedan_car.info()