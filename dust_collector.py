# Create a Dust collecotr 
# Practice Python classes, sub classes, abstract classes, its instances and methods

from ABC import  ABC, abstractmethod

class DustCollector(ABC):
    def __init__(self, name):
        self.name = name 