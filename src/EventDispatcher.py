from __future__ import annotations
from pygame.event import Event
from src.Listener.AbstractListener import AbstractListener


class EventDispatcher:
    def __init__(self):
        self._listeners = []

    def add_listener(self, listener: AbstractListener) -> EventDispatcher:
        self._listeners.append(listener)

        return self

    def dispatch(self, event: Event):
        for listener in self._listeners:
            if listener.supports(event):
                listener.handle(event)
