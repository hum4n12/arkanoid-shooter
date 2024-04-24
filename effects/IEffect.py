from abc import ABC, abstractmethod

class IEffect(ABC):

    @abstractmethod
    def apply():
        pass

    @abstractmethod
    def clean_up():
        pass