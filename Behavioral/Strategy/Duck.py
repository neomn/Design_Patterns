from abc import ABC, abstractmethod
from DuckStrategies import *


class Duck(ABC):
    
    def __init__(self):
        pass

    @abstractmethod
    def quack(self): ...
        
    @abstractmethod
    def eat(self): ...
        
    @abstractmethod
    def fly(self): ...

    

class RubberDuck(Duck): 
    
    def __init__(self):
        self.strategies = {}
        self.strategies['quack'] = Quack()
        self.strategies['eat'] = Eat()
        self.strategies['fly'] = Fly()

    def quack(self):
        self.quack = self.strategies['quack'].funny()

    def eat(self):
        self.quack = self.strategies['eat'].unable()

    def fly(self):
        self.quack = self.strategies['fly'].unable()


class WildDuck(Duck): 
    
    def __init__(self):
        self.strategies = {}
        self.strategies['quack'] = Quack()
        self.strategies['eat'] = Eat()
        self.strategies['fly'] = Fly()

    def quack(self):
        self.quack = self.strategies['quack'].matting()

    def eat(self):
        self.quack = self.strategies['eat'].fast()

    def fly(self):
        self.quack = self.strategies['fly'].jet()




rubber_duck = RubberDuck()
rubber_duck.quack()
rubber_duck.eat()
rubber_duck.fly()

print()
wild_duck = WildDuck()
wild_duck.quack()
wild_duck.eat()
wild_duck.fly()

