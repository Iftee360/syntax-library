### GETTERS & SETTERS

## Not commonly used in python, but it serves a good purpose when writing classes

class Car:
    def __init__ (self, model, cost):            #initialize constructor
        self.model = model
        self.cost = cost

    @property
    def model(self):
        print("getting model")
        return self._model

    @model.setter
    def model(self, value):
        print("setting model")
        self._model = value

    @model.deleter
    def model(self):
        del self._model


    def review_car(self):               #self is mendatory, which refers to the craeted object

        print("The", self.model, "Car costs around", self.cost)

        if self.cost >= 100000:
            print("The car is costly, think before buying...\n")
        else:
            print("Price is within budget\n")



car1 = Car("Audi A8", 280000)
car1.review_car()

car2 = Car("Toyota X Corolla", 70000)
car2.review_car()
