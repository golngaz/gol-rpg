from pygame import QUIT
from pygame.event import Event
from src.Listener.AbstractListener import AbstractListener


class QuitListener(AbstractListener):
    def supports(self, event: Event):
        return event.type == QUIT

    def handle(self, event):
        self._engine.quit()
