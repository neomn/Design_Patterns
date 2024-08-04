import copy

class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attr):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class Car:
    def __init__(self):
        self.make = "Ford"
        self.model = "Mustang"
        self.color = "Red"

    def __str__(self):
        return f'{self.make} {self.model} in {self.color}'


# Usage
if __name__ == "__main__":
    car = Car()
    prototype = Prototype()
    prototype.register_object('car', car)

    car2 = prototype.clone('car')
    print(f"Car 1: {car}")
    print(f"Car 2: {car2}")

    car3 = prototype.clone('car', model="Fusion", color="Blue")
    print(f"Car 3: {car3}")
