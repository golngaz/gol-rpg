from pygame import Surface
from src.DisplayerInterface import DisplayerInterface
from src.Menu.AbstractElement import AbstractElement


class EditorDisplayer(DisplayerInterface):
    def __init__(self):
        self._elements = list()

    @staticmethod
    def name():
        return 'EditorDisplayer'

    def add_element(self, element: AbstractElement):
        self._elements.append(element)

    def load(self) -> None:
        for element in self._elements:
            element.load()

    def tick(self, tick) -> None:
        pass

    def draw(self, surface: Surface) -> None:
        for element in self._elements:
            element.draw(surface)

    def elements(self) -> list:
        return self._elements
