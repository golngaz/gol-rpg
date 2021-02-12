from pygame.event import Event
from abc import ABC, abstractmethod
from src import AbstractEngine


class AbstractListener(ABC):
    def __init__(self, engine: AbstractEngine):
        self._engine = engine

    @abstractmethod
    def supports(self, event: Event): ...

    @abstractmethod
    def handle(self, event): ...

