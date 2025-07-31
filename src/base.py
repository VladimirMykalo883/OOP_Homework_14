from abc import ABC, abstractmethod


class LogMixin:
    """Миксин для логирования создания объектов"""
    def __init__(self, *args, **kwargs):
        print(f"Создан объект {self.__class__.__name__} с параметрами:")
        params = []
        for name, value in self.__dict__.items():
            if not name.startswith('_'):
                params.append(f"{name}={value}")
        print(", ".join(params))
        super().__init__(*args, **kwargs)


class BaseClass(ABC):
    """Абстрактный базовый класс для Category и Order"""
    @abstractmethod
    def __init__(self):
        self.name = ""
        self.description = ""

    @abstractmethod
    def __str__(self):
        pass
