from src.AbstractEngine import AbstractEngine
from src.Config.ConfigInterface import ConfigInterface
from src.Game.Character import Character
from src.Game.MapDisplayer import MapDisplayer
from src.Game.MapFactory import MapFactory
from src.Listener.DisplayListener import DisplayListener
from src.Listener.QuitListener import QuitListener


class Editor(AbstractEngine):
    def __init__(self, config: ConfigInterface):
        super().__init__(config)

        self._core.configure_displayer(self)
        self._init_dispatcher()

    def run(self):
        self._core.run()

    def configure_displayer(self, map_displayer: MapDisplayer, map_factory: MapFactory):
        map_displayer.add_map(map_factory.map('start-map'))
        map_displayer.set_current_map('start-map')

    def _init_dispatcher(self):
        self._dispatcher.add_listener(QuitListener(self))
        self._dispatcher.add_listener(DisplayListener(self))

    def player(self) -> Character:
        pass

    def quit(self):
        self._core.quit()
