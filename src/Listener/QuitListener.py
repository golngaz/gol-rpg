from pygame import QUIT
from pygame.event import Event
from src.Core import Core
from src.Listener.AbstractListener import AbstractListener


class QuitListener(AbstractListener):
    def supports(self, event: Event):
        return event.type == QUIT

    def handle(self, event: Event, core: Core):
        self._engine.quit()
