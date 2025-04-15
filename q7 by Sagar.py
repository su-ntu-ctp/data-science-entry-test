class Car:
    """
    A class to represent a car.

    Attributes:
        make (str): Manufacturer of the car.
        model (str): Model of the car.
        year (int): Year the car was manufactured.
    """

    def __init__(self, make, model, year):
        """
        Initializes a new Car instance with make, model, and year.

        Parameters:
            make (str): Manufacturer of the car.
            model (str): Model of the car.
            year (int): Year of manufacture.
        """
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        """
        Prints a string describing the car in the format: 'Year Make Model'.
        """
        print(f"{self.year} {self.make} {self.model}")
# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Calling the method to print the car description
my_car.describe_car()
