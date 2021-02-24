from abc import ABC, abstractmethod
from pygame import Surface


class DisplayerInterface(ABC):

    @staticmethod
    @abstractmethod
    def name() -> str: ...

    @abstractmethod
    def load(self) -> None: ...

    @abstractmethod
    def tick(self, tick) -> None: ...

    @abstractmethod
    def draw(self, surface: Surface) -> None: ...
