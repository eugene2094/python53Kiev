import copy


class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def clone(self):
        return copy.copy(self)


prototype_car = Car('Tesla model S', 'black')
cloned_car = prototype_car.clone()
print("Original car: ", prototype_car)
print("cloned car: ", cloned_car)
