from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def __init__(self):
        self.observers = []

    @abstractmethod
    def attach(self, observer):
        self.observers.append(observer)

    @abstractmethod
    def detach(self, observer):
        self.observers.remove(observer)

    @abstractmethod
    def notify(self, operation):
        for observer in self.observers:
            observer.update(self, operation)
