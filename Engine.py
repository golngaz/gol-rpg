import pygame
from pygame.locals import *
from src.Config.ConfigInterface import ConfigInterface
from src.Game.Character import Character
from src.Game.Charset import Charset
from src.Game.MapFactory import MapFactory


class Engine:
    def __init__(self, config: ConfigInterface):
        self._config = config
        self._running = True
        self._map_factory = MapFactory(self._config)
        successes, failures = pygame.init()
        print("Initializing pygame: {0} successes and {1} failures.".format(successes, failures))

        self._clock = pygame.time.Clock()
        self._screen = pygame.display.set_mode((self._config.get('width'), self._config.get('height')))
        self._fps = self._config.get('fps', 60)

    def run(self) -> None:
        self._running = True

        map = self._map_factory.map('start-map')
        map.load()
        map.draw(self._screen)

        player = Character(Charset('asset/charset/armored-npcs.png', 48, 72, 8, 3, 4, 4))
        player.load()
        player.draw(self._screen)
        pygame.display.flip()

        while self._running:
            tick = self._clock.tick(self._fps) / 1000
            self._screen.fill((100, 150, 100))

            for event in pygame.event.get():
                if event.type == QUIT:
                    self._running = False

                elif event.type == pygame.KEYDOWN:
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

            # print(player)
            player.tick(tick, self._screen)
            map.draw(self._screen)
            player.draw(self._screen)
            pygame.display.flip()

    def __del__(self):
        pygame.quit()
