### INHERITENCE

class Chef:
    def cook_chicken(self):
        print("The chef cooks chicken")

    def cook_salad(self):
        print("The chef prepares salad")

    def cook_special_dish(self):
        print("chef cooks Steak")


class BengaliChef(Chef):
    #A new class can inherit from a parent class by taking the parent class as its parameter...
    def cook_biryani(self):
        print("the chef prepares Biriyani")

    def cook_special_dish(self):
        print("the chef cooks Kabab\n")


rifat = Chef()
rifat.cook_special_dish()

wasif = BengaliChef()
wasif.cook_special_dish()


#more stuff
class Car:
    def __init__(self, model, cost):
        self.model = model
        self.cost = cost

    def Horn(self):
        print("Beep")

    def review(self):
        print("The", self.model, "costs around", self.cost)

        if self.cost >= 100000:
            print("the car's costly\n")
        else:
            print("the car is good for you\n")


class Audi(Car):
    def __init__(self, model, cost, type):      #can have new Parameters except parent Parameters
        super().__init__(model, cost)
        self.type = type

    def Horn(self):
        print("Vmmm")



car1 = Car("Corolla", 70000)
car1.review()

audi1 = Audi("Audi A8", 140000, "SUV")
audi1.review()
