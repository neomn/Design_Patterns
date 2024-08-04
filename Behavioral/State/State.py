# state_pattern.py

from abc import ABC, abstractmethod

# State interface
class State(ABC):
    @abstractmethod
    def insert_coin(self, vending_machine):
        pass

    @abstractmethod
    def eject_coin(self, vending_machine):
        pass

    @abstractmethod
    def select_item(self, vending_machine):
        pass

# Concrete States
class IdleState(State):
    def insert_coin(self, vending_machine):
        print("Coin inserted")
        vending_machine.set_state(vending_machine.has_coin_state)

    def eject_coin(self, vending_machine):
        print("No coin to eject")

    def select_item(self, vending_machine):
        print("Please insert a coin first")

class HasCoinState(State):
    def insert_coin(self, vending_machine):
        print("Coin already inserted")

    def eject_coin(self, vending_machine):
        print("Coin ejected")
        vending_machine.set_state(vending_machine.idle_state)

    def select_item(self, vending_machine):
        print("Item dispensed")
        if vending_machine.item_count > 0:
            vending_machine.item_count -= 1
            vending_machine.set_state(vending_machine.idle_state)
            if vending_machine.item_count == 0:
                vending_machine.set_state(vending_machine.out_of_stock_state)
        else:
            vending_machine.set_state(vending_machine.out_of_stock_state)

class OutOfStockState(State):
    def insert_coin(self, vending_machine):
        print("Unable to insert coin, machine is out of stock")

    def eject_coin(self, vending_machine):
        print("No coin to eject")

    def select_item(self, vending_machine):
        print("Out of stock")

# Context
class VendingMachine:
    def __init__(self, item_count):
        self.idle_state = IdleState()
        self.has_coin_state = HasCoinState()
        self.out_of_stock_state = OutOfStockState()

        self.item_count = item_count
        self.current_state = self.idle_state if item_count > 0 else self.out_of_stock_state

    def set_state(self, state):
        self.current_state = state

    def insert_coin(self):
        self.current_state.insert_coin(self)

    def eject_coin(self):
        self.current_state.eject_coin(self)

    def select_item(self):
        self.current_state.select_item(self)

# Client code
if __name__ == "__main__":
    vending_machine = VendingMachine(2)

    vending_machine.select_item()  # Please insert a coin first
    vending_machine.insert_coin()  # Coin inserted
    vending_machine.select_item()  # Item dispensed

    vending_machine.insert_coin()  # Coin inserted
    vending_machine.select_item()  # Item dispensed

    vending_machine.select_item()  # Please insert a coin first
    vending_machine.insert_coin()  # Unable to insert coin, machine is out of stock
