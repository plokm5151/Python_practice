class Driver:
    def __init__(self):
        my=123
    
    def __xpaht(self):
        print('Yes!')
    
    def get_xpath(self):
        self.__xpaht()
class Car:
    def __init__(self, make, model, year, speed):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__speed = speed

    def test(self):
        #Driver.__xpaht(0)
        ddd=Driver()
        ddd.get_xpath()
        
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_speed(self):
        return self.__speed

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def set_speed(self, speed):
        self.__speed = speed

my_car = Car("Toyota", "Corolla", 2020, 0)

my_car.test()


#my_car.set_speed(60)

#print("My car is a " + my_car.get_make() + " " + my_car.get_model() + " " + str(my_car.get_year()) + " model and is currently traveling at " + str(my_car.get_speed()) + " mph.")