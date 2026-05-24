from abc import ABC, abstractmethod

class Chooser(ABC):
    @abstractmethod
    def choose_move(self, engine):
        pass