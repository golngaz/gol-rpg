import pygame
from src.Config.ConfigInterface import ConfigInterface
from src.EventDispatcher import EventDispatcher
from src.Game.Character import Character
from src.Game.Charset import Charset
from src.Game.MapDisplayer import MapDisplayer
from src.Game.MapFactory import MapFactory


class Core:
    def __init__(self, config: ConfigInterface, dispatcher: EventDispatcher):
        self._dispatcher = dispatcher
        self._config = config
        self._running = True

        successes, failures = pygame.init()
        print("Initializing pygame: {0} successes and {1} failures.".format(successes, failures))

        self._map_factory = MapFactory(self._config)
        self._map_displayer = MapDisplayer(self._config)

        self._clock = pygame.time.Clock()
        self._screen = pygame.display.set_mode((self._config.get('width'), self._config.get('height')))
        self._fps = self._config.get('fps', 60)

    def configure_displayer(self, visitor):
        visitor.configure_displayer(self._map_displayer, self._map_factory)

    def run(self) -> None:
        self._running = True

        self._map_displayer.load()
        self._map_displayer.draw(self._screen)

        pygame.display.flip()

        while self._running:
            tick = self._clock.tick(self._fps) / 1000

            for event in pygame.event.get():
                self._dispatcher.dispatch(event)

            self._map_displayer.tick(tick)
            self._map_displayer.draw(self._screen)
            pygame.display.flip()

    def quit(self):
        self._running = False

    def __del__(self):
        pygame.quit()
