import pygame
from pygame.event import Event

from src.AbstractEngine import AbstractEngine
from src.Core import Core
from src.Listener.AbstractListener import AbstractListener


class ClickElementListener(AbstractListener):
    """
        Appelle le handle on_click d'un bouton lors d'un click
    """

    def __init__(self, engine: AbstractEngine, elements):
        super().__init__(engine)
        self._elements = elements

    def supports(self, event: Event):
        return event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP

    def handle(self, event: Event, core: Core):
        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for element in self._elements:
                if element.rect().collidepoint(*pos):
                    element.hold()
        else:
            for element in self._elements:
                if element.is_hold() and element.rect().collidepoint(*pos):
                    element.on_click(*pos, core)

                # release all points because mouse button up
                element.release()
