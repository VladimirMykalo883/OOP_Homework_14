'''ДЗ_16_2'''
from abc import ABC, abstractmethod
from typing import Any


class LogMixin:
    """Миксин для логирования создания объектов"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        print(f"Создан объект {self.__class__.__name__} с параметрами:")
        params = []
        for name, value in self.__dict__.items():
            if not name.startswith("_"):
                params.append(f"{name}={value}")
        print(", ".join(params))
        super().__init__(*args, **kwargs)


class BaseClass(ABC):
    """Абстрактный базовый класс для Category и Order"""

    @abstractmethod
    def __init__(self) -> None:
        #        self.name = ""
        #        self.description = ""
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass
