from abc import ABC, abstractmethod
from functools import wraps

def sugar(func): 
    SUGAR_COST = 0.35
    def wrapper(product):
        product_cost = func(product)
        return product_cost + SUGAR_COST
    return wrapper
    

def cream(func): 
    CREAM_COST = 2.5
    def wrapper(product):
        product_cost = func(product)
        return product_cost + CREAM_COST
    return wrapper
 
