
class Car:

    # Constructor: a method that gets called when an instance of a Class is created
    # 'self' parameter is mendatory, which refers to the craeted object. Except that others are parameters you require

    def __init__ (self, model, cost):            #initialize constructor
        self.model = model
        self.cost = cost


    # Method: a function inside of a Class

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
