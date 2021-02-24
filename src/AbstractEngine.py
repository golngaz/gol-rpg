from abc import ABC, abstractmethod

from src.Config.ConfigInterface import ConfigInterface
from src.Core import Core
from src.Displayer import Displayer
from src.EventDispatcher import EventDispatcher
from src.Game.Character import Character


class AbstractEngine(ABC):

    def __init__(self, config: ConfigInterface):
        self._dispatcher = EventDispatcher()
        self._displayer = Displayer()
        self._core = Core(config, self._dispatcher, self._displayer)

    @abstractmethod
    def player(self) -> Character: ...

    @abstractmethod
    def run(self): ...

    @abstractmethod
    def quit(self): ...
