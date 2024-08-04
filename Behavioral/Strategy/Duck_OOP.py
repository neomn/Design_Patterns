#-----------------------  base class  -------------------
class Duck():

    def eat(self, food: str):
        print(f"base_class: i'm eating {food}")
    
    def quack(self):
        print('base_class: quack quack')

    def fly(self, source: str, destination: str):
        print(f"base_class: flying from {source} to {destination}")



#-----------------------  child classes  -------------------
class WildDuck(Duck):

    def quack(self): # wild duck re-implemented quack method since it has different quack behavior
        print('wild_duck: i quack like a wild duck')


class RubberDuck(Duck):
    
    def fly(self, source: str, destination: str): # rubber docker must re-implement fly since it can't fly
        print("rubber_duck: i can't fly, i'm a rubber duck")



#-----------------------  objects  -------------------
rubber_duck = RubberDuck()
wild_duck = WildDuck()

rubber_duck.quack()
rubber_duck.eat('apple')
rubber_duck.fly('point A', 'point B')
print()

wild_duck.quack()
wild_duck.eat('bannana')
wild_duck.fly('point A', 'point B')


