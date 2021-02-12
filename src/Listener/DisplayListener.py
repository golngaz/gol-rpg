import pygame
from pygame.event import Event
from src.Listener.AbstractListener import AbstractListener


class DisplayListener(AbstractListener):
    def supports(self, event: Event):
        return event.type == pygame.KEYDOWN and event.key == pygame.K_F11

    def handle(self, event):
        pygame.display.toggle_fullscreen()
