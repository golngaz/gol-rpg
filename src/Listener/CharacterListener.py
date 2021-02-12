import pygame
from pygame.event import Event
from src.Listener.AbstractListener import AbstractListener


class CharacterListener(AbstractListener):

    def supports(self, event: Event):
        return event.type == pygame.KEYDOWN or event.type == pygame.KEYUP

    def handle(self, event):
        player = self._engine.player()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                player.move_up()

            elif event.key == pygame.K_s:
                player.move_down()

            elif event.key == pygame.K_q:
                player.move_left()

            elif event.key == pygame.K_d:
                player.move_right()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_z:
                player.move_up_stop()

            elif event.key == pygame.K_s:
                player.move_down_stop()

            elif event.key == pygame.K_q:
                player.move_left_stop()

            elif event.key == pygame.K_d:
                player.move_right_stop()
