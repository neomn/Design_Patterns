from abc import ABC, abstractmethod
from addons import *


class Beverage(ABC):
    
    @abstractmethod
    def get_cost(): ...


class Coffee(Beverage):

    def __init__(self):
        self.cost = 3.0
    
    def get_cost(self):
        return self.cost
    

@sugar
@cream
def get_cost(product):
    return product.get_cost()

coffee = Coffee()
print(get_cost(coffee))



