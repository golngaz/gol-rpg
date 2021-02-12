from abc import ABC, abstractmethod

from src.Config.ConfigInterface import ConfigInterface
from src.Core import Core
from src.EventDispatcher import EventDispatcher
from src.Game.Character import Character
from src.Game.MapDisplayer import MapDisplayer
from src.Game.MapFactory import MapFactory


class AbstractEngine(ABC):

    def __init__(self, config: ConfigInterface):
        self._dispatcher = EventDispatcher()
        self._core = Core(config, self._dispatcher)

    @abstractmethod
    def player(self) -> Character: ...

    @abstractmethod
    def configure_displayer(self, map_displayer: MapDisplayer, map_factory: MapFactory) -> None: ...

    @abstractmethod
    def run(self): ...

    @abstractmethod
    def quit(self): ...
