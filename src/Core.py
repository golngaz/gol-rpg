import pygame
from pygame.surface import Surface
from src.Config.ConfigInterface import ConfigInterface
from src.Displayer import Displayer
from src.EventDispatcher import EventDispatcher


class Core:
    def __init__(self, config: ConfigInterface, dispatcher: EventDispatcher, displayer: Displayer):
        self._loaded = False
        self._dispatcher = dispatcher
        self._config = config
        self._running = True

        successes, failures = pygame.init()
        print("Initializing pygame: {0} successes and {1} failures.".format(successes, failures))

        self._displayer = displayer

        self._clock = pygame.time.Clock()
        self._screen = pygame.display.set_mode((self._config.get('width'), self._config.get('height')))
        self._fps = self._config.get('fps', 60)

    def load(self, force: bool = False) -> None:
        if force or not self._loaded:
            self._displayer.load()
            self._loaded = True

    def run(self) -> None:
        self.load()
        self._displayer.draw(self._screen)

        pygame.display.flip()

        self._running = True
        while self._running:
            tick = self._clock.tick(self._fps) / 1000

            for event in pygame.event.get():
                self._dispatcher.dispatch(event, self)

            self._displayer.tick(tick)
            self._displayer.draw(self._screen)
            pygame.display.flip()

    def displayer(self) -> Displayer:
        return self._displayer

    def quit(self):
        self._running = False

    def __del__(self):
        pygame.quit()
