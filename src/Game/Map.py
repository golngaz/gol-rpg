

class Map:
    def __init__(self):
        self._layers = []
        self._name = 'default'

    def name(self) -> str:
        return self._name
