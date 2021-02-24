from __future__ import annotations
from abc import ABC, abstractmethod
from pygame import Rect
from src.Core import Core


class AbstractElement(ABC):

    def __init__(self, rect: Rect):
        """
        :param rect: where is the element and his size
        """
        self._rect = rect
        self._hold = False

    def rect(self) -> Rect:
        return self._rect

    def hold(self) -> AbstractElement:
        self._hold = True

        return self

    def release(self) -> AbstractElement:
        self._hold = False

        return self

    def is_hold(self) -> bool:
        return self._hold

    @abstractmethod
    def on_click(self, x: float, y: float, core: Core):
        self._hold = False
