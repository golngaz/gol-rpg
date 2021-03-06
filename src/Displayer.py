from pygame import Surface
from src.DisplayerInterface import DisplayerInterface


class Displayer:
    def __init__(self):
        self._displayers = {}

    def add_displayer(self, displayer: DisplayerInterface):
        self._displayers[displayer.name()] = displayer

    def get(self, displayer_name: str):
        return self._displayers[displayer_name]

    def load(self):
        for displayer_name in self._displayers:
            self._displayers[displayer_name].load()

    def tick(self, tick):
        for displayer_name in self._displayers:
            self._displayers[displayer_name].tick(tick)

    def draw(self, surface: Surface):
        for displayer_name in self._displayers:
            self._displayers[displayer_name].draw(surface)
