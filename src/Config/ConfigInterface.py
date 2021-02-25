from __future__ import annotations
from abc import ABC, abstractmethod


class ConfigInterface(ABC):
    @abstractmethod
    def get(self, key: str, default=None): ...

    @abstractmethod
    def set(self, key: str, value) -> ConfigInterface: ...

