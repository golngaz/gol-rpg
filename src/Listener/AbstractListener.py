from pygame.event import Event
from abc import ABC, abstractmethod
from src import AbstractEngine
from src import Core


class AbstractListener(ABC):
    def __init__(self, engine: AbstractEngine):
        self._engine = engine

    @abstractmethod
    def supports(self, event: Event): ...

    @abstractmethod
    def handle(self, event: Event, core: Core): ...

